import requests


def test_api_is_alive():
    response = requests.get("https://restful-booker.herokuapp.com/ping")
    assert response.status_code == 201, f"Ожидали 201, получили {response.status_code}"