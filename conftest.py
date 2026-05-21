import pytest
from pathlib import Path
from playwright.sync_api import Page
from config.settings import settings
from config.browser_config import BROWSER_CONTEXTS
from utils.logger import get_logger

logger = get_logger(__name__)

for _dir in ["reports/screenshots", "reports/logs", "reports/videos"]:
    Path(_dir).mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# Browser launch / context configuration
# ---------------------------------------------------------------------------

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": settings.HEADLESS,
        "slow_mo": settings.SLOW_MO,
    }


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, browser_name):
    context_overrides = BROWSER_CONTEXTS.get(browser_name, {})
    if settings.VIDEO_ON_FAILURE:
        context_overrides["record_video_dir"] = "reports/videos/"
    return {**browser_context_args, **context_overrides}


# ---------------------------------------------------------------------------
# Authenticated page fixture
# ---------------------------------------------------------------------------

@pytest.fixture
def authenticated_page(page: Page):
    """Yields a page already logged in as the standard user, with dashboard confirmed loaded."""
    from pages.login_page import LoginPage
    from pages.dashboard_page import DashboardPage
    login = LoginPage(page)
    login.goto()
    login.login(settings.STANDARD_USER, settings.PASSWORD)
    DashboardPage(page).expect_on_dashboard()
    yield page


# ---------------------------------------------------------------------------
# Failure screenshot hook
# ---------------------------------------------------------------------------

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed and settings.SCREENSHOT_ON_FAILURE:
        page: Page | None = item.funcargs.get("page") or item.funcargs.get("authenticated_page")
        if page:
            safe_name = item.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_")
            path = f"reports/screenshots/FAILED_{safe_name}.png"
            try:
                page.screenshot(path=path, full_page=True)
                logger.info(f"Failure screenshot saved: {path}")
            except Exception as exc:
                logger.warning(f"Could not capture failure screenshot: {exc}")
