from requests import Response
from fixtures.register.model import RegisterNewUser
from fixtures.validation import Validation
from common.deco import logging as log


class Register(Validation):
    def __init__(self, app):
        self.app = app

    POST_REGISTER = "/register"

    @log("Регистрация нового пользователя.")
    def register(self, data: RegisterNewUser, type_response=None) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/register/regUser
        """
        response = self.app.client_requests.request(
            method="POST",
            url=f"{self.app.url}{self.POST_REGISTER}",
            json=data.obj_to_dict(),
        )
        return self.structure(response, type_response=type_response)
