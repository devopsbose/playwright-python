from data.generators import generator


class UserFactory:
    @staticmethod
    def build(**kwargs) -> dict:
        return {
            "name": kwargs.get("name", generator.full_name()),
            "email": kwargs.get("email", generator.email()),
            "job": kwargs.get("job", generator.job_title()),
            "first_name": kwargs.get("first_name", generator.first_name()),
            "last_name": kwargs.get("last_name", generator.last_name()),
            "zip": kwargs.get("zip", generator.zip_code()),
        }

    @staticmethod
    def build_checkout_info(**kwargs) -> dict:
        return {
            "first_name": kwargs.get("first_name", generator.first_name()),
            "last_name": kwargs.get("last_name", generator.last_name()),
            "zip": kwargs.get("zip", generator.zip_code()),
        }


class ApiUserFactory:
    @staticmethod
    def build(**kwargs) -> dict:
        return {
            "name": kwargs.get("name", generator.full_name()),
            "job": kwargs.get("job", generator.job_title()),
        }
