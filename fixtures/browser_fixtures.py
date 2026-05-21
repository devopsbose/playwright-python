import pytest
from playwright.sync_api import Page
from pages import LoginPage, HomePage, DashboardPage
from data import TestUsers


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def home_page(page: Page) -> HomePage:
    return HomePage(page)


@pytest.fixture
def dashboard_page(page: Page) -> DashboardPage:
    return DashboardPage(page)


@pytest.fixture
def authenticated_page(page: Page) -> Page:
    lp = LoginPage(page)
    lp.open()
    lp.login(TestUsers.VALID.username, TestUsers.VALID.password)
    return page
