from app.main import db
from app.main.model.ski_touring_model import SkiTouring
from sqlalchemy import desc


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def save_new_ski_tour(data):
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

    print(new_ski_tour)
    save_changes(new_ski_tour)


def get_all_ski_tours():
    return SkiTouring.query.order_by(desc(SkiTouring.date)).all()


def get_ski_tour(id):
    return SkiTouring.query.filter_by(id=id).first()

