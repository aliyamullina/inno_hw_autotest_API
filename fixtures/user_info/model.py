import attr
from faker import Faker
from fixtures.base import Base

fake = Faker()


@attr.s
class Address:
    city: str = attr.ib(default=None)
    street: str = attr.ib(default=None)
    home_number: str = attr.ib(default=None)


@attr.s
class UserInfo(Base):
    phone: str = attr.ib(default=None)
    email: str = attr.ib(default=None)
    address: Address = attr.ib(default=None)

    @staticmethod
    def random():
        address = Address(
            city=fake.city(),
            street=fake.street_name(),
            home_number=fake.building_number(),
        )
        return UserInfo(phone=fake.phone_number(), email=fake.email(), address=address)


@attr.s
class AddUserResponse:
    message: str = attr.ib()
    uuid: int = attr.ib()


@attr.s
class UpdateUserInfo(Base):
    phone: str = attr.ib(default=None)
    email: str = attr.ib(default=None)
    address: Address = attr.ib(default=None)

    @staticmethod
    def random():
        address = Address(
            city=fake.city(),
            street=fake.street_name(),
            home_number=fake.building_number(),
        )
        return UpdateUserInfo(
            phone=fake.phone_number(), email=fake.email(), address=address
        )


@attr.s
class UpdateUserInfoResponse:
    message: str = attr.ib()


# @attr.s
# class GetUserInfoResponse:
#     phone: str = attr.ib(default=None)
#     email: str = attr.ib(default=None)
#     userID: int = attr.ib(default=None)
#     street: str = attr.ib(default=None)
#     city: str = attr.ib(default=None)
