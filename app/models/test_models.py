from app import create_app
from app.models.twiglet import Twiglet
from app.models.user import User

def test_new_user_with_fixture():
    """
    Given a User model
    When a new User is created
    Then check the username, email, password and reputation
    """
    user = User('flo', 'flo@flo.com', 'password', 'null')
    assert user.username == 'flo'
    assert user.email == 'flo@flo.com'
    assert user.password_hash == 'password'
    assert user.reputation == 'null'
    
# def test_new_user_with_fixture_again():
#     flask_app = create_app()



def test_new_twiglet_with_fixtures():
    """
    Given a Twiglet Model
    When a new Twiglet is created
    Then check longitude, latitude, shop_name, address, found_by_user
    """
    twiglet = Twiglet('45.555', '51.5155153', 'twiglet shop', 'ChIJ_1e1OtMEdkgRQBWTjNRRVJM', 'twiglet street', '1', '2022-08-29 16:36:00.829214', '2022-08-29 16:36:00.829216' )
    assert twiglet.longitude == '45.555'
    assert twiglet.latitude == '51.5155153'
    assert twiglet.shop_name == 'twiglet shop'
    assert twiglet.shop_id == 'ChIJ_1e1OtMEdkgRQBWTjNRRVJM'
    assert twiglet.address == 'twiglet street'
    assert twiglet.found_by_user == '1'
    assert twiglet.date_found == '2022-08-29 16:36:00.829214'
    assert twiglet.date_last_confirmed == '2022-08-29 16:36:00.829216'
