from dataclasses import dataclass
from faker import Faker

fake = Faker()


@dataclass
class UserData:
    username: str
    password: str
    email: str
    first_name: str
    last_name: str


def generate_user() -> UserData:
    return UserData(
        username=fake.user_name(),
        password=fake.password(length=12, special_chars=True),
        email=fake.email(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
    )


class TestUsers:
    VALID = UserData(
        username="standard_user",
        password="secret_sauce",
        email="standard@example.com",
        first_name="Standard",
        last_name="User",
    )
    LOCKED_OUT = UserData(
        username="locked_out_user",
        password="secret_sauce",
        email="locked@example.com",
        first_name="Locked",
        last_name="User",
    )
    INVALID = UserData(
        username="invalid_user",
        password="wrong_password",
        email="invalid@example.com",
        first_name="Invalid",
        last_name="User",
    )
