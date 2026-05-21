from faker import Faker

_fake = Faker()


class DataGenerator:
    @staticmethod
    def first_name() -> str:
        return _fake.first_name()

    @staticmethod
    def last_name() -> str:
        return _fake.last_name()

    @staticmethod
    def full_name() -> str:
        return _fake.name()

    @staticmethod
    def email() -> str:
        return _fake.email()

    @staticmethod
    def phone() -> str:
        return _fake.phone_number()

    @staticmethod
    def address() -> str:
        return _fake.address()

    @staticmethod
    def zip_code() -> str:
        return _fake.zipcode()

    @staticmethod
    def job_title() -> str:
        return _fake.job()

    @staticmethod
    def company() -> str:
        return _fake.company()

    @staticmethod
    def password(length: int = 12) -> str:
        return _fake.password(length=length)

    @staticmethod
    def sentence() -> str:
        return _fake.sentence()

    @staticmethod
    def uuid() -> str:
        return str(_fake.uuid4())


generator = DataGenerator()
