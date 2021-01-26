import sys
import json
from typing import Tuple, Dict
import logging

from flask import request
from flask_restplus import Resource

from ..dto.ski_touring_dto import SkiTouringDto
from ..service.ski_touring_service import save_new_ski_tour, get_all_ski_tours, get_ski_tour
from ..util.decorator import admin_token_required
from ..util.logger import custom_log_message
from ..util.logger import configure_logging

api = SkiTouringDto.api
_ski_tour = SkiTouringDto.ski_tour

app_logger = configure_logging('SkiTouring controller')


@api.route('/')
class SkiTourList(Resource):
    @api.doc('list of registered ski tours.')
    @api.marshal_list_with(_ski_tour, envelope='data')
    def get(self):
        """
        List of all ski tours registered
        :return:
        """
        log_infos: Dict = {
            'level': logging.DEBUG,
            'msg': 'List of ski tours requested.',
            'filename': __name__,
            'funcName': sys._getframe().f_code.co_name
        }
        custom_log_message(app_logger, log_infos)

        return get_all_ski_tours()

    @api.response(201, 'Ski tour successfully added.')
    @api.doc('Add new ski tour')
    @api.expect(_ski_tour, validate=True)
    @admin_token_required
    def post(self) -> Tuple[Dict[str, str], int]:
        """
        Register new ski tour in database
        :return:
        """

        log_infos: Dict = {
            'level': logging.DEBUG,
            'msg': 'Create new ski tour request.',
            'filename': __name__,
            'funcName': sys._getframe().f_code.co_name
        }
        custom_log_message(app_logger, log_infos)

        data = request.json
        # print(data)
        return save_new_ski_tour(data=data)


@api.route('/<id>')
@api.param('id', 'The ski tour id (primary key)')
@api.response(404, 'Ski tour not found')
class SkiTour(Resource):
    @api.doc('get a ski tour')
    @api.marshal_with(_ski_tour)
    def get(self, id):
        """
        get ski tour given its primary key
        :param id: int
        :return:
        """
        ski_tour = get_ski_tour(id=id)

        if not ski_tour:
            log_infos: Dict = {
                'level': logging.INFO,
                'msg': 'No ski tour found with id provided',
                'filename': __name__,
                'funcName': sys._getframe().f_code.co_name,
                'data': json.dumps({'id': id})
            }
            custom_log_message(app_logger, log_infos)

            api.abort(404)

        else:

            log_infos: Dict = {
                'level': logging.DEBUG,
                'msg': 'Ski tour found.',
                'filename': __name__,
                'funcName': sys._getframe().f_code.co_name,
                'data': json.dumps({'id': id})
            }
            custom_log_message(app_logger, log_infos)

            return ski_tour
