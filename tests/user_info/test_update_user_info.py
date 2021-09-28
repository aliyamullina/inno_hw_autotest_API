import pytest

from fixtures.user_info.model import UpdateUserInfo, UpdateUserInfoResponse


class TestUpdateUserInfo:
    def test_update_user_info(self, app, user_info):
        """
        Шаги.

        1. Обновить информацию о пользователе действительными данными.
        2. Убедиться, что код состояния - 200
        3. Проверить ответ.
        """
        data = UpdateUserInfo.random()
        response = app.user_info.update_user_info(
            user_id=user_info.uuid,
            data=data,
            type_response=UpdateUserInfoResponse,
            header=user_info.header,
        )
        assert response.status_code == 200

    @pytest.mark.parametrize("uuid", ["kjbkjkjb", "@/jhk", -55, True])
    def test_update_invalid_id_user_info(self, app, user_info, uuid):
        """
        Шаги.

        1. Обновить информацию об id пользователя различными типами данных.
        2. Убедиться, что код состояния - 404
        3. Проверить ответ.
        """
        data = UpdateUserInfo.random()
        response = app.user_info.update_user_info(
            user_id=uuid,
            data=data,
            type_response=None,
            header=user_info.header,
        )
        assert response.status_code == 404

    def test_update_none_exist_id_user_info(self, app, user_info, uuid=1000):
        """
        Шаги.

        1. Обновить информацию об id пользователе с не существующими данными.
        2. Убедиться, что код состояния - 404
        3. Проверить ответ.
        """
        data = UpdateUserInfo.random()
        response = app.user_info.update_user_info(
            user_id=uuid,
            data=data,
            type_response=None,
            header=user_info.header,
        )
        assert response.status_code == 404

    @pytest.mark.xfail(
        reason="Ожидается 400 ошибка, при добавлении номера длиной 10 000."
    )
    def test_update_max_size_number_phone_user_info(
        self, app, user_info, phone="1" * 10000
    ):
        """
        Шаги.

        1. Обновить информацию о номере телефона пользователя с максимальными числом.
        2. Убедиться, что код состояния - 400
        3. Проверить ответ.
        """
        data = UpdateUserInfo.random()
        setattr(data, "phone", phone)
        response = app.user_info.update_user_info(
            user_id=user_info.uuid,
            data=data,
            type_response=None,
            header=user_info.header,
        )
        assert response.status_code == 400

    def test_update_without_header_user_info(self, app, user_info):
        """
        Шаги.

        1. Заполнить информацию о пользователе с пустым значением header.
        2. Убедиться, что код состояния - 401
        3. Проверить ответ.
        """
        data = UpdateUserInfo.random()
        response = app.user_info.update_user_info(
            user_id=user_info.uuid,
            data=data,
            type_response=None,
            header=None,
        )
        assert response.status_code == 401
