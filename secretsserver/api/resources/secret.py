from functools import wraps
from flask import request
from flask_restful import Resource
from models import db, Secret, SecretSchema, Account
import status_codes
import uuid
import flask
from itsdangerous import base64_decode
secrets_schema = SecretSchema(many=True)
secret_schema = SecretSchema()


def validate_authentication(func):
    @wraps(func)
    def inner(*args, **kwargs):
        request_headers = request.headers
        token = request_headers['Authorization']
        decoded_token = base64_decode(token)
        if decoded_token:
            flask.g.user_id = Account.verify_token(decoded_token)
        else:
            return status_codes.HTTP_400_BAD_REQUEST
        return func(*args, **kwargs)
    return inner


class SecretResource(Resource):
    SECRET_TYPE = ["password","certificate","privatekey"]

    @validate_authentication
    def get(self):
        account_id = flask.g.user_id
        user_secrets = Secret.query.filter_by(account_id=account_id).all()
        secrets = secrets_schema.dump(user_secrets)
        for secret in secrets:
            bytedata = secret["data"].encode('utf-8')
            decrypted_secret = Secret.decrypt_secret(bytedata)
            secret["data"] = decrypted_secret.decode('utf-8')
        return {'status': 'success', 'data': secrets}, status_codes.HTTP_200_OK

    @validate_authentication
    def post(self):
        request_data = request.get_json(force=True)
        if not request_data:
               return {'message': 'No input data provided'}, status_codes.HTTP_400_BAD_REQUEST
        account_id = flask.g.user_id
        try:
            if request_data["type"] not in SecretResource.SECRET_TYPE:
                return {'message': 'Secret type not correct, allowed values: ' + str(SecretResource.SECRET_TYPE)}, status_codes.HTTP_400_BAD_REQUEST
            if Secret.if_exists(request_data["name"], request_data["type"], account_id):
                return {"message": "Secret already exists, skipping..."}, status_codes.HTTP_400_BAD_REQUEST
            else:
                encrypted_secret = Secret.encrypt_secret(request_data["data"])
                secret = Secret(id=str(uuid.uuid4()),
                                name=request_data["name"],
                                description=request_data["description"],
                                type=request_data["type"],
                                data=encrypted_secret.decode('utf-8'),
                                account_id=account_id)
                db.session.add(secret)
                db.session.commit()
                request_result = secret_schema.dump(secret)
                return {"status": 'success', 'data': request_result}, status_codes.HTTP_201_CREATED
        except:
                return {'message': 'Something went wrong'}, status_codes.HTTP_500_INTERNAL_SERVER_ERROR

    @validate_authentication
    def put(self):
        request_data = request.get_json(force=True)
        if not request_data:
            return {'message': 'No input data provided'}, status_codes.HTTP_400_BAD_REQUEST
        account_id = flask.g.user_id
        try:
            if request_data["type"] not in SecretResource.SECRET_TYPE:
                return {'message': 'Secret type not correct, allowed values: ' + str(SecretResource.SECRET_TYPE)}, status_codes.HTTP_400_BAD_REQUEST

            secret = Secret.get_secret_by_id(request_data["id"], account_id)
            if not secret:
                return {"message": "Secret not found!"}, status_codes.HTTP_400_BAD_REQUEST
            else:
                if request_data["name"]:
                    secret.name = request_data["name"]
                if request_data["description"]:
                    secret.description = request_data["description"]
                if request_data["type"]:
                    secret.type = request_data["type"]
                if request_data["data"]:
                    encrypted_secret = Secret.encrypt_secret(request_data["data"])
                    secret.data = encrypted_secret.decode('utf-8')
                db.session.commit()
                request_result = secret_schema.dump(secret)
                return {"status": 'success', 'data': request_result}, status_codes.HTTP_200_OK
        except:
                return {'message': 'Something went wrong'}, status_codes.HTTP_500_INTERNAL_SERVER_ERROR
