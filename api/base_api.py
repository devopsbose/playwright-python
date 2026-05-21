import requests
from requests import Response, Session
from config.settings import settings
from utils.logger import get_logger

logger = get_logger(__name__)


class BaseAPI:
    def __init__(self, base_url: str = None):
        self.base_url = base_url or settings.API_BASE_URL
        self.session: Session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
        })

    def get(self, endpoint: str, params: dict = None) -> Response:
        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET {url}")
        response = self.session.get(url, params=params)
        logger.debug(f"Response [{response.status_code}]: {response.text[:200]}")
        return response

    def post(self, endpoint: str, payload: dict = None) -> Response:
        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST {url}")
        response = self.session.post(url, json=payload)
        logger.debug(f"Response [{response.status_code}]: {response.text[:200]}")
        return response

    def put(self, endpoint: str, payload: dict = None) -> Response:
        url = f"{self.base_url}{endpoint}"
        logger.info(f"PUT {url}")
        response = self.session.put(url, json=payload)
        logger.debug(f"Response [{response.status_code}]: {response.text[:200]}")
        return response

    def patch(self, endpoint: str, payload: dict = None) -> Response:
        url = f"{self.base_url}{endpoint}"
        logger.info(f"PATCH {url}")
        response = self.session.patch(url, json=payload)
        logger.debug(f"Response [{response.status_code}]: {response.text[:200]}")
        return response

    def delete(self, endpoint: str) -> Response:
        url = f"{self.base_url}{endpoint}"
        logger.info(f"DELETE {url}")
        response = self.session.delete(url)
        logger.debug(f"Response [{response.status_code}]")
        return response

    def set_auth_token(self, token: str):
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def assert_status(self, response: Response, expected: int):
        assert response.status_code == expected, (
            f"Expected {expected}, got {response.status_code}. Body: {response.text}"
        )
