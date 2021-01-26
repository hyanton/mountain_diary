from flask import request
from flask_restplus import Resource

from ..service.auth_helper import Auth
from ..dto.auth_dto import AuthDto

api = AuthDto.api
_user_auth = AuthDto.user_auth


@api.route('/login')
class UserLogin(Resource):
    """
    User login resource
    """

    @api.doc('user login')
    @api.expect(_user_auth, validate=True)
    def post(self):
        """
        Login
        :return:
        """

        data = request.json
        return Auth.login_user(data)


@api.route('/logout')
class LogoutApi(Resource):
    """
    Logout resource
    """

    @api.doc('user logout')
    def post(self):
        """
        Get auth token to mark it as blacklisted and logout.
        :return:
        """

        auth_header = request.headers.get('Authorization')

        return Auth.logout_user(auth_header)
