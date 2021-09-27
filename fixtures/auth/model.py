import attr
from faker import Faker
from fixtures.base import Base
from fixtures.user_info.model import UserInfo

fake = Faker()


@attr.s
class AuthUser(Base):
    username: str = attr.ib(default=None)
    password: str = attr.ib(default=None)

    @staticmethod
    def random():
        return AuthUser(username=fake.email(), password=fake.password())


@attr.s
class AuthUserResponse(Base):
    access_token: str = attr.ib()


@attr.s
class UserType:
    header: dict = attr.ib(default=None)
    uuid: int = attr.ib(default=None)
    user_data: UserInfo = attr.ib(default=None)
