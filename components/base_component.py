from playwright.sync_api import Page, Locator


class BaseComponent:
    def __init__(self, page: Page, root_selector: str):
        self.page = page
        self.root = page.locator(root_selector)

    def is_visible(self) -> bool:
        return self.root.is_visible()

    def find(self, selector: str) -> Locator:
        return self.root.locator(selector)
