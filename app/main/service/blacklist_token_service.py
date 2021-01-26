from .. import db
from ..model.blacklist_token_model import BlackListToken
from typing import Dict, Tuple


def save_token(token: str) -> Tuple[Dict[str, str], int]:
    """
    Save token in database (mark it as blacklisted)
    :param token: str
    :return:
    """
    blacklist_token = BlackListToken(token)

    try:
        db.session.add(blacklist_token)
        db.session.commit()

        response_object: Dict[str, str] = {
            'status': 'success',
            'message': 'Successfully logged out'
        }

        return response_object, 200

    except Exception as e:
        response_object: Dict[str, str] = {
            'status': 'failed',
            'message': e
        }

        return response_object, 500
