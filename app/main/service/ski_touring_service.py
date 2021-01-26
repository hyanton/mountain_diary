from typing import Dict, Tuple

from app.main import db
from ..model.ski_touring_model import SkiTouring
from sqlalchemy import desc


def save_changes(data: SkiTouring):
    """
    Save ski tour in database
    :param data: SkiTouring
    :return:
    """
    db.session.add(data)
    db.session.commit()


def save_new_ski_tour(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    new_ski_tour = SkiTouring(date=data.get('date'),
                              summit_name=data.get('summit_name'),
                              region=data.get('region'),
                              activity_type=data.get('activity_type'),
                              description=data.get('description'),
                              climb_time=data.get('climb_time'),
                              descent_time=data.get('descent_time'),
                              distance=data.get('distance'),
                              itinerary=data.get('itinerary'),
                              technical_information=data.get('technical_information'),
                              map=data.get('map'),
                              topo_link=data.get('topo_link')
                              )

    # print(new_ski_tour)
    save_changes(new_ski_tour)

    response_object: Dict[str, str] = {
        'status': 'success',
        'message': 'Ski tour for {} added in database.'.format(new_ski_tour.summit_name)
    }

    return response_object, 201


def get_all_ski_tours():
    return SkiTouring.query.order_by(desc(SkiTouring.date)).all()


def get_ski_tour(id: int):
    return SkiTouring.query.filter_by(id=id).first()

