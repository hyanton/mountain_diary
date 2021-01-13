import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS'))

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)

from models.ski_touring import SkiTouring, SkiTouringSchema


@app.route('/')
def hello():
    return 'Hello World'


@app.route('/ski_touring')
def ski_touring():
    ski_tours = SkiTouring.query.all()
    ski_tour_schema = SkiTouringSchema(many=True)
    ski_tours = ski_tour_schema.dump(ski_tours)
    print(ski_tours)
    return ski_tours[0]


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
