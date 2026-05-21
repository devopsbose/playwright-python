import re
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class DashboardPage(BasePage):
    PAGE_TITLE = ".title"
    PRODUCT_ITEMS = ".inventory_item"
    CART_BADGE = ".shopping_cart_badge"
    SORT_DROPDOWN = "[data-test='product_sort_container']"
    ADD_TO_CART_BUTTONS = ".inventory_item button"
    ITEM_PRICES = ".inventory_item_price"

    def __init__(self, page: Page):
        super().__init__(page)

    def get_page_title(self) -> str:
        return self.get_text(self.PAGE_TITLE)

    def get_product_count(self) -> int:
        return self.page.locator(self.PRODUCT_ITEMS).count()

    def get_cart_count(self) -> str:
        badge = self.page.locator(self.CART_BADGE)
        return badge.inner_text() if badge.is_visible() else "0"

    def sort_products(self, option: str):
        self.page.locator(self.SORT_DROPDOWN).select_option(option)

    def get_all_prices(self) -> list[float]:
        texts = self.page.locator(self.ITEM_PRICES).all_inner_texts()
        return [float(p.replace("$", "")) for p in texts]

    def add_first_product_to_cart(self):
        self.page.locator(self.ADD_TO_CART_BUTTONS).first.click()

    def expect_on_dashboard(self):
        expect(self.page).to_have_url(re.compile(r".*/inventory\.html"))
        expect(self.page.locator(self.PAGE_TITLE)).to_be_visible()
