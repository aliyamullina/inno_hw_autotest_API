import cattr
from requests import Response


class Validation:
    @staticmethod
    def structure(response: Response, type_response) -> Response:
        """
        Проверка структуры валидации.
        """
        if type_response:
            try:
                response.data = cattr.structure(response.json(), type_response)
            except Exception as e:
                raise e
        return response
