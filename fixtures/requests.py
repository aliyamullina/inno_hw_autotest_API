import requests
from requests import Response


class ClientRequests:
    """
    HTTP клиент, нужен для запросов.
    Здесь библиотека requests изолирована от api.

    **kwargs: params, json, headers.
    """

    @staticmethod
    def request(method: str, url: str, **kwargs) -> Response:
        return requests.request(method, url, **kwargs)
