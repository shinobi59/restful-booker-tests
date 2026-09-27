
def test_api_is_alive(api):
    response = api.get("/ping")
    assert response.status_code == 201, f"Ожидали 201, получили {response.status_code}"

def test_ping_returns_created_status(api):
    response = api.get("/ping")
    assert response.status_code == 201
    assert response.text == "Created"