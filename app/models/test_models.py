from app.models import User, Twiglet

def test_new_user_with_fixture():
    """
    Given a User model
    When a new User is created
    Then check the username, email, password and reputation
    """
    user = User('saamiya101', 'saamiya101@gmail.com', 'password', 'Null')
    assert user.username == 'saamiya101'
    assert user.email == 'saamiya101@gmail.com'
    assert user.password == 'password'
    assert user.reputation == 'Null'


def test_new_twiglet_with_fixtures():
    """
    Given a Twiglet Model
    When a new Twiglet is created
    Then check longitude, latitude, shop_name, address, found_by_user
    """
    twiglet = Twiglet('45.555', '54.555', 'twiglet shop', 'twiglet street', '1')
    assert twiglet.longitude == '45.555'
    assert twiglet.latitude == '55.555'
    assert twiglet.shop_name == 'twiglet shop'
    assert twiglet.address == 'twiglet street'
    assert twiglet.found_by_user == '1'
