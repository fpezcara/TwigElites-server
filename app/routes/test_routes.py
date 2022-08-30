import json

def test_welcome(api):
    """connects to root route"""
    app = api.get('/')
    assert app.status == '200 OK'
    assert app.get_data() ==  b"<h1>Twigelites Server!</h1>"
