import time
from typing import Callable, Any
from utils.logger import get_logger

logger = get_logger(__name__)


def retry(func: Callable, retries: int = 3, delay: float = 1.0) -> Any:
    last_exc = None
    for attempt in range(1, retries + 1):
        try:
            return func()
        except Exception as exc:
            last_exc = exc
            logger.warning(f"Attempt {attempt}/{retries} failed: {exc}")
            if attempt < retries:
                time.sleep(delay)
    raise last_exc


def wait_for_condition(condition: Callable[[], bool], timeout: float = 10.0, poll: float = 0.5) -> bool:
    deadline = time.time() + timeout
    while time.time() < deadline:
        if condition():
            return True
        time.sleep(poll)
    return False


def build_url(base: str, path: str, params: dict | None = None) -> str:
    url = f"{base.rstrip('/')}/{path.lstrip('/')}"
    if params:
        query = "&".join(f"{k}={v}" for k, v in params.items())
        url = f"{url}?{query}"
    return url
