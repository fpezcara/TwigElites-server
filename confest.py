from app import User, Twiglet
import init_db
import pytest

app = init_db()

@pytest.fixture
def api():
    client = app.test_client()
    return client

@pytest.fixture(scope='module')
def new_user():
    user = User('saamiya101', 'saamiya@gmail.com', 'password')
    return user


@pytest.fixture(scope='module')
def new_twiglet():
    twiglet = Twiglet('twiglet shop', 'twiglet stree', '1')
    return twiglet

