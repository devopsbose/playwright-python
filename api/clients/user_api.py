from api.base_api import BaseAPI
from requests import Response


class UserAPI(BaseAPI):
    ENDPOINT = "/users"

    def get_users(self, page: int = 1, limit: int = 5) -> Response:
        return self.get(self.ENDPOINT, params={"_page": page, "_limit": limit})

    def get_user(self, user_id: int) -> Response:
        return self.get(f"{self.ENDPOINT}/{user_id}")

    def create_user(self, name: str, job: str) -> Response:
        return self.post(self.ENDPOINT, payload={"name": name, "job": job})

    def update_user(self, user_id: int, name: str, job: str) -> Response:
        return self.put(f"{self.ENDPOINT}/{user_id}", payload={"name": name, "job": job})

    def delete_user(self, user_id: int) -> Response:
        return self.delete(f"{self.ENDPOINT}/{user_id}")
