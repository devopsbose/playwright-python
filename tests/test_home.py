import pytest
from playwright.sync_api import Page
from pages import HomePage, DashboardPage


@pytest.mark.smoke
class TestHomePage:

    def test_home_page_loads(self, home_page: HomePage):
        home_page.open()
        assert home_page.get_title() != ""

    def test_nav_menu_is_visible(self, home_page: HomePage):
        home_page.open()
        home_page.expect_visible(HomePage.NAV_MENU)

    def test_heading_is_present(self, home_page: HomePage):
        home_page.open()
        home_page.expect_visible(HomePage.HERO_HEADING)


@pytest.mark.regression
class TestHomeAuthenticated:

    def test_authenticated_user_sees_avatar(self, authenticated_page: Page):
        home = HomePage(authenticated_page)
        home.open()
        assert home.is_logged_in(), "Logged-in user should see avatar"

    def test_search_stays_on_page(self, authenticated_page: Page):
        home = HomePage(authenticated_page)
        home.open()
        home.search("playwright")
        home.wait_for_url("**/search**")


@pytest.mark.smoke
class TestDashboard:

    def test_dashboard_loads_after_login(self, authenticated_page: Page):
        dashboard = DashboardPage(authenticated_page)
        dashboard.open()
        dashboard.wait_for_load()
        assert dashboard.get_title() != ""

    def test_dashboard_has_stats_cards(self, authenticated_page: Page):
        dashboard = DashboardPage(authenticated_page)
        dashboard.open()
        dashboard.wait_for_load()
        assert dashboard.get_stats_count() > 0
