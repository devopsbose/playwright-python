import pytest
from pages import LoginPage
from data import TestUsers, generate_user


@pytest.mark.login
@pytest.mark.smoke
class TestLoginSuccess:

    def test_valid_login_redirects_to_dashboard(self, login_page: LoginPage):
        login_page.open()
        login_page.login(TestUsers.VALID.username, TestUsers.VALID.password)
        login_page.wait_for_url("**/dashboard**")

    def test_login_page_title_is_correct(self, login_page: LoginPage):
        login_page.open()
        assert "Login" in login_page.get_title()


@pytest.mark.login
@pytest.mark.regression
class TestLoginFailure:

    def test_invalid_credentials_shows_error(self, login_page: LoginPage):
        login_page.open()
        login_page.login(TestUsers.INVALID.username, TestUsers.INVALID.password)
        assert login_page.is_error_displayed(), "Error message should be visible"

    def test_empty_username_shows_error(self, login_page: LoginPage):
        login_page.open()
        login_page.login("", TestUsers.VALID.password)
        assert login_page.is_error_displayed()

    def test_empty_password_shows_error(self, login_page: LoginPage):
        login_page.open()
        login_page.login(TestUsers.VALID.username, "")
        assert login_page.is_error_displayed()

    def test_locked_out_user_sees_error(self, login_page: LoginPage):
        login_page.open()
        login_page.login(TestUsers.LOCKED_OUT.username, TestUsers.LOCKED_OUT.password)
        assert login_page.is_error_displayed()

    @pytest.mark.parametrize("username,password", [
        ("", ""),
        ("user@", "pass"),
        ("a" * 256, "password"),
    ])
    def test_boundary_inputs(self, login_page: LoginPage, username: str, password: str):
        login_page.open()
        login_page.login(username, password)
        assert login_page.is_error_displayed() or login_page.is_visible(LoginPage.ERROR_MESSAGE)
