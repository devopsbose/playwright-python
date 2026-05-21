import pytest
from api.clients.user_api import UserAPI
from data.factories import ApiUserFactory


@pytest.fixture(scope="class")
def user_api():
    return UserAPI()


class TestUsersAPI:

    @pytest.mark.smoke
    def test_get_users_returns_200(self, user_api: UserAPI):
        response = user_api.get_users()
        user_api.assert_status(response, 200)

    def test_get_users_returns_list(self, user_api: UserAPI):
        response = user_api.get_users()
        body = response.json()
        assert isinstance(body, list)
        assert len(body) > 0

    def test_get_users_page_2(self, user_api: UserAPI):
        response = user_api.get_users(page=2, limit=5)
        user_api.assert_status(response, 200)
        body = response.json()
        assert isinstance(body, list)
        assert len(body) > 0

    def test_get_single_user(self, user_api: UserAPI):
        response = user_api.get_user(1)
        user_api.assert_status(response, 200)
        assert response.json()["id"] == 1

    def test_get_non_existent_user_returns_404(self, user_api: UserAPI):
        response = user_api.get_user(9999)
        user_api.assert_status(response, 404)

    def test_create_user_returns_201(self, user_api: UserAPI):
        payload = ApiUserFactory.build()
        response = user_api.create_user(payload["name"], payload["job"])

        user_api.assert_status(response, 201)
        body = response.json()
        assert body["name"] == payload["name"]
        assert body["job"] == payload["job"]
        assert "id" in body

    def test_update_user(self, user_api: UserAPI):
        payload = ApiUserFactory.build()
        response = user_api.update_user(1, payload["name"], payload["job"])

        user_api.assert_status(response, 200)
        body = response.json()
        assert body["name"] == payload["name"]
        assert body["job"] == payload["job"]

    def test_delete_user_returns_200(self, user_api: UserAPI):
        response = user_api.delete_user(1)
        user_api.assert_status(response, 200)

    @pytest.mark.parametrize("user_id", [1, 2, 3])
    def test_get_multiple_users(self, user_api: UserAPI, user_id: int):
        response = user_api.get_user(user_id)
        user_api.assert_status(response, 200)
        assert response.json()["id"] == user_id
