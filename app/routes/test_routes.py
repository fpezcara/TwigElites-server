import json
from urllib import response

# Test for route in main.py
def test_welcome(api):
    """connects to root route"""
    app = api.get('/')
    assert app.status == '200 OK'
    assert app.get_data() ==  b"<h1>Twigelites Server!</h1>"
  
# Test for routes in auth.py
def test_register(api):
    user_data = json.dumps({'username': "tester", 'email': 'flo@gmail.com', 'password': 'test'})
    mock_headers = {'Content-Type': 'application/json'}
    app = api.post('/auth/register', data=user_data, headers=mock_headers)

def test_login(api):
    user_data = json.dumps({'username': "tester",'password': 'test'})
    mock_headers = {'Content-Type': 'application/json'}
    app = api.post('/auth/login', data=user_data, headers=mock_headers)

def test_get_all_users(api):
    app = api.get('/auth/users')
    assert app.status == '200 OK'
    assert b'email' in app.get_data()

# Tests for routes in twiglet.py
def test_get_all_twiglets(api):
    app = api.get('/twiglets')
    assert app.status == '200 OK'
    assert b'twiglet_id' in app.get_data()


def test_get_twiglet_id(api):
    app = api.get('/twiglets/1/')
    assert app.status == '201 CREATED'
    assert b'Twiglet not found!' in app.get_data()

# Test for error handlers
def test_401(api):
    app = api.post('/auth/login')
    user_data = json.dumps({'username': "tester", 'password': ''})
    mock_headers = {'Content-Type': 'application/json'}
    app = api.post('/auth/login', data=user_data, headers=mock_headers)

