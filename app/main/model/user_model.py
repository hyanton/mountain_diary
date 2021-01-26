import os
import uuid

from .. import db, flask_bcrypt
from ..model.blacklist_token_model import BlackListToken
from datetime import datetime, timedelta
import jwt
from typing import Union, Dict


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True, nullable=False)
    public_id = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    registred_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.public_id = str(uuid.uuid4()),
        self.password = password
        self.registred_on = datetime.now()

    def __repr__(self):
        return "User '{}'".format(self.username)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password) -> bool:
        """
        Check if password_hash matches the hash of password argument
        :param password:
        :return:
        """
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    @staticmethod
    def encode_auth_token(user_id: int) -> Union[str, Exception]:
        """
        Generates Auth ken
        :param user_id: int
        :return:
        """

        try:
            payload: Dict = {
                'exp': datetime.utcnow() + timedelta(days=30),
                'iat': datetime.utcnow(),
                'sub': user_id
            }

            key: str = os.environ.get('APP_SETTINGS')
            token: str = jwt.encode(payload=payload, key=key, algorithm='HS256')

            return token

        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token: str) -> Union[str, int]:
        """
        Decodes the auth token
        :param auth_token: str
        :return:
        """
        try:
            key: str = os.environ.get('APP_SETTINGS')
            payload: Dict = jwt.decode(jwt=auth_token, key=key, algorithms=['HS256'])
            is_blacklisted_token = BlackListToken.check_blacklist(auth_token)

            if is_blacklisted_token:
                return 'Token blacklisted.'
            else:
                return payload['sub']

        except jwt.ExpiredSignatureError:
            return 'Signature expired'

        except jwt.InvalidTokenError:
            return 'Invalid token'
