import attr
from faker import Faker
from fixtures.base import Base

fake = Faker()


@attr.s
class RegisterNewUser(Base):
    username: str = attr.ib(default=None)
    password: str = attr.ib(default=None)

    @staticmethod
    def random():
        return RegisterNewUser(username=fake.email(), password=fake.password())


@attr.s
class RegisterNewUserResponse(Base):
    message: str = attr.ib()
    uuid: int = attr.ib()
