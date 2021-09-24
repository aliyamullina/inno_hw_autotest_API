from fixtures.user_info.model import UserInfo


class TestUserInfo:
    def test_add_user_info(self, app, auth_user):
        """
        Шаги
        1. Заполнить информацию о пользователе действительными данными.
        2. Убедиться, что код состояния - 200
        3. Проверить ответ.
        """
        data = UserInfo.random()
        response = app.user_info.add_user_info(
            user_id=auth_user.uuid, data=data, header=auth_user.header
        )
        assert response.status_code == 200
