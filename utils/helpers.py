from datetime import datetime
from pathlib import Path


def ensure_dir(path: str):
    Path(path).mkdir(parents=True, exist_ok=True)


def timestamp() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def get_screenshot_path(test_name: str) -> str:
    ensure_dir("reports/screenshots")
    return f"reports/screenshots/{test_name}_{timestamp()}.png"


def get_video_path(test_name: str) -> str:
    ensure_dir("reports/videos")
    return f"reports/videos/{test_name}_{timestamp()}.webm"
