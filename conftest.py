import pytest
from api.client import ApiClient
from api.auth import AuthApi

BASE_URL = "https://restful-booker.herokuapp.com"


@pytest.fixture(scope="session")
def api():
    client = ApiClient(base_url=BASE_URL)
    yield client
    client.close()

@pytest.fixture(scope="session")
def auth(api):
    return AuthApi(api)

@pytest.fixture(scope="session")
def token(auth):
    return auth.get_token()

@pytest.fixture(scope="session")
def auth_headers(auth, token):
    return auth.get_headers(token)