import pytest
from fixtures.auth.model import AuthUser
from fixtures.const import ResponseText
from fixtures.register.model import RegisterNewUser, RegisterNewUserResponse


class TestAuth:
    def test_auth_with_valid_data(self, app):
        """
        Шаги.

        1. Авторизоваться с действительными данными.
        2. Убедиться, что код состояния - 200.
        3. Проверить ответ.
        """
        data = RegisterNewUser.random()

        response_register = app.register.register(
            data=data, type_response=RegisterNewUserResponse
        )
        assert response_register.status_code == 201, "Пользователь создан."
        assert (
            response_register.data.message == ResponseText.MESSAGE_REGISTER_USER
        ), "Проверка сообщения."

        response_auth = app.auth.login(data=data, type_response=None)
        assert response_auth.status_code == 200, "Пользователь авторизован."

    def test_login_user_with_not_registered_data(self, app):
        """
        Steps.
            1. Авторизоваться с не действительными данными.
            2. Убедиться, что код состояния - 401
            3. Проверить ответ.
        """
        data = AuthUser.random()
        response = app.auth.login(data=data)
        assert (
            response.status_code == 401
        ), "Пользователь не авторизовался с не действительными данными логина и пароля."

    @pytest.mark.parametrize("field", ["username", "password"])
    def test_auth_empty_data(self, app, field):
        """
        Steps.
            1. Авторизоваться с пустым значением логина.
            2. Убедиться, что код состояния - 401
            3. Проверить ответ.
        """
        data = AuthUser.random()
        setattr(data, field, None)
        response = app.auth.login(data)
        assert (
            response.status_code == 401
        ), "Пользователь не авторизовался с пустыми данными логина и пароля."
