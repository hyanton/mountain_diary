from app.main import db
from datetime import datetime


class BlackListToken(db.Model):
    """
    Token model for storing JWT tokens
    """
    __tablename__ = 'blacklist_tokens'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String, unique=True, nullable=False)
    blacklisted_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, token):
        self.token = token
        self.blacklisted_on = datetime.now()

    def __repr__(self):
        return 'toekn id: {}'.format(self.token)

    @staticmethod
    def check_blacklist(auth_token):
        """
        Check if token has been blacklisted
        :param auth_token:
        :return:
        """
        res = BlackListToken.query.filter_by(token=str(auth_token)).first()

        if res:
            return True
        else:
            return False
