from app.main import db
from app.main.model.ski_touring_model import SkiTouring


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def save_new_ski_tour(data):
    new_ski_tour = SkiTouring(date=data['date'],
                              summit_name=data['summit_name'],
                              region=data['region'],
                              type=data['type'],
                              technical_information=data['technical_information'],
                              time=data['time'],
                              distance=data['distance'],
                              itinerary=data['itinerary'],
                              description=data['description'])

    save_changes(new_ski_tour)


def get_all_ski_tours():
    return SkiTouring.query.all()


def get_ski_tour(id):
    return SkiTouring.query.filter_by(id=id).first()

