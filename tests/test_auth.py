def test_get_token_success(auth):
    token = auth.get_token()
    assert token is not None
    assert isinstance(token, str)
    assert len(token) > 0

def test_get_token_invalid_credit(auth):
    token = auth.get_token(username="wrong", password="wrong")
    assert token is None

def test_token_is_available_via_fixture(token):
    assert token is not None
    assert isinstance(token, str)