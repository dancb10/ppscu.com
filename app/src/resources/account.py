from flask_restful import Resource
from flask import request
from models.models import db, Account, AccountSchema
import uuid
accounts_schema = AccountSchema(many=True)
account_schema = AccountSchema()


class AccountResource(Resource):

    def post(self):
        request_data = request.get_json(force=True)
        if not request_data:
            return {'message': 'No input data provided'}, 400
        account = Account(username=request_data["username"],
                          password=request_data["password"],
                          email=request_data["email"],
                          user_id=str(uuid.uuid4()))

        try:
            if not account.if_exists(email=request_data["email"]):

                db.session.add(account)
                db.session.commit()
            else:
                return {'message': 'Account already exists'}, 400

            request_result = account_schema.dump(account)

            return {
                       "status": 'success',
                       'message': 'Account {} was created'.format(request_data['email']),
                       'data': request_result
                   }, 201
        except:
            return {'message': 'Something went wrong'}, 500
