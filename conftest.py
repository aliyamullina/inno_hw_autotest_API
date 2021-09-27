import logging
import pytest
from fixtures.app import App
from fixtures.auth.model import AuthUserResponse, UserType
from fixtures.register.model import RegisterNewUser, RegisterNewUserResponse
from fixtures.user_info.model import UserInfo

logger = logging.getLogger("API")


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--api-url")
    logger.info(f"Запуск тестов API, ссылка {url}")
    return App(url)


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="https://stores-tests-api.herokuapp.com/",
    ),


@pytest.fixture
def auth_user(app):
    data = RegisterNewUser.random()
    response_register = app.register.register(
        data=data, type_response=RegisterNewUserResponse
    )
    response_auth = app.auth.login(data=data, type_response=AuthUserResponse)

    token = response_auth.data.access_token
    header = {"Authorization": f"JWT {token}"}
    user_uuid = response_register.data.uuid
    return UserType(header, user_uuid)


@pytest.fixture
def user_info(app, auth_user):
    data = UserInfo.random()
    app.user_info.add_user_info(
        user_id=auth_user.uuid, data=data, header=auth_user.header
    )
    auth_user.user_data = data
    return UserType(header=auth_user.header, uuid=auth_user.uuid, user_data=data)
