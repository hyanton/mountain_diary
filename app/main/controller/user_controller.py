import json
import sys
from typing import Dict
import logging

from flask import request
from flask_restplus import Resource

from ..dto.user_dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_user
from ..util.decorator import admin_token_required
from ..util.logger import configure_logging, custom_log_message

api = UserDto.api
_user = UserDto.user

app_logger = configure_logging('User controller')


@api.route('/')
class UserList(Resource):
    @api.doc('list of regirstred users')
    @api.marshal_list_with(_user, envelope='data')
    @admin_token_required
    def get(self):
        """
        List of all regirstred users
        :return:
        """

        log_infos: Dict = {
            'level': logging.DEBUG,
            'msg': 'List of users requested.',
            'filename': __name__,
            'funcName': sys._getframe().f_code.co_name
        }
        custom_log_message(app_logger, log_infos)

        return get_all_users()

    @api.response(201, 'User successfully created')
    @api.doc('create new user')
    @api.expect(_user, validate=True)
    @admin_token_required
    def post(self):
        """
        Create and register new user
        :return:
        """

        log_infos: Dict = {
            'level': logging.DEBUG,
            'msg': 'Create new user request.',
            'filename': __name__,
            'funcName': sys._getframe().f_code.co_name
        }
        custom_log_message(app_logger, log_infos)

        data = request.json
        return save_new_user(data)


@api.route('/<public_id>')
@api.param('public_id', 'user identifier')
@api.response(404, 'User not found')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    @admin_token_required
    def get(self, public_id):
        """
        Get specific user represented by unique public_id
        :param public_id: str
        :return:
        """

        user = get_user(public_id)

        if not user:
            log_infos: Dict = {
                'level': logging.INFO,
                'msg': 'No user found with public_id provided',
                'filename': __name__,
                'funcName': sys._getframe().f_code.co_name,
                'data': json.dumps({'public_id': public_id})
            }
            custom_log_message(app_logger, log_infos)

            api.abort(404)
        else:

            log_infos: Dict = {
                'level': logging.DEBUG,
                'msg': 'User found.',
                'filename': __name__,
                'funcName': sys._getframe().f_code.co_name,
                'data': json.dumps({'public_id': public_id})
            }
            custom_log_message(app_logger, log_infos)

            return user
