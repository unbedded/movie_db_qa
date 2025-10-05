"""Page object for TMDB Discovery page."""

from playwright.sync_api import Page

from movie_db_qa.pages.base_page import BasePage


class DiscoverPage(BasePage):
    """Page object for TMDB Discovery application.

    Encapsulates interactions with the movie discovery interface including
    filters, search, and pagination.
    """

    BASE_URL = "https://tmdb-discover.surge.sh"

    def __init__(self, page: Page) -> None:
        """Initialize Discover page.

        Args:
            page: Playwright page instance
        """
        super().__init__(page)
        self.url = self.BASE_URL

    def load(self) -> None:
        """Load the discover page."""
        self.navigate_to(self.url)
        self.wait_for_load_state("networkidle")

    # Filter actions
    def select_popular_filter(self) -> None:
        """Click Popular category filter."""
        self.logger.info("Clicking Popular filter")
        self.page.click("a[href='/popular']")
        self.wait_for_load_state("networkidle")

    def select_trending_filter(self) -> None:
        """Click Trending category filter."""
        self.logger.info("Clicking Trending filter")
        self.page.click("a[href='/trend']")
        self.wait_for_load_state("networkidle")

    def select_newest_filter(self) -> None:
        """Click Newest category filter."""
        self.logger.info("Clicking Newest filter")
        self.page.click("a[href='/new']")
        self.wait_for_load_state("networkidle")

    def select_top_rated_filter(self) -> None:
        """Click Top Rated category filter."""
        self.logger.info("Clicking Top Rated filter")
        self.page.click("a[href='/top']")
        self.wait_for_load_state("networkidle")

    # Pagination actions
    def click_next_page(self) -> None:
        """Click Next pagination button."""
        self.logger.info("Clicking Next page button")
        self.page.click("text=Next")
        self.wait_for_load_state("networkidle")

    def click_previous_page(self) -> None:
        """Click Previous pagination button."""
        self.logger.info("Clicking Previous page button")
        self.page.click("text=Previous")
        self.wait_for_load_state("networkidle")

    def navigate_to_page(self, page_number: int) -> None:
        """Navigate to specific page number.

        Args:
            page_number: Page number to navigate to
        """
        self.logger.info("Navigating to page: %d", page_number)
        # Click on the page number link in pagination
        self.page.click(f"a:has-text('{page_number}')")
        self.wait_for_load_state("networkidle")

    # Getters
    def get_results_count(self) -> int:
        """Get number of movie results displayed.

        Returns:
            Count of movie cards on page
        """
        # Wait for grid to be visible (handles SPA rendering delay)
        self.page.wait_for_selector(".grid", state="visible", timeout=10000)

        # Movie cards are divs in grid with image + title structure
        movie_cards = self.page.locator(".grid > div").all()
        count = len(movie_cards)
        self.logger.debug("Found %d movie results on page", count)
        return count

    def get_current_page(self) -> int:
        """Get current page number.

        Returns:
            Current page number
        """
        # Extract page number from URL (e.g., /popular/2 -> 2)
        url = self.page.url
        self.logger.debug("Current URL: %s", url)

        # URL patterns: /popular, /popular/1, /popular/2, etc.
        parts = url.rstrip("/").split("/")
        if parts[-1].isdigit():
            page_num = int(parts[-1])
        else:
            page_num = 1  # Default to page 1 if no page number in URL

        self.logger.debug("Current page number: %d", page_num)
        return page_num

    def get_movie_titles(self) -> list[str]:
        """Get list of movie titles on current page.

        Returns:
            List of movie title strings
        """
        # Movie titles are in <p class="text-blue-500 font-bold py-1">
        title_elements = self.page.locator("p.text-blue-500.font-bold.py-1").all()
        titles = [elem.text_content() or "" for elem in title_elements]
        self.logger.debug("Found %d movie titles", len(titles))
        return titles

    # Filter state checkers
    def is_filter_active(self, filter_name: str) -> bool:
        """Check if a filter is in active state.

        Args:
            filter_name: Filter name to check (Popular, Trend, Newest, Top rated)

        Returns:
            True if filter is active, False otherwise
        """
        # Active filter has text-white class, inactive has text-blue-500
        filter_locator = self.page.locator(f"li:has-text('{filter_name}')")
        class_attr = filter_locator.get_attribute("class")
        is_active = "text-white" in (class_attr or "")
        self.logger.debug("Filter '%s' active state: %s", filter_name, is_active)
        return is_active

    def is_popular_filter_active(self) -> bool:
        """Check if Popular filter is active.

        Returns:
            True if Popular filter is active
        """
        return self.is_filter_active("Popular")

    def is_trending_filter_active(self) -> bool:
        """Check if Trending filter is active.

        Returns:
            True if Trending filter is active
        """
        return self.is_filter_active("Trend")

    def is_newest_filter_active(self) -> bool:
        """Check if Newest filter is active.

        Returns:
            True if Newest filter is active
        """
        return self.is_filter_active("Newest")

    def is_top_rated_filter_active(self) -> bool:
        """Check if Top Rated filter is active.

        Returns:
            True if Top Rated filter is active
        """
        return self.is_filter_active("Top rated")
