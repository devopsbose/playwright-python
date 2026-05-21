import os
from playwright.sync_api import Page, expect
from utils.logger import get_logger

logger = get_logger(__name__)


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = os.getenv("BASE_URL", "https://example.com")
        self.timeout = int(os.getenv("TIMEOUT", "30000"))

    def navigate(self, path: str = "") -> None:
        url = f"{self.base_url}{path}"
        logger.info(f"Navigating to: {url}")
        self.page.goto(url)

    def get_title(self) -> str:
        return self.page.title()

    def wait_for_url(self, url_pattern: str) -> None:
        self.page.wait_for_url(url_pattern, timeout=self.timeout)

    def take_screenshot(self, name: str) -> None:
        path = f"reports/screenshots/{name}.png"
        os.makedirs("reports/screenshots", exist_ok=True)
        self.page.screenshot(path=path)
        logger.info(f"Screenshot saved: {path}")

    def expect_visible(self, locator_str: str) -> None:
        expect(self.page.locator(locator_str)).to_be_visible(timeout=self.timeout)

    def expect_text(self, locator_str: str, text: str) -> None:
        expect(self.page.locator(locator_str)).to_have_text(text, timeout=self.timeout)

    def click(self, locator_str: str) -> None:
        logger.debug(f"Clicking: {locator_str}")
        self.page.locator(locator_str).click()

    def fill(self, locator_str: str, value: str) -> None:
        logger.debug(f"Filling '{locator_str}' with value")
        self.page.locator(locator_str).fill(value)

    def get_text(self, locator_str: str) -> str:
        return self.page.locator(locator_str).inner_text()

    def is_visible(self, locator_str: str) -> bool:
        return self.page.locator(locator_str).is_visible()
