import json

def test_welcome(api):
    """connects to root route"""
    app = api.get('/')
    assert app.status == '200 OK'
    assert app.get_data() ==  b"<h1>Twigelites Server!</h1>"
  
def test_register(api):
    user_data = json.dumps({'username': "tester", 'email': 'flo@gmail.com', 'password': 'test'})
    mock_headers = {'Content-Type': 'application/json'}
    app = api.post('/auth/register', data=user_data, headers=mock_headers)

def test_login(api):
    user_data = json.dumps({'username': "tester",'password': 'test'})
    mock_headers = {'Content-Type': 'application/json'}
    app = api.post('/auth/login', data=user_data, headers=mock_headers)

def test_get_all_twiglets(api):
    app = api.get('/twiglets')
    assert app.status == '200 OK'
    assert b'twiglet_id' in app.get_data()

def test_get_all_users(api):
    app = api.get('/auth/users')
    assert app.status == '200 OK'
    assert b'email' in app.get_data()

# def test_get_twiglet_id(api):
#     app = api.post('/twiglets/1')
#     assert app.status == '404'
#     assert b'twiglet_id' in app.get_data()


def test_401(api):
    app = api.post('/auth/login')
    user_data = json.dumps({'username': "tester", 'password': ''})
    mock_headers = {'Content-Type': 'application/json'}
    app = api.post('/auth/login', data=user_data, headers=mock_headers)

# def test_400(api):
#     app = api.post('/auth/login')
#     assert app.status == '400 BAD REQUEST'
