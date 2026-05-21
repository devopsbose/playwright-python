from playwright.sync_api import Page
from .base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)


class DashboardPage(BasePage):
    # Locators
    DASHBOARD_TITLE = "h1.dashboard-title"
    STATS_CARDS = ".stats-card"
    ACTIVITY_TABLE = "table.activity-table"
    TABLE_ROWS = "table.activity-table tbody tr"
    LOADING_SPINNER = ".loading-spinner"

    def __init__(self, page: Page):
        super().__init__(page)
        self.path = "/dashboard"

    def open(self) -> "DashboardPage":
        self.navigate(self.path)
        return self

    def wait_for_load(self) -> "DashboardPage":
        self.page.wait_for_selector(self.LOADING_SPINNER, state="hidden", timeout=self.timeout)
        return self

    def get_title(self) -> str:
        return self.get_text(self.DASHBOARD_TITLE)

    def get_stats_count(self) -> int:
        return self.page.locator(self.STATS_CARDS).count()

    def get_table_row_count(self) -> int:
        return self.page.locator(self.TABLE_ROWS).count()

    def get_row_data(self, row_index: int) -> list[str]:
        row = self.page.locator(self.TABLE_ROWS).nth(row_index)
        cells = row.locator("td")
        return [cells.nth(i).inner_text() for i in range(cells.count())]
