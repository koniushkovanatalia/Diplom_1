## Задание 1: Юнит-тесты

### Автотесты для проверки класса Burger в Stellar Burgers

### Реализованные сценарии

Покрыты юнит-тестами методы класса `Burger`:

- `set_buns`
- `add_ingredient`
- `remove_ingredient`
- `move_ingredient`
- `get_price`
- `get_receipt`

Процент покрытия кода 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `praktikum` - пакет, содержащий код программы
- `tests` - пакет, содержащий тест `test_burger`

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=praktikum --cov-report=html`
