import re
import pytest
from playwright.sync_api import Page, expect
from pages.dashboard_page import DashboardPage
from components.navbar import Navbar


class TestDashboard:

    @pytest.mark.smoke
    def test_dashboard_shows_products(self, authenticated_page: Page):
        dashboard = DashboardPage(authenticated_page)
        assert dashboard.get_product_count() > 0

    def test_dashboard_page_title(self, authenticated_page: Page):
        assert DashboardPage(authenticated_page).get_page_title() == "Products"

    def test_sort_by_price_low_to_high(self, authenticated_page: Page):
        dashboard = DashboardPage(authenticated_page)
        dashboard.sort_products("lohi")

        prices = dashboard.get_all_prices()
        assert prices == sorted(prices), "Products are not sorted by price ascending"

    def test_sort_by_price_high_to_low(self, authenticated_page: Page):
        dashboard = DashboardPage(authenticated_page)
        dashboard.sort_products("hilo")

        prices = dashboard.get_all_prices()
        assert prices == sorted(prices, reverse=True), "Products are not sorted by price descending"

    def test_add_product_to_cart_updates_badge(self, authenticated_page: Page):
        dashboard = DashboardPage(authenticated_page)
        dashboard.add_first_product_to_cart()

        assert dashboard.get_cart_count() == "1"

    def test_navbar_logout_redirects_to_login(self, authenticated_page: Page):
        navbar = Navbar(authenticated_page)
        navbar.logout()

        expect(authenticated_page).to_have_url(re.compile(r".*saucedemo\.com/?$"))

    def test_navigate_to_cart(self, authenticated_page: Page):
        navbar = Navbar(authenticated_page)
        navbar.go_to_cart()

        expect(authenticated_page).to_have_url(re.compile(r".*/cart\.html"))
