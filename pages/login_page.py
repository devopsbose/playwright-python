from playwright.sync_api import Page
from .base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)


class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "button[type='submit']"
    ERROR_MESSAGE = ".error-message"
    REMEMBER_ME_CHECKBOX = "#remember-me"

    def __init__(self, page: Page):
        super().__init__(page)
        self.path = "/login"

    def open(self) -> "LoginPage":
        self.navigate(self.path)
        return self

    def enter_username(self, username: str) -> "LoginPage":
        self.fill(self.USERNAME_INPUT, username)
        return self

    def enter_password(self, password: str) -> "LoginPage":
        self.fill(self.PASSWORD_INPUT, password)
        return self

    def click_login(self) -> None:
        logger.info("Submitting login form")
        self.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str) -> None:
        self.enter_username(username).enter_password(password).click_login()

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_displayed(self) -> bool:
        return self.is_visible(self.ERROR_MESSAGE)

    def toggle_remember_me(self) -> "LoginPage":
        self.click(self.REMEMBER_ME_CHECKBOX)
        return self
