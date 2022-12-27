import pytest
from application import create_app
from injector import Binder

from application import db

@pytest.fixture(scope='session')
def test_settings():
    return {
        'SQLALCHEMY_DATABASE_URI': 'sqlite://',
        'SECRET_KEY': 'TOP_SECRET'
    }

@pytest.fixture(scope='function')
def app(test_settings):
    
    def configure(binder: Binder): 
        ... # put mocked-stuff that can't normally be tested in here

    app = create_app(test_settings, injector_module=configure)

    yield app

@pytest.fixture(scope='function')
def client(app):
    return app.test_client()
