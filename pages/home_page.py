from playwright.sync_api import Page
from .base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)


class HomePage(BasePage):
    # Locators
    NAV_MENU = "nav.main-nav"
    SEARCH_INPUT = "input[placeholder='Search...']"
    SEARCH_BUTTON = "button.search-btn"
    HERO_HEADING = "h1.hero-heading"
    USER_AVATAR = ".user-avatar"
    LOGOUT_LINK = "a[href='/logout']"

    def __init__(self, page: Page):
        super().__init__(page)
        self.path = "/"

    def open(self) -> "HomePage":
        self.navigate(self.path)
        return self

    def search(self, query: str) -> "HomePage":
        self.fill(self.SEARCH_INPUT, query)
        self.click(self.SEARCH_BUTTON)
        logger.info(f"Searched for: {query}")
        return self

    def get_heading(self) -> str:
        return self.get_text(self.HERO_HEADING)

    def is_logged_in(self) -> bool:
        return self.is_visible(self.USER_AVATAR)

    def logout(self) -> None:
        self.click(self.USER_AVATAR)
        self.click(self.LOGOUT_LINK)
        logger.info("User logged out")
