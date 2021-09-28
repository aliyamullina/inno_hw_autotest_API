from requests import Response
from fixtures.auth.model import AuthUser
from fixtures.validation import Validation
from common.logger import logging as log


class Auth(Validation):
    def __init__(self, app):
        self.app = app

    POST_AUTH = "/auth"

    @log("Авторизация пользователя.")
    def login(self, data: AuthUser, type_response=None) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/auth/authUser
        """
        response = self.app.client_requests.request(
            method="POST",
            url=f"{self.app.url}{self.POST_AUTH}",
            json=data.obj_to_dict(),
        )
        return self.structure(response, type_response=type_response)
