from playwright.sync_api import Page
from components.base_component import BaseComponent


class Navbar(BaseComponent):
    CART_LINK = ".shopping_cart_link"
    BURGER_MENU = "#react-burger-menu-btn"
    MENU_LOGOUT = "#logout_sidebar_link"
    MENU_ALL_ITEMS = "#inventory_sidebar_link"
    MENU_ABOUT = "#about_sidebar_link"

    def __init__(self, page: Page):
        super().__init__(page, "#header_container")

    def go_to_cart(self):
        self.page.locator(self.CART_LINK).click()

    def logout(self):
        self.page.locator(self.BURGER_MENU).click()
        self.page.locator(self.MENU_LOGOUT).click()

    def go_to_all_items(self):
        self.page.locator(self.BURGER_MENU).click()
        self.page.locator(self.MENU_ALL_ITEMS).click()
