import hashlib
from datetime import datetime

from flask import current_app
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import TimedSerializer, SignatureExpired, BadSignature
from marshmallow import fields

db = SQLAlchemy()
ma = Marshmallow()


class Account(db.Model):
    __tablename__ = 'accounts'

    user_id = db.Column(db.String(255), primary_key=True, autoincrement=False, unique=True)
    username = db.Column(db.String(80),  nullable=False, unique=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(80),  nullable=False, unique=True)
    date_created = db.Column(db.DateTime,    nullable=False, default=datetime.utcnow())
    active = db.Column('is_active', db.Boolean(), nullable=False, default=False)

    def __init__(self, username, password, email, user_id):
        self.username = username
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.email = email
        self.date_created = datetime.utcnow().strftime('%Y/%m/%d %H:%M:%S')
        self.user_id = user_id

    def __repr__(self):
        return '<user_id {0}>'.format(self.user_id)

    @classmethod
    def if_exists(cls, email):
        existing_account = cls.query.filter_by(email=email).first()
        if existing_account is None:
            return False
        else:
            if existing_account.email == email:
                return True
            else:
                return False

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def get_all_accounts(cls):
        return cls.query.all()

    @classmethod
    def get_id(cls, email):
        existing_account = cls.query.filter_by(email=email).first()
        return existing_account.user_id

    @staticmethod
    def generate_token(email):
        secret_key = current_app.config['TOKEN_SECRET_KEY']
        serializer = TimedSerializer(secret_key)
        token = serializer.dumps({'email': email})
        return token

    @staticmethod
    def verify_token(token):
        serializer = TimedSerializer(current_app.config['TOKEN_SECRET_KEY'])
        max_age = current_app.config['TOKEN_MAX_AGE']
        try:
            decoded_token = serializer.loads(token, max_age)
        except SignatureExpired:
            return {'message': 'Token expired'}, 400
        except BadSignature:
            return {'message': 'Token not valid'}, 400
        if Account.get_id(decoded_token['email']):
            return True
        return False


class AccountSchema(ma.Schema):
    user_id = fields.String(dump_only=True)
    username = fields.String(required=True)
    email = fields.String(required=True)
    date_created = fields.DateTime()
