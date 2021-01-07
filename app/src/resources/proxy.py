import logging
from collections import Counter

import requests
from flask import current_app
from flask import request, Response
from flask_restful import Resource
from itsdangerous import base64_decode

from exceptions import NoHealthyInstancesForDomainException
from lb.lb import LoadBalancing
from models.models import Account
from utils.utils import Utils


request_counter = Counter()
log = logging.getLogger('proxy')


class ProxyRouteResource(Resource):

    def set_instance(self):
        request_counter['requests'] += 1
        domain = Utils.extract_domain(request.url)
        lb = LoadBalancing().get_lb_algorithm(domain, request_counter)
        instance_details = lb.pick_instance()
        url = 'http://{}:{}'.format(instance_details[0], instance_details[1])
        log.debug('sending request to url: {}'.format(url))
        return url, domain

    def check_auth(self):
        if current_app.config["AUTH_ENABLED"]:
            log.info("Authentication enabled, proceeding further")
            request_headers = request.headers
            token = request_headers['Authorization']
            try:
                decoded_token = base64_decode(token)
                if decoded_token:
                    return Account.verify_token(decoded_token)
            except Exception as e:
                return "Authentication failed: {}".format(e)
        else:
            log.info("Authentication disabled, proceed as anonymous")
            return True

    def proxy_data(self, resp, domain):
        try:
            headers = [(name, value) for (name, value) in resp.raw.headers.items()]
            log.debug('received response: {}'.format(resp.content))
            response = Response(resp.content, resp.status_code, headers)
            return response
        except NoHealthyInstancesForDomainException as e:
            log.error('Exception: no healthy instances found for domain: {}'.format(domain))
            return {'Exception': str(e)}, 404
        except requests.exceptions.RequestException as e:
            return {'Exception': str(e)}, 500

    def post(self):
        auth_reponse = self.check_auth()
        if auth_reponse == True:
            url, domain = self.set_instance()
            resp = requests.post(url, json=request.get_json())
            return self.proxy_data(resp, domain)
        else:
            return "Authentication failed"

    def get(self):
        auth_reponse = self.check_auth()
        if auth_reponse == True:
            url, domain = self.set_instance()
            resp = requests.get(url)
            return self.proxy_data(resp, domain)
        else:
            return "Authentication failed"
