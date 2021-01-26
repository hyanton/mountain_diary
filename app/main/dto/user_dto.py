from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address', example='example@example.com'),
        'username': fields.String(required=True, description='user username', example='example'),
        'password': fields.String(required=True, description='user password', example='example'),
        'public_id': fields.String(description='user Identifier', example=None)
    })