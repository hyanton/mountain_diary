import json
import sys
from typing import Dict
import logging

from flask import request
from flask_restplus import Resource

from ..service.auth_helper import Auth
from ..dto.auth_dto import AuthDto
from ..util.logger import configure_logging, custom_log_message

api = AuthDto.api
_user_auth = AuthDto.user_auth

app_logger = configure_logging('Auth controller')


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

        log_infos: Dict = {
            'level': logging.DEBUG,
            'msg': 'Login request.',
            'filename': __name__,
            'funcName': sys._getframe().f_code.co_name
        }
        custom_log_message(app_logger, log_infos)

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

        log_infos: Dict = {
            'level': logging.DEBUG,
            'msg': 'Logout request.',
            'filename': __name__,
            'funcName': sys._getframe().f_code.co_name
        }
        custom_log_message(app_logger, log_infos)

        auth_header = request.headers.get('Authorization')

        return Auth.logout_user(auth_header)
