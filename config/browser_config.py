from config.settings import settings

BROWSER_CONTEXTS = {
    "chromium": {
        "viewport": {"width": 1920, "height": 1080},
        "ignore_https_errors": True,
    },
    "firefox": {
        "viewport": {"width": 1920, "height": 1080},
        "ignore_https_errors": True,
    },
    "webkit": {
        "viewport": {"width": 1920, "height": 1080},
        "ignore_https_errors": True,
    },
}

LAUNCH_OPTIONS = {
    "headless": settings.HEADLESS,
    "slow_mo": settings.SLOW_MO,
}
