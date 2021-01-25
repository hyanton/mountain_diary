# dto = data transfer object
from app.main.util.enums import ActivityType
from flask_restplus import Namespace, fields
from datetime import date, time
from .custom_fields import TimeDeltaFormat, JsonFormat


class SkiTouringDto:
    api = Namespace('ski_touring', description='ski touring related operations')

    technical_information = api.model('technical information', {
        'starting_altitude': fields.Float(attribute='starting_altitude', allow_null=True,
                                          description='starting altitude in [m]',
                                          example=1001.01),
        'summit_elevation': fields.Float(attribute='summit_elevation', allow_null=True,
                                         description='summit elevation in [m]',
                                         example=2567),
        'positive_elevation': fields.Float(attribute='positive_elevation', allow_null=True,
                                           description='positive elevation in [m]',
                                           example=1500),
        'negative_elevation': fields.Float(attribute='negative_elevation', allow_null=True,
                                           description='negative elevation in [m]',
                                           example=1666),
        'technical_difficulty': fields.String(attribute='technical_difficulty', allow_null=True,
                                              description='technical difficulty',
                                              example='no technical difficulty'),
        'physical_difficulty': fields.String(attribute='physical_difficulty', allow_null=True,
                                             description='physical difficulty',
                                             example='long effort'),
    })

    # access = api.model('access', {
    #     'road_access': fields.String(description='access of the starting point description.',
    #                                  example='Accès par la route depuis Orsières.')
    # })

    itinerary = api.model('itinerary', {
        'access': fields.String(description='access of the starting point description.',
                                example='Accès par la route depuis Orsières.'),
        'climb': fields.String(description='Climbing to the summit description.', example='Fllow the tracks.'),
        'descent': fields.String(description='Descent description', example='Take the same itinerary.')
    })

    ski_tour = api.model('ski_touring', {
        'id': fields.Integer(description='id of the ski tour'),
        'date': fields.Date(required=True, description='date of the ski tour.',
                            example=date(year=2020, month=1, day=26).strftime('%Y-%m-%d')),
        'summit_name': fields.String(required=True, description='name of the summit.', example='Les Monts Telliers'),
        'region': fields.String(required=False, description='name of the region.', example='Pays du Saint-Bernard'),
        'activity_type': fields.String(required=False,  # enum=[el.value for el in ActivityType],
                                       description='excursion type.', example=ActivityType.ski_touring.value),
        'description': fields.String(desciption='description of the excursion',
                                     example='La vue est splendide au sommet. Une cabane se trouve quelques mètres au-dessus du parking, on y mange très bien.'),
        'climb_time': TimeDeltaFormat(description='climbing duration.', example=time(hour=4).strftime('%H:%M:%S')),
        'descent_time': TimeDeltaFormat(description='descent duration.',
                                        example=time(hour=1, minute=30).strftime('%H:%M:%S')),
        'distance': fields.Float(description='distance of the excursion in [km]', example=9.8),
        'itinerary': JsonFormat(allow_null=True, skip_none=True,
                                description='Information concerning the acces, the climb and the descent.',
                                example={
                                    'access': 'Depuis Martigny, par la route du Col du Grand St Bernard.',
                                    'climb': 'Débuter la montée depuis le parking. Les derniers mètres au sommet se font à pied.',
                                    'descent': 'Redescendre par le même itinéraire.'
                                }),
        'technical_information': JsonFormat(allow_null=True, skip_none=True,
                                            description='dictionnary containing on the ski tour',
                                            example={"starting altitude": 1299, "summit elevation": 2103,
                                                     "positive elevation": 800, "negative elevation": 800,
                                                     "orientation": {"climb": "Nord", "descent": "Nord"},
                                                     "material": "crampons"}),
        'map': fields.String(description='useful maps(s) for the tour.'),
        'topo_link': fields.String(description='Url link to a guide for the excursion.',
                                   example='https://www.camptocamp.org/routes/45321/fr/monts-telliers-par-la-combe-de-drone-voie-normale-')
    })
