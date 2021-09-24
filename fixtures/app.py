from fixtures.auth.api import Auth
from fixtures.register.api import Register
from fixtures.requests import ClientRequests
from fixtures.user_info.api import AddUserInfo


class App:
    """
    Доступ ко всем методам внутри приложения для начала тестирования.
    """

    def __init__(self, url):
        self.url = url
        self.client_requests = ClientRequests
        self.register = Register(self)
        self.auth = Auth(self)
        self.user_info = AddUserInfo(self)
