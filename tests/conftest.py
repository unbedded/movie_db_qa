"""Pytest configuration and fixtures."""

import logging
from collections.abc import Generator
from pathlib import Path
from typing import Any

import pytest
from playwright.sync_api import Browser, BrowserContext, Page, Playwright, sync_playwright

from movie_db_qa.utils.config import config

# Screenshot directory
SCREENSHOT_DIR = Path("artifacts/bug-screenshots")
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

# Log directory
LOG_DIR = Path("artifacts/logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)


@pytest.fixture(scope="session", autouse=True)
def configure_logging() -> Generator[None, None, None]:
    """Configure root logger to capture all test logs to file.

    This runs once per test session and captures logs from all modules.
    """
    # Configure root logger with both console and file handlers
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # File handler
    log_file = LOG_DIR / "test_execution.log"
    file_handler = logging.FileHandler(log_file, mode="w")  # Overwrite each run
    file_handler.setLevel(logging.INFO)
    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(file_formatter)
    root_logger.addHandler(file_handler)

    yield

    # Cleanup
    file_handler.close()
    root_logger.removeHandler(file_handler)


# Module logger
logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def playwright_instance() -> Generator[Playwright, None, None]:
    """Create Playwright instance for session.

    Yields:
        Playwright instance
    """
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright) -> Generator[Browser, None, None]:
    """Launch browser for session.

    Args:
        playwright_instance: Playwright instance from fixture

    Yields:
        Browser instance
    """
    logger.info("Launching %s browser (headless=%s)", config.browser, config.headless)
    browser = playwright_instance.chromium.launch(
        headless=config.headless,
        slow_mo=config.slow_mo,
    )
    yield browser
    logger.info("Closing browser")
    browser.close()


@pytest.fixture
def context(browser: Browser) -> Generator[BrowserContext, None, None]:
    """Create new browser context for each test.

    Args:
        browser: Browser instance from fixture

    Yields:
        Browser context
    """
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
    )
    yield context
    context.close()


@pytest.fixture
def page(context: BrowserContext, request: pytest.FixtureRequest) -> Generator[Page, None, None]:
    """Create new page for each test.

    Args:
        context: Browser context from fixture
        request: Pytest request fixture for test metadata

    Yields:
        Page instance
    """
    page = context.new_page()
    page.set_default_timeout(config.timeout)

    # Store API calls for validation (attached to page for test access)
    api_calls: list[dict[str, Any]] = []
    page.api_calls = api_calls  # type: ignore[attr-defined]

    def handle_request(request: Any) -> None:
        """Capture API requests for validation.

        Args:
            request: Playwright request object
        """
        # Filter for TMDB API calls
        if "api.themoviedb.org" in request.url:
            api_calls.append(
                {
                    "url": request.url,
                    "method": request.method,
                    "resource_type": request.resource_type,
                }
            )
            logger.info("API call captured: %s %s", request.method, request.url)

    # Attach request listener
    page.on("request", handle_request)

    yield page

    # Capture screenshot on test failure (including xfail tests to show actual bug state)
    if hasattr(request.node, "rep_call"):
        # Capture for both unexpected failures and expected failures (xfail)
        # xfail screenshots demonstrate the actual defect behavior
        if request.node.rep_call.failed or (
            hasattr(request.node.rep_call, "wasxfail") and request.node.rep_call.wasxfail
        ):
            screenshot_name = f"{request.node.name}_{request.node.rep_call.when}.png"
            screenshot_path = SCREENSHOT_DIR / screenshot_name
            status = "xfail" if hasattr(request.node.rep_call, "wasxfail") else "failed"
            logger.info("Test %s - capturing screenshot: %s", status, screenshot_path)
            page.screenshot(path=str(screenshot_path))

    page.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo[None]) -> Generator[None, Any, None]:
    """Pytest hook to capture test results for screenshot on failure.

    NOTE: xfail tests in this project document EXPECTED application failures
    (known bugs DEF-001, DEF-002, DEF-003, DEF-007), not test implementation issues.
    This is proper pytest usage for maintaining coverage while preventing false CI failures.

    Args:
        item: Test item
        call: Test call info

    Yields:
        Test outcome
    """
    # Execute all other hooks to obtain the report object
    outcome: Any = yield
    rep = outcome.get_result()

    # Store test results on item for access in fixtures
    setattr(item, f"rep_{rep.when}", rep)
