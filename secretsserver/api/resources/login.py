from flask import request
from flask_restful import Resource
from models import Account
import status_codes
import hashlib
from itsdangerous import base64_encode


class AccountLoginResource(Resource):

    def post(self):
        request_data = request.get_json(force=True)
        current_account = Account.find_by_email(request_data['email'])
        try:
            if not current_account:
                return {'message': 'User {} doesn\'t exist'.format(request_data['email'])}, status_codes.HTTP_400_BAD_REQUEST

            if hashlib.sha256(request_data['password'].encode()).hexdigest() == current_account.password:
                token = Account.generate_token(current_account.email)
                print(token)
                encoded_token = base64_encode(token)
                return {
                    'message': 'Logged in as {}'.format(request_data['email']),
                    'token': encoded_token.decode('utf-8')
                    }, status_codes.HTTP_200_OK
            else:
                return {'message': 'Wrong credentials'}, status_codes.HTTP_400_BAD_REQUEST
        except:
            return {'message': 'Something went wrong'}, status_codes.HTTP_500_INTERNAL_SERVER_ERROR

