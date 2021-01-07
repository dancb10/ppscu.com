from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields
from datetime import datetime
import hashlib
from itsdangerous import TimedSerializer, SignatureExpired, BadSignature
from flask import current_app
import status_codes

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

db = SQLAlchemy()
ma = Marshmallow()


class Account(db.Model):
    __tablename__ = 'accounts'

    id              = db.Column(db.String(255), primary_key=True, autoincrement=False, unique=True)
    username        = db.Column(db.String(80),  nullable=False, unique=False)
    password        = db.Column(db.String(255), nullable=False)
    email           = db.Column(db.String(80),  nullable=False, unique=True)
    date_created    = db.Column(db.DateTime,    nullable=False, default=datetime.utcnow())
    active          = db.Column('is_active', db.Boolean(), nullable=False, default=False)

    #class constructor
    def __init__(self, username, password, email, id):
        self.username = username
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.email = email
        self.date_created = datetime.utcnow().strftime('%Y/%m/%d %H:%M:%S')
        self.id = id

    #object representation
    def __repr__(self):
        return '<id {0}>'.format(self.id)

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
    #verifica daca exista un acount cu emailulala si intoarce email
    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def get_id(cls, email):
        existing_account = cls.query.filter_by(email=email).first()
        return existing_account.id

    @classmethod
    def get_accopunt_by_id(cls, id):
        existing_account = cls.query.filter_by(id=id).first()
        return existing_account

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
            return {'message': 'Token expired'}, status_codes.HTTP_400_BAD_REQUEST
        except BadSignature:
            return {'message': 'Token not valid'}, status_codes.HTTP_400_BAD_REQUEST
        id = Account.get_id(decoded_token['email'])
        return id


class AccountSchema(ma.Schema):
    id           = fields.String(dump_only=True)
    username     = fields.String(required=True)
    email        = fields.String(required=True)
    date_created = fields.DateTime()


class Secret(db.Model):
    __tablename__ = 'secrets'

    id          = db.Column(db.String(255), primary_key=True, autoincrement=False, unique=True)
    name        = db.Column(db.String(80), unique=False)
    description = db.Column(db.String(255))
    type        = db.Column(db.String(255))
    data        = db.Column(db.String(255))
    account_id  = db.Column(db.String(255))

    def __init__(self, id, name, description, type, data, account_id):
        self.id             = id
        self.name           = name
        self.description    = description
        self.type           = type
        self.data           = data
        self.account_id     = account_id

    @classmethod
    def if_exists(cls, name: str, type: str, account_id: str):
        existing_secrets = cls.query.filter_by(account_id=account_id).all()
        if existing_secrets is None:
            return False
        else:
            for secret in existing_secrets:
                if secret.name == name and secret.type == type:
                    return True
            return False

    @classmethod
    def get_secret_by_id(cls, id: str, account_id: str):
        existing_secrets = cls.query.filter_by(account_id=account_id).all()
        if existing_secrets:
            for secret in existing_secrets:
                if secret.id == id:
                    return secret
        else:
            return None

    @classmethod
    def get_secrets(cls, account_id):
        existing_secrets = cls.query.filter_by(account_id=account_id).all()
        return existing_secrets

    @staticmethod
    def encrypt_secret(clear_text):
        secret_key = current_app.config['ENCRYPTION_KEY']
        encoded_key = b64decode(secret_key)
        iv = get_random_bytes(16)
        cipher = AES.new(encoded_key, AES.MODE_CBC, iv)
        padded_secret = pad(clear_text.encode(), 16)
        encrypted_secret = cipher.encrypt(padded_secret)
        return b64encode(iv + encrypted_secret)

    @staticmethod
    def decrypt_secret(encrypted_text):
        secret_key = current_app.config['ENCRYPTION_KEY']
        encrypted_secret = b64decode(encrypted_text)
        iv = encrypted_secret[:16]
        encoded_key = b64decode(secret_key)
        cipher = AES.new(encoded_key, AES.MODE_CBC, iv)
        decrypted_secret = cipher.decrypt(encrypted_secret[16:])
        return unpad(decrypted_secret, 16)


class SecretSchema(ma.Schema):
    name        = fields.String(required=True)
    description = fields.String(required=True)
    type        = fields.String(required=True)
    data        = fields.String(required=True)
    account_id  = fields.String(required=False)
    id          = fields.String(required=True)
