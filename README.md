# Restful Booker API Tests

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