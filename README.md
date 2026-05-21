# Playwright Python E2E Framework

Enterprise-grade Playwright test framework in Python with POM architecture and parallel execution.

## Structure

```
playwright-python/
├── conftest.py              # Global fixtures + parallel hooks
├── pytest.ini               # pytest config
├── requirements.txt         # Dependencies
├── run_tests.ps1            # Windows test runner helper
├── .env.example             # Environment variable template
├── pages/                   # Page Object Model layer
│   ├── base_page.py         # Base class (navigate, click, fill, expect…)
│   ├── login_page.py
│   ├── home_page.py
│   └── dashboard_page.py
├── tests/                   # Test layer
│   ├── test_login.py
│   └── test_home.py
├── fixtures/                # Reusable fixture layer
│   └── browser_fixtures.py
├── utils/                   # Utilities layer
│   ├── logger.py            # Structured file + console logging
│   └── helpers.py           # retry(), wait_for_condition()
├── data/                    # Data layer
│   └── test_data.py         # UserData dataclass + Faker generator
└── reports/                 # Auto-created: HTML, JSON, screenshots, logs
```

## Setup

```powershell
pip install -r requirements.txt
playwright install
```

Copy `.env.example` to `.env` and adjust values for your environment.

## Running tests

### Parallel (4 workers, Chromium)
```powershell
pytest -n 4 --browser chromium
```

### All three browsers in parallel
```powershell
pytest -n 4 --browser chromium --browser firefox --browser webkit
```

### Headed mode for debugging
```powershell
pytest -n 1 --browser chromium --headed
```

### By marker
```powershell
pytest -n 4 -m smoke
pytest -n 4 -m "login and regression"
```

### PowerShell helper
```powershell
.\run_tests.ps1 -Workers 4 -Marker smoke
.\run_tests.ps1 -AllBrowsers -Workers 6
.\run_tests.ps1 -Headed -Browser firefox
```

## Parallel execution notes

- `pytest-xdist` (`-n N`) forks N worker processes; each gets its own Playwright browser instance via `pytest-playwright`.
- `pytest-playwright` manages one browser per worker automatically — no manual setup needed.
- Screenshots on failure are saved to `reports/screenshots/FAIL_<test_name>.png`.
- Logs go to `reports/logs/test_YYYYMMDD.log`.
- HTML report at `reports/report.html`.

## Adding a new page

1. Create `pages/my_page.py` extending `BasePage`.
2. Export it from `pages/__init__.py`.
3. Add a fixture in `fixtures/browser_fixtures.py` if reuse across tests is needed.
4. Write tests in `tests/test_my_page.py`.
