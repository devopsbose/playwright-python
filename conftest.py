import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page, BrowserContext, Browser, Playwright

load_dotenv()

# Re-export fixtures so pytest discovers them
from fixtures.browser_fixtures import (  # noqa: F401, E402
    login_page,
    home_page,
    dashboard_page,
    authenticated_page,
)


# ---------------------------------------------------------------------------
# Playwright parallel execution settings
# ---------------------------------------------------------------------------

def pytest_configure(config):
    os.makedirs("reports/screenshots", exist_ok=True)
    os.makedirs("reports/logs", exist_ok=True)


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    """Merge env-driven launch args into the default ones provided by pytest-playwright."""
    slow_mo = int(os.getenv("SLOW_MO", "0"))
    headless = os.getenv("HEADLESS", "true").lower() != "false"
    return {
        **browser_type_launch_args,
        "headless": headless,
        "slow_mo": slow_mo,
    }


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Default context options applied to every browser context."""
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
        "ignore_https_errors": True,
        "record_video_dir": "reports/videos" if os.getenv("RECORD_VIDEO") else None,
    }


# ---------------------------------------------------------------------------
# Screenshot on failure
# ---------------------------------------------------------------------------

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page: Page | None = item.funcargs.get("page")
        if page:
            name = item.nodeid.replace("::", "_").replace("/", "_")
            path = f"reports/screenshots/FAIL_{name}.png"
            try:
                page.screenshot(path=path)
            except Exception:
                pass
