from flask import request, jsonify
from flask_restful import Resource
from models import db, Account, AccountSchema
import status_codes
import uuid
accounts_schema = AccountSchema(many=True)
account_schema = AccountSchema()
from resources.secret import validate_authentication
import flask
import hashlib

class AccountResource(Resource):

    # def get(self):
    #     accounts = Account.query.all()
    #     accounts = accounts_schema.dump(accounts)
    #     return {'status': 'success', 'data': accounts}, status_codes.HTTP_200_OK

    def post(self):
        request_data = request.get_json(force=True)
        if not request_data:
               return {'message': 'No input data provided'}, status_codes.HTTP_400_BAD_REQUEST

        account = Account(username=request_data["username"],
                          password=request_data["password"],
                          email=request_data["email"],
                          id=str(uuid.uuid4()))
        try:
            if not account.if_exists(email=request_data["email"]):
                db.session.add(account)
                db.session.commit()
            else:
                return {'message': 'Account already exists'}, status_codes.HTTP_400_BAD_REQUEST

            request_result = account_schema.dump(account)

            return {
                "status": 'success',
                'message': 'Account {} was created'.format(request_data['email']),
                'data': request_result
                }, status_codes.HTTP_201_CREATED
        except:
            return {'message': 'Something went wrong'}, status_codes.HTTP_500_INTERNAL_SERVER_ERROR

    @validate_authentication
    def put(self):
        request_data = request.get_json(force=True)
        if not request_data:
            return {'message': 'No input data provided'}, status_codes.HTTP_400_BAD_REQUEST
        account_id = flask.g.user_id
        account = Account.get_accopunt_by_id(account_id)
        try:

            if request_data["username"]:
                account.username = request_data["username"]
            if request_data["email"]:
                account.email = request_data["email"]
            if request_data["password"]:
                hashed_password = hashlib.sha256(request_data["password"].encode()).hexdigest()
                account.password = hashed_password
            db.session.commit()
            request_result = account_schema.dump(account)
            return {"status": 'success', 'data': request_result}, status_codes.HTTP_200_OK
        except:
            return {'message': 'Something went wrong'}, status_codes.HTTP_500_INTERNAL_SERVER_ERROR
