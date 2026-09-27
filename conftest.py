import pytest
from api.client import ApiClient


BASE_URL = "https://restful-booker.herokuapp.com"


@pytest.fixture
def api():
    client = ApiClient(base_url=BASE_URL)
    yield client
    client.close()