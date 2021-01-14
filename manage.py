import os
import unittest

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from dotenv import load_dotenv

load_dotenv()

from app.main import create_app, db
from app import blueprint

app = create_app(config_name=os.environ.get('APP_SETTINGS'))
app.register_blueprint(blueprint)

app.app_context().push()

migrate = Migrate(app, db, compare_type=True)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# from app.main.model.ski_touring_model import SkiTouring


@manager.command
def run():
    app.run()


@manager.command
def test():
    """
    Run unit tests
    :return:
    """
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
