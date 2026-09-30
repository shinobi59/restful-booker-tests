import allure

@allure.feature("Booking")
@allure.title("Получение id бронирования")
@allure.severity(allure.severity_level.NORMAL)
def test_get_booking_id(booking):
    ids = booking.get_booking_ids()
    assert len(ids) > 0
    assert isinstance(ids, list)

@allure.feature("Booking")
@allure.title("Поиск бронирования по id")
@allure.severity(allure.severity_level.NORMAL)
def test_booking_by_id(booking):
    ids = booking.get_booking_ids()
    first_id = ids[0]["bookingid"]
    data = booking.get_booking(first_id)
    assert "firstname" in data
    assert "lastname" in data
    assert "bookingdates" in data

@allure.feature("Booking")
@allure.title("Получение неизвестного id бронирования")
@allure.severity(allure.severity_level.NORMAL)
def test_get_unknown_booking(booking):
    response = booking.get_booking_response(9999999)
    assert response.status_code == 404

@allure.feature("Booking")
@allure.title("Создание бронирования")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_booking(booking, booking_data):
    created = booking.create_booking(booking_data)
    assert "bookingid" in created
    assert isinstance(created["bookingid"], int)
    assert created["booking"]["firstname"] == "John"
    assert created["booking"]["lastname"] == "Doe"

@allure.feature("Booking")
@allure.title("Полный CRUD-цикл бронирования")
@allure.severity(allure.severity_level.CRITICAL)
def test_full_crud_cycle(booking, booking_data, token):
    with allure.step("Создать бронирование"):
        created = booking.create_booking(booking_data)
        booking_id = created["bookingid"]

    with allure.step("Получить созданное бронирование"):
        fetched = booking.get_booking(booking_id)
        assert fetched["firstname"] == "John"

    with allure.step("Обновить firstname на Jane"):
        booking.update_booking(booking_id, {**booking_data, "firstname": "Jane"}, token)

    with allure.step("Проверить, что firstname изменился"):
        refetched = booking.get_booking(booking_id)
        assert refetched["firstname"] == "Jane"

    with allure.step("Удалить бронирование"):
        status = booking.delete_booking(booking_id, token)
        assert status == 201

    with allure.step("Проверить, что после удаления 404"):
        response = booking.get_booking_response(booking_id)
        assert response.status_code == 404

@allure.feature("Booking")
@allure.title("Частичное обновление бронирования")
@allure.severity(allure.severity_level.NORMAL)
def test_patch_booking(booking, booking_data, token):
    created = booking.create_booking(booking_data)
    ids = created["bookingid"]

    booking.partial_update_booking(ids, {"firstname": "Bird"}, token)

    refetched = booking.get_booking(ids)
    assert refetched["firstname"] == "Bird"
    assert refetched["lastname"] == "Doe"

@allure.feature("Booking")
@allure.title("Создание бронирование без требуемых полей")
@allure.severity(allure.severity_level.MINOR)
def test_create_without_required_fields(booking, booking_data, token):
    invalid_data = {k: v for k, v in booking_data.items() if k != "firstname"}

    response = booking.client.post("/booking", json=invalid_data)
    assert response.status_code == 500




