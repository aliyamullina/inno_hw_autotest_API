from fixtures.const import ResponseText
from fixtures.register.model import RegisterNewUser, RegisterNewUserResponse


class TestRegisterUser:
    def test_register_user_with_valid_data(self, app):
        """
        Шаги.

        1. Зарегистрировать пользователя с действительными данными.
        2. Убедиться, что код состояния - 201.
        3. Проверить ответ.
        """
        data = RegisterNewUser.random()
        response = app.register.register(
            data=data, type_response=RegisterNewUserResponse
        )
        assert response.status_code == 201
        assert (
            response.data.message == ResponseText.MESSAGE_REGISTER_USER
        ), "Check response message"


# Проверка на длину 20 юзернейм 10 пасс
# Проверка на числа и булевое значение юзернейм и пасс  это стринги
# Проверка на пустые строки
# На существующий юзернейм, два раза посылать одни и те же данные
# Если будут баги https://youtu.be/9oNoqttYeA4?t=10069
