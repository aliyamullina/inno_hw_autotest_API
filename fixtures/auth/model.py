import attr
from faker import Faker
from fixtures.base import Base

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
class AuthUserType:
    header: dict = attr.ib()
    uuid: int = attr.ib()
