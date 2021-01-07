from flask import request
from flask_restful import Resource
from models.models import Account
import hashlib
from itsdangerous import base64_encode


class AccountLoginResource(Resource):

    def post(self):
        request_data = request.get_json(force=True)
        current_account = Account.find_by_email(request_data['email'])
        try:
            if not current_account:
                return {'message': 'User {} doesn\'t exist'.format(request_data['email'])}, 400

            if hashlib.sha256(request_data['password'].encode()).hexdigest() == current_account.password:
                token = Account.generate_token(current_account.email)
                encoded_token = base64_encode(token)
                return {
                    'message': 'Logged in as {}'.format(request_data['email']),
                    'token': encoded_token.decode('utf-8')
                    }, 200
            else:
                return {'message': 'Wrong credentials'}, 400
        except:
            return {'message': 'Something went wrong'}, 500
