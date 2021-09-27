[![tests](https://github.com/aliyamullina/inno_hw_tests_API/actions/workflows/tests_ci.yml/badge.svg)](https://github.com/aliyamullina/inno_hw_tests_API/actions/workflows/tests_ci.yml)

# Автотесты API
Это учебный проект, в котором показано, как реализовать тесты API в Python.

В проекте используются:
- Python
- Requests
- Allure для отчетов
- CI (GitHub actions)
- Тестируемое приложение на Flask 

### Описание API
[app.swaggerhub.com](https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0)

### Тестируемое API
[stores-tests-api.herokuapp.com](https://stores-tests-api.herokuapp.com/)

### Gitgub проекта
[flask-restful-api](https://github.com/berpress/flask-restful-api)

# Тесты
### Тесты на регистрацию
```
tests/register/test_register.py
```
### Тесты на авторизацию
```
tests/auth/test_auth.py
```
### Тесты на добавление данных пользователя
```
tests/user_info/test_add_user_info.py
```
### Тесты на обновление данных пользователя
```
tests/user_info/test_update_user_info.py
```
# Установка
### Отчеты Allure
[docs.qameta.io/allure/#_get_started](https://docs.qameta.io/allure/#_get_started)
### Зависимости
```
pip install -r requirements.txt
```
### Запуск тестов из терминала
```
tox
```
