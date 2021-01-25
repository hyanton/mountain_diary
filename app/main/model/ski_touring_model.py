from app.main import db
from sqlalchemy.dialects.postgresql import JSONB
from app.main.util.enums import ActivityType


class SkiTouring(db.Model):
    __tablename__ = 'SkiTouring'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    summit_name = db.Column(db.String, nullable=False)
    region = db.Column(db.String)
    activity_type = db.Column(name='activity_type',
                              type_=db.Enum(ActivityType, name='activity_type', validate_strings=True,
                                            values_callable=lambda x: [el.value for el in x]))
    description = db.Column(db.Text)
    climb_time = db.Column(db.Interval)
    descent_time = db.Column(db.Interval)
    distance = db.Column(db.Float)
    itinerary = db.Column(JSONB)
    technical_information = db.Column(JSONB)
    map = db.Column(db.String)
    topo_link = db.Column(db.String)

    def __init__(self, date, summit_name, region, activity_type, description, climb_time, descent_time, distance,
                 itinerary, technical_information, map, topo_link):
        self.date = date
        self.summit_name = summit_name
        self.region = region
        self.activity_type = activity_type
        self.description = description
        self.climb_time = climb_time
        self.descent_time = descent_time
        self.distance = distance
        self.itinerary = itinerary
        self.technical_information = technical_information
        self.map = map
        self.topo_link = topo_link

    def __repr__(self):
        message = 'Ski tour to {} (id: {})'.format(self.summit_name, self.id)
        return message
