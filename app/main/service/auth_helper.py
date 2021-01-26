from typing import Dict, Union, Tuple

from app.main.model.user_model import User
from app.main.service.blacklist_token_service import save_token


class Auth:

    @staticmethod
    def login_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        try:
            # fetch user data
            user: User = User.query.filter_by(email=data.get('email')).first()

            if user and user.check_password(data.get('password')):
                auth_token: str = User.encode_auth_token(user.id)

                if auth_token:
                    response_object: Dict[str, str] = {
                        'status': 'success',
                        'message': 'Successfully logged in',
                        'Authorization': auth_token
                    }

                    return response_object, 200

            else:
                response_object: Dict[str, str] = {
                    'status': 'failed',
                    'message': 'email or password does not match'
                }

                return response_object, 401

        except Exception as e:
            response_object: Dict[str, str] = {
                'status': 'failed',
                'message': 'try again'
            }

            return response_object, 500

    @staticmethod
    def logout_user(data: str) -> Tuple[Dict[str, str], int]:
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''

        if auth_token:
            resp: str = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # Mark token as blacklisted
                return save_token(auth_token)

            else:
                response_object: Dict[str, str] = {
                    'status': 'fail',
                    'message': resp
                }

                return response_object, 401

        else:
            response_object: Dict[str, str] = {
                'status': 'failed',
                'message': 'Provide valid token'
            }

            return response_object, 403

    @staticmethod
    def get_logged_in_user(new_request) -> Tuple[Dict[str, str], int]:
        # get auth token
        auth_token = new_request.headers.get('Authorization')

        if auth_token:
            response = User.decode_auth_token(auth_token)

            if not isinstance(response, str):
                user = User.query.filter_by(id=response).first()

                response_object: Dict[str, str] = {
                    'status': 'success',
                    'data': {
                        'user_id': user.id,
                        'email': user.email,
                        'admin': user.admin,
                        'registered_on': str(user.registred_on)
                    }
                }

                return response_object, 401

            else:
                response_object: Dict[str, str] = {
                    'status': 'fail',
                    'message': response
                }

                return response_object, 401

        else:
            response_object: Dict[str, str] = {
                'status': 'fail',
                'message': 'Provide valid token'
            }

            return response_object, 401
