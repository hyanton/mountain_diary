from functools import wraps
from typing import Dict, Callable

from flask import request

from app.main.service.auth_helper import Auth


def token_required(f: Callable) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):
        response, status_code = Auth.get_logged_in_user(request)
        data = response.get('data')

        if not data:
            return response, status_code

        return f(*args, **kwargs)

    return decorated


def admin_token_required(f: Callable) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):

        response, status_code = Auth.get_logged_in_user(request)
        data = response.get('data')

        if not data:
            return data, status_code

        admin = data.get('admin')

        if not admin:
            response_object: Dict[str, str] = {
                'status': 'fail',
                'message': 'Admin token requied'
            }

            return response_object, 401

        return f(*args, **kwargs)

    return decorated
