from app import db
from sqlalchemy.dialects.postgresql import JSON
from marshmallow_sqlalchemy import ModelSchema


class SkiTouring(db.Model):
    __tablename__ = 'SkiTouring'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    summit_name = db.Column(db.String, nullable=False)
    region = db.Column(db.String)
    type = db.Column(db.String)
    technical_information = db.Column(JSON)
    time = db.Column(db.Interval)
    distance = db.Column(db.Float)
    itinerary = db.Column(JSON)
    description = db.Column(db.Text)

    def __init__(self, date, summit_name, region, type, technical_information, time, distance, itinerary, description):
        self.date = date
        self.summit_name = summit_name
        self.region = region
        self.type = type
        self.technical_information = technical_information
        self.time = time
        self.distance = distance
        self.itinerary = itinerary
        self.description = description

    def __repr__(self):
        message = 'Ski tour to {} made on {} (id: {})'.format(self.summit_name, self.date, self.id)
        return message


class SkiTouringSchema(ModelSchema):
    class Meta:
        model = SkiTouring
        sqla_session = db.session
