from requests import Response
from fixtures.user_info.model import UserInfo
from fixtures.validation import Validation
from common.deco import logging as log


class AddUserInfo(Validation):
    def __init__(self, app):
        self.app = app

    POST_USER_INFO = "/user_info/{}"

    @log("Добавление информации о пользователе.")
    def add_user_info(
        self, user_id: int, data: UserInfo, header=None, type_response=None
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/userInfo/userInfoAdd
        """
        response = self.app.client_requests.request(
            method="POST",
            url=f"{self.app.url}{self.POST_USER_INFO.format(user_id)}",
            json=data.obj_to_dict(),
            headers=header,
        )
        return self.structure(response, type_response=type_response)
