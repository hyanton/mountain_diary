import logging
import os
import socket
from logging.handlers import TimedRotatingFileHandler
from typing import Dict


def custom_log_message_extra(log_infos):
    """
    Add extra argument to log messages
    :param log_infos: Dict contains informations such filename, funcName and data
    :return: json
    """
    filename: str = log_infos.get('filename')
    funcName: str = log_infos.get('funcName')
    data: str = log_infos.get('data')

    extra_json: Dict[str, str] = {'environment': os.getenv('FLASK_ENV'), 'hostname': socket.gethostname(),
                                  'custom_filename': filename, 'custom_funcName': funcName, 'data': data}

    return extra_json


def custom_log_message(app_logger, log_infos: Dict):

    level: str = log_infos.get('level')
    msg: str = log_infos.get('msg')

    if level == logging.DEBUG:
        app_logger.debug(msg=msg, extra=custom_log_message_extra(log_infos=log_infos))
    elif level == logging.INFO:
        app_logger.info(msg=msg, extra=custom_log_message_extra(log_infos=log_infos))
    elif level == logging.WARNING:
        app_logger.warning(msg=msg, extra=custom_log_message_extra(log_infos=log_infos))
    elif level == logging.ERROR:
        app_logger.error(msg=msg, extra=custom_log_message_extra(log_infos=log_infos))
    elif level == logging.CRITICAL:
        app_logger.critical(msg=msg, extra=custom_log_message_extra(log_infos=log_infos))
    else:
        # DEBUG level by default
        app_logger.debug(msg=msg, extra=custom_log_message_extra(log_infos=log_infos))


def configure_logging(name: str = __name__):
    app_logger = logging.getLogger(name)
    app_logger.setLevel(logging.DEBUG)

    # debug handler
    debug_handler = TimedRotatingFileHandler(filename=os.environ.get('LOGGING_FILENAME'), when='D')
    debug_handler.setLevel(logging.DEBUG)

    # formatter
    custom_formatter = logging.Formatter(
        '{"timestamp": "%(asctime)s", "hostname": "%(hostname)s", "environment": "%(environment)s", '
        '"name": "%(name)s", "filename": "%(custom_filename)s", "function name": "%(custom_funcName)s", '
        '"level": "%(levelname)s", "message": "%(message)s", "data": "%(data)s"}')
    debug_handler.setFormatter(custom_formatter)

    app_logger.addHandler(debug_handler)

    return app_logger

# app_logger = configure_logging()
