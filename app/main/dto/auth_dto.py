from flask_restplus import Namespace, fields


class AuthDto:
    api = Namespace('auth', description='authentification relatied operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='email adress', example='example@example.com'),
        'password': fields.String(required=True, description='user password', example='example')
    })
