# Restful Booker API Tests

[![Tests](https://github.com/shinobi59/restful-booker-tests/actions/workflows/tests.yml/badge.svg)](https://github.com/shinobi59/restful-booker-tests/actions/workflows/tests.yml)
[![Allure Report](https://img.shields.io/badge/Allure-Report-brightgreen)](https://shinobi59.github.io/restful-booker-tests/)

Автоматизированные API-тесты для публичного сервиса [Restful Booker](https://restful-booker.herokuapp.com).

## Стек

- **Python 3.12+**
- **pytest** — тест-фреймворк
- **requests** — HTTP-клиент
- **allure-pytest** — генерация отчётов
- **GitHub Actions** — CI/CD

## Что тестируется

- **Авторизация** — получение токена, невалидные данные
- **CRUD бронирований** — create, read, update (PUT/PATCH), delete, полный цикл с проверкой состояния
- **Healthcheck** — `/ping`
- **Негативные сценарии** — 404, отсутствие обязательных полей

## Структура проекта
```
restful-booker-tests/
├── api/ # HTTP-клиент
│ ├── client.py # обёртка над requests
│ ├── auth.py # работа с токеном
│ └── booking.py # CRUD бронирований
├── tests/ # тесты
│ ├── test_auth.py
│ ├── test_booking_crud.py
│ └── test_ping.py
├── conftest.py # pytest-фикстуры
├── pytest.ini # конфигурация pytest
└── requirements.txt
```

## Allure-отчёт

Локально:

```bash
pytest
allure serve allure-results
```

Либо открыть **живой отчёт**: [shinobi59.github.io/restful-booker-tests](https://shinobi59.github.io/restful-booker-tests/)

## Установка и запуск

```bash
git clone https://github.com/shinobi59/restful-booker-tests.git
cd restful-booker-tests
python -m venv .venv
.venv\Scripts\activate         # Windows
# source .venv/bin/activate    # Linux/Mac
pip install -r requirements.txt
pytest
```  

## CI

Тесты запускаются автоматически на GitHub Actions при каждом push и pull request.
Результаты Allure публикуются на GitHub Pages — [живой отчёт](https://shinobi59.github.io/restful-booker-tests/).

## Автор

Максим — QA Engineer, [GitHub](https://github.com/shinobi59)