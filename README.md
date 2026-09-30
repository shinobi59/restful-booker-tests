# Restful Booker API Tests

![Tests](https://github.com/shinobi59/restful-booker-tests/actions/workflows/tests.yml/badge.svg)
[![Allure Report](https://img.shields.io/badge/Allure-Report-brightgreen)](https://shinobi59.github.io/restful-booker-tests/)

Автоматизированные тесты для публичного API [Restful Booker](https://restful-booker.herokuapp.com).

## Стек
- Python 3.12+
- pytest
- requests
- Allure

## Структура
- `api` — HTTP-клиент для Restful Booker
- `tests` — тесты
- `conftest.py` — фикстуры

## Запуск
```bash
pip install -r requirements.txt
pytest