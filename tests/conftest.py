import pytest
from app import create_app
from app.models.planet import Planet
from app import db
from flask.signals import request_finished


@pytest.fixture
def app():
    # create the app with a test config dictionary
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    # close and remove the temporary database
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def two_saved_planets(app):
    # initialize 2 objects and put them into database
    # random test data
    # pass all attributes, except for id
    planet1 = Planet(name="Earth", description="Green", radius=333)
    planet2 = Planet(name="Mars", description="Red", radius=444)

    db.session.add_all([planet1, planet2])

    db.session.commit()
