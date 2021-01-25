from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

# Create the SQLAlchemy db instance
db = SQLAlchemy()

# Initialize Marshmallow
# ma = Marshmallow()

flask_bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_name)

    db.init_app(app)
    # ma.init_app(app)
    flask_bcrypt.init_app(app)

    return app
