import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.settings import settings


class TestLogin:

    @pytest.mark.smoke
    def test_successful_login(self, page: Page):
        login = LoginPage(page)
        login.goto()
        login.login(settings.STANDARD_USER, settings.PASSWORD)

        DashboardPage(page).expect_on_dashboard()

    def test_login_with_invalid_credentials(self, page: Page):
        login = LoginPage(page)
        login.goto()
        login.login("invalid_user", "wrong_password")

        login.expect_error_visible()
        assert "Username and password do not match" in login.get_error_message()

    def test_login_locked_out_user(self, page: Page):
        login = LoginPage(page)
        login.goto()
        login.login(settings.LOCKED_USER, settings.PASSWORD)

        login.expect_error_visible()
        assert "locked out" in login.get_error_message().lower()

    def test_login_empty_username(self, page: Page):
        login = LoginPage(page)
        login.goto()
        login.login("", settings.PASSWORD)

        login.expect_error_visible()
        assert "Username is required" in login.get_error_message()

    def test_login_empty_password(self, page: Page):
        login = LoginPage(page)
        login.goto()
        login.login(settings.STANDARD_USER, "")

        login.expect_error_visible()
        assert "Password is required" in login.get_error_message()

    @pytest.mark.parametrize("username,password,expected_error", [
        ("", "", "Username is required"),
        ("some_user", "", "Password is required"),
        ("invalid", "wrong", "Username and password do not match"),
    ])
    def test_login_validation_matrix(self, page: Page, username, password, expected_error):
        login = LoginPage(page)
        login.goto()
        login.login(username, password)

        login.expect_error_visible()
        assert expected_error in login.get_error_message()
