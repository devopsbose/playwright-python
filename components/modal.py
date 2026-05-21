from playwright.sync_api import Page, expect
from components.base_component import BaseComponent


class CartModal(BaseComponent):
    CONTINUE_SHOPPING = "[data-test='continue-shopping']"
    CHECKOUT_BTN = "[data-test='checkout']"
    CART_ITEMS = ".cart_item"

    def __init__(self, page: Page):
        super().__init__(page, ".cart_contents_container")

    def get_item_count(self) -> int:
        return self.page.locator(self.CART_ITEMS).count()

    def continue_shopping(self):
        self.page.locator(self.CONTINUE_SHOPPING).click()

    def proceed_to_checkout(self):
        self.page.locator(self.CHECKOUT_BTN).click()

    def expect_visible(self):
        expect(self.root).to_be_visible()
