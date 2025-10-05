"""Base page object with common interactions for all pages."""

import logging

from playwright.sync_api import Page


class BasePage:
    """Base page object with common page interactions.

    All page objects inherit from this class to share common functionality
    like navigation, waiting, and element interactions.
    """

    def __init__(self, page: Page) -> None:
        """Initialize base page.

        Args:
            page: Playwright page instance
        """
        # CLAUDE.md: Instantiate logging as first step in constructor
        self.logger = logging.getLogger(self.__class__.__name__)
        self.page = page

    def navigate_to(self, url: str) -> None:
        """Navigate to a specific URL.

        Args:
            url: The URL to navigate to
        """
        self.page.goto(url)

    def get_title(self) -> str:
        """Get the page title.

        Returns:
            Page title as string
        """
        return self.page.title()

    def get_url(self) -> str:
        """Get current page URL.

        Returns:
            Current URL as string
        """
        return self.page.url

    def wait_for_load_state(self, state: str = "load") -> None:
        """Wait for page to reach specific load state.

        Args:
            state: Load state to wait for (load, domcontentloaded, networkidle)
        """
        self.page.wait_for_load_state(state)  # type: ignore

    def screenshot(self, path: str) -> None:
        """Take a screenshot of the current page.

        Args:
            path: File path to save screenshot
        """
        self.page.screenshot(path=path)
