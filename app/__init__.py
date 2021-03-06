from flask_restplus import Api
from flask import Blueprint

from .main.controller.ski_touring_controller import api as ski_touring_ns
from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.random_controller import api as random_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Mountain diary API',
          version='1.0',
          description='API for manage mountain expeditions'
          )

api.add_namespace(ns=ski_touring_ns, path='/ski_touring')
api.add_namespace(ns=user_ns, path='/user')
api.add_namespace(ns=auth_ns, path='/auth')
api.add_namespace(ns=random_ns, path='/random')
