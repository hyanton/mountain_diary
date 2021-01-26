from typing import Tuple, Dict

from flask import request
from flask_restplus import Resource

from ..dto.ski_touring_dto import SkiTouringDto
from ..service.ski_touring_service import save_new_ski_tour, get_all_ski_tours, get_ski_tour
from ..util.decorator import admin_token_required

api = SkiTouringDto.api
_ski_tour = SkiTouringDto.ski_tour


@api.route('/')
class SkiTourList(Resource):
    @api.doc('list of registered ski tours.')
    @api.marshal_list_with(_ski_tour, envelope='data')
    def get(self):
        """
        List of all ski tours registered
        :return:
        """
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
            api.abort(404)
        else:
            return ski_tour
