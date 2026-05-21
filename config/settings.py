import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")
    API_BASE_URL = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")
    TIMEOUT = int(os.getenv("TIMEOUT", "30000"))
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    SLOW_MO = int(os.getenv("SLOW_MO", "0"))
    SCREENSHOT_ON_FAILURE = os.getenv("SCREENSHOT_ON_FAILURE", "true").lower() == "true"
    VIDEO_ON_FAILURE = os.getenv("VIDEO_ON_FAILURE", "false").lower() == "true"
    ENVIRONMENT = os.getenv("ENVIRONMENT", "staging")

    STANDARD_USER = os.getenv("STANDARD_USER", "standard_user")
    LOCKED_USER = os.getenv("LOCKED_USER", "locked_out_user")
    PASSWORD = os.getenv("PASSWORD", "secret_sauce")


settings = Settings()
