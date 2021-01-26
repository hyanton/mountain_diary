import unittest

from flask import current_app
from flask_testing import TestCase

from manage import app


class TestDevelopmentConfing(TestCase):
    def create_app(self):
        config_name = 'app.main.config.DevelopmentConfig'
        app.config.from_object(config_name)
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)


class TestTestingConfig(TestCase):
    def create_app(self):
        config_name = 'app.main.config.TestingConfig'
        app.config.from_object(config_name)
        return app

    def test_app_is_testing(self):
        self.assertTrue(app.config['TESTING'])
        self.assertTrue(app.config['DEBUG'])

class TestProductionConfig(TestCase):
    def create_app(self):
        config_name = 'app.main.config.ProductionConfig'
        app.config.from_object(config_name)
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()
