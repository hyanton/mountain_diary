import uuid
from datetime import datetime

from app.main import db
from ..model.user_model import User
from typing import Dict, Tuple


def save_changes(data: User) -> None:
    db.session.add(data)
    db.session.commit()


def generate_token(user: User) -> Tuple[Dict[str, str], int]:
    """
    Generate new token
    :param user: User
    :return:
    """

    try:
        # generate auth token
        auth_token = User.encode_auth_token(user.id)

        response_object: Dict[str, str] = {
            'status': 'success',
            'message': 'registred succesfully',
            'Authorization': auth_token
        }

        return response_object, 201

    except Exception as e:
        response_object: Dict[str, str] = {
            'status': 'failed',
            'message': 'An error occured, please try again.'
        }

        return response_object, 401


def save_new_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    user = User.query.filter_by(email=data['email']).first()

    if not user:
        new_user = User(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )

        save_changes(new_user)

        return generate_token(new_user)

    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists.'
        }

        return response_object, 409


def get_all_users():
    return User.query.all()


def get_user(public_id: str):
    return User.query.filter_by(public_id=public_id).first()
