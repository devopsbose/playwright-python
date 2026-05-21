from playwright.sync_api import Page, expect
from config.settings import settings
from utils.logger import get_logger

logger = get_logger(__name__)


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.timeout = settings.TIMEOUT

    def navigate(self, path: str = ""):
        url = f"{settings.BASE_URL}{path}"
        logger.info(f"Navigating to: {url}")
        self.page.goto(url, timeout=self.timeout)
        self.wait_for_load()

    def wait_for_load(self):
        self.page.wait_for_load_state("networkidle", timeout=self.timeout)

    def get_title(self) -> str:
        return self.page.title()

    def take_screenshot(self, name: str):
        path = f"reports/screenshots/{name}.png"
        self.page.screenshot(path=path, full_page=True)
        logger.info(f"Screenshot saved: {path}")

    def is_visible(self, selector: str) -> bool:
        return self.page.locator(selector).is_visible()

    def click(self, selector: str):
        logger.debug(f"Clicking: {selector}")
        self.page.locator(selector).click()

    def fill(self, selector: str, value: str):
        logger.debug(f"Filling '{selector}'")
        self.page.locator(selector).fill(value)

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text()

    def expect_url(self, url_pattern: str):
        expect(self.page).to_have_url(url_pattern)

    def expect_title(self, title: str):
        expect(self.page).to_have_title(title)
