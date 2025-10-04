"""Pytest configuration and fixtures."""

from collections.abc import Generator

import pytest
from playwright.sync_api import Browser, BrowserContext, Page, Playwright, sync_playwright

from movie_db_qa.utils.config import config
from movie_db_qa.utils.logger import setup_logger

logger = setup_logger(__name__)


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
def page(context: BrowserContext) -> Generator[Page, None, None]:
    """Create new page for each test.

    Args:
        context: Browser context from fixture

    Yields:
        Page instance
    """
    page = context.new_page()
    page.set_default_timeout(config.timeout)
    yield page
    page.close()
