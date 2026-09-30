import allure

@allure.feature("Auth")
@allure.title("Получение токена")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_token_success(auth):
    token = auth.get_token()
    assert token is not None
    assert isinstance(token, str)
    assert len(token) > 0

@allure.feature("Auth")
@allure.title("Получение токена неверного пользователя")
@allure.severity(allure.severity_level.NORMAL)
def test_get_token_invalid_credit(auth):
    token = auth.get_token(username="wrong", password="wrong")
    assert token is None

@allure.feature("Auth")
@allure.title("Проверка доступности токена через фикстуру")
@allure.severity(allure.severity_level.MINOR)
def test_token_is_available_via_fixture(token):
    assert token is not None
    assert isinstance(token, str)