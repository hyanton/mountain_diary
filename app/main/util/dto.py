# dto = data transfer object

from flask_restplus import Namespace, fields
from datetime import date, time


class TimeDeltaFormat(fields.Raw):
    def format(self, value):
        return str(value)


class SkiTouringDto:
    api = Namespace('ski_touring', description='ski touring related operations')

    technical_information = api.model('technical information', {
        'starting_altitude': fields.Float(description='starting altitude in [m]', example=1001.01),
        'summit_elevation': fields.Float(description='summit elevation in [m]', example=2567),
        'positive_elevation': fields.Float(description='positive elevation in [m]', example=1500),
        'negative_elevation': fields.Float(description='negative elevation in [m]', example=1666),
        'technical_difficulty': fields.String(description='technical difficulty', example='no technical difficulty'),
        'physical_difficulty': fields.String(description='physical difficulty', example='long effort'),
    })

    itinerary = api.model('itinerary', {
        'access': fields.String(description='access of the starting point description.',
                                example='Accès par la route depuis Orsières.'),
        'climb': fields.String(description='Climbing to the summit description.', example='Fllow the tracks.'),
        'descent': fields.String(description='Descent description', example='Take the same itinerary.')
    })

    ski_tour = api.model('ski_touring', {
        'date': fields.DateTime(description='date of the ski tour.',
                                example=date(year=2020, month=1, day=26).strftime(format='%Y-%m%d')),
        'summit_name': fields.String(required=False, description='name of the summit.', example='Les Monts Telliers'),
        'region': fields.String(required=False, description='name of the region.', example='Pays du Saint-Bernard'),
        'type': fields.String(required=False, description='excursion type.', example='ski touring'),
        'technical_information': fields.Nested(technical_information, description='dictionnary containing information '
                                                                                  'such as starting altitude, '
                                                                                  'summit elevation, positive elevation, '
                                                                                  'negative elevation, '
                                                                                  'technical difficulty, '
                                                                                  'physical difficulty.'),
        'time': TimeDeltaFormat(description='excursion duration.', example=time(hour=4).strftime(format='%H:%S')),
        'distance': fields.Float(description='distance of the excursion in [km]', example=9.8),
        'itinerary': fields.Nested(itinerary,
                                   description='Information concerning the acces, the climb and the descent.'),
        'description': fields.String(desciption='description of the excursion',
                                     example='La vue est splendide au sommet. Une cabane se trouve quelques mètres au-dessus du parking, on y mange très bien.')
    })
