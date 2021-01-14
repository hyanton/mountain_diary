from flask_restplus import Api
from flask import Blueprint

from .main.controller.ski_touring_controller import api as ski_touring_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Mountain diary API',
          version='1.0',
          description='API for manage mountain expeditions'
          )

api.add_namespace(ns=ski_touring_ns, path='/ski_touring')