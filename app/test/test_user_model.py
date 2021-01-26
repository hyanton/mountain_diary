import unittest
from datetime import datetime, timedelta

from app.main import db
from app.main.model.user_model import User
from app.test.base import BaseTestCase


class TestUserModel(BaseTestCase):
    def test_encode_auth_token(self):
        user = User(email='test@test.com', username='test', password='test')
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, str))

    def test_decode_auth_token(self):
        user = User(email='test@test.com', username='test', password='test')
        db.session.add(user)
        db.session.commit()
        auth_token: str = user.encode_auth_token(user.id)
        self.assertTrue(User.decode_auth_token(auth_token) == 1)


if __name__ == '__main__':
    unittest.main()
