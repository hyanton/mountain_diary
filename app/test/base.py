from flask_testing import TestCase
from app.main import db
from manage import app


class BaseTestCase(TestCase):
    """
    Base tests
    """

    def create_app(self):
        config_name: str = 'app.main.config.TestingConfig'
        app.config.from_object(config_name)
        return app

    def setUp(self) -> None:
        db.create_all()
        db.session.commit()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
