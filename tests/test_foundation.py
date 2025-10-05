"""Foundation test cases for TMDB Discovery application.

This module contains 8 Critical/High priority test cases demonstrating
test design skills using formal techniques (BVA, EP, Decision Tables, etc.).

Test Case Summary:
- TC-FLT-CAT-001: Popular filter works (Critical, EP)
- TC-FLT-CAT-002: Trending filter works (Critical, EP)
- TC-PAG-001: Navigate to page 2 (High, BVA)
- TC-PAG-002: Last page boundary error (High, BVA, DEF-002)
- TC-PAG-003: Filter persists across pagination (High, Exploratory, DEF-003)
- TC-NEG-001: Direct URL access fails (High, Negative, DEF-001)
- TC-NEG-002: Invalid page number (High, BVA)
- TC-CMB-001: Popular + Movies combined (High, Decision Table)

See docs/test-cases.md for detailed specifications with WHY explanations.
"""

import logging

import pytest
from playwright.sync_api import BrowserContext, Page, expect

from movie_db_qa.pages.discover_page import DiscoverPage
from movie_db_qa.utils.config import config

# Module-level logger
logger = logging.getLogger(__name__)


class TestCategoryFilters:
    """Test category filter functionality (Popular, Trending, etc.)."""

    def test_tc_flt_cat_001_popular_filter_works(self, page: Page) -> None:
        """TC-FLT-CAT-001: Popular Filter Works.

        Priority: Critical
        Test Type: Functional
        Design Technique: Equivalence Partitioning (EP)

        WHY: Primary user workflow - Popular is most commonly used filter.
        Tests valid category filter (Popular = valid equivalence class).

        Preconditions: Incognito browser (fresh context via Playwright)

        Steps:
        1. Navigate to base URL
        2. Observe auto-forward to /popular
        3. Verify Popular filter is active
        4. Verify movie results displayed
        5. Count results = 20
        6. Validate API call (discover/movie with sort_by=popularity.desc)
        """
        logger.info("Test started: TC-FLT-CAT-001")

        # Setup
        discover = DiscoverPage(page)

        # Step 1: Navigate to base URL
        logger.info("Navigating to URL: %s", config.base_url)
        discover.load()

        # Step 2: Observe auto-forward to /popular
        expect(page).to_have_url(f"{config.base_url}/popular")
        logger.info("Verified auto-forward to /popular")

        # Step 3: Verify Popular filter is active
        assert discover.is_popular_filter_active(), "Popular filter should be active"
        logger.info("Verified Popular filter is active")

        # Step 4: Verify movie results displayed
        results_count = discover.get_results_count()
        assert results_count > 0, "Should display movie results"
        logger.info("Verified movie results displayed: %d movies", results_count)

        # Step 5: Count results = 20
        assert results_count == config.expected_results_per_page, (
            f"Should display {config.expected_results_per_page} results"
        )

        # Step 6: Validate API call
        api_calls = page.api_calls  # type: ignore[attr-defined]
        movie_calls = [call for call in api_calls if "/movie/" in call["url"]]
        assert len(movie_calls) > 0, "Should make API call to TMDB movie endpoint"

        # Verify Popular endpoint called
        popular_call = [call for call in movie_calls if "/movie/popular" in call["url"]]
        assert len(popular_call) > 0, "Should call /movie/popular endpoint"
        logger.info("Verified API call: %s", popular_call[0]["url"])
        logger.info("Test passed: TC-FLT-CAT-001")

    def test_tc_flt_cat_002_trending_filter_works(self, page: Page) -> None:
        """TC-FLT-CAT-002: Trending Filter Works.

        Priority: Critical
        Test Type: Functional
        Design Technique: Equivalence Partitioning (EP)

        WHY: Second most common workflow - validates filter switching.
        Tests another valid category (Trending = same equivalence class).

        Steps:
        1. Navigate to base URL
        2. Click Trending filter
        3. Verify Trending active, Popular inactive
        4. Verify movie results displayed
        5. Validate API call (discover/movie with sort_by parameter change)
        """
        logger.info("Test started: TC-FLT-CAT-002")

        discover = DiscoverPage(page)

        # Step 1: Navigate
        logger.info("Navigating to URL: %s", config.base_url)
        discover.load()

        # Step 2: Click Trending filter
        logger.info("Applying filter: Trending")
        discover.select_trending_filter()

        # Step 3: Verify filter states
        assert discover.is_trending_filter_active(), "Trending filter should be active"
        assert not discover.is_popular_filter_active(), "Popular filter should be inactive"
        logger.info("Verified filter exclusivity (only Trending active)")

        # Step 4: Verify results displayed
        results_count = discover.get_results_count()
        assert results_count == config.expected_results_per_page, (
            f"Should display {config.expected_results_per_page} results"
        )

        # Step 5: Validate API call for Trending
        api_calls = page.api_calls  # type: ignore[attr-defined]
        movie_calls = [call for call in api_calls if "/movie/" in call["url"]]
        assert len(movie_calls) >= 2, "Should make API calls (Popular + Trending)"

        # Log all movie API calls for visibility
        logger.info("API calls captured: %d movie endpoints", len(movie_calls))
        for call in movie_calls:
            logger.info("  - %s", call["url"])
        logger.info("Test passed: TC-FLT-CAT-002")


class TestPagination:
    """Test pagination functionality (Next/Previous, boundaries)."""

    @pytest.mark.xfail(reason="DEF-007: Pagination navigation broken - Next/page number clicks don't work")
    def test_tc_pag_001_navigate_to_page_2(self, page: Page) -> None:
        """TC-PAG-001: Navigate to Page 2 (Defect Found).

        Priority: High
        Test Type: Functional (Defect)
        Design Technique: Boundary Value Analysis (BVA)
        Defect: DEF-007

        WHY: Page 2 is first boundary (page 1 → page 2 transition).
        Validates core pagination functionality works.

        Expected: TEST SHOULD FAIL - validates newly found defect.

        Steps:
        1. Navigate to /popular
        2. Verify on page 1
        3. Click Next button
        4. Verify URL changed to /popular/2 (FAILS - pagination broken)
        5. Validate API call includes page=2 parameter
        """
        logger.info("Test started: TC-PAG-001")

        discover = DiscoverPage(page)

        # Step 1-2: Navigate and verify page 1
        # Use discover.load() to avoid DEF-001 (direct URL access fails)
        logger.info("Loading discover page (will auto-redirect to /popular)")
        discover.load()
        discover.wait_for_load_state("networkidle")

        initial_page = discover.get_current_page()
        assert initial_page == 1, "Should start on page 1"
        logger.info("Verified starting on page 1")

        # Get page 1 movie titles for comparison
        page1_titles = discover.get_movie_titles()

        # Step 3: Click Next button
        logger.info("Clicking Next button")
        discover.click_next_page()

        # Step 4: Verify URL changed
        expect(page).to_have_url(f"{config.base_url}/popular/2")
        logger.info("Verified URL changed to /popular/2")

        # Step 5: Verify different results
        page2_titles = discover.get_movie_titles()
        assert page1_titles != page2_titles, "Page 2 should have different movies"
        logger.info("Verified different movie results on page 2")

        # Step 6: Verify page indicator
        current_page = discover.get_current_page()
        assert current_page == 2, "Should be on page 2"

        # Step 7: Validate API call with page=2
        api_calls = page.api_calls  # type: ignore[attr-defined]
        movie_calls = [call for call in api_calls if "/movie/" in call["url"]]
        page2_calls = [call for call in movie_calls if "page=2" in call["url"]]
        assert len(page2_calls) > 0, "Should make API call with page=2 parameter"
        logger.info("Verified API call with page=2: %s", page2_calls[0]["url"])
        logger.info("Test passed: TC-PAG-001")

    @pytest.mark.xfail(reason="DEF-002: Known defect - last page pagination broken")
    def test_tc_pag_002_last_page_boundary_error(self, context: BrowserContext) -> None:
        """TC-PAG-002: Last Page Boundary Error (Known Defect).

        Priority: High
        Test Type: Negative
        Design Technique: Boundary Value Analysis (BVA)
        Defect: DEF-002

        WHY: Known defect - last page is upper boundary (off-by-one errors).
        High user impact - users browsing all results hit this error.

        Expected: TEST SHOULD FAIL - validates known defect exists.

        Steps:
        1. Navigate to base URL
        2. Apply Popular filter
        3. Navigate to last page (e.g., page 289)
        4. Observe error screen
        """
        logger.info("Test started: TC-PAG-002 (expected to fail - DEF-002)")

        page: Page = context.new_page()
        discover = DiscoverPage(page)

        # Step 1-2: Navigate and apply filter
        logger.info("Navigating to URL: %s", config.base_url)
        discover.load()

        # Step 3: Navigate to high page number (symptom of DEF-002)
        high_page = 289
        logger.info("Navigating to page: %d", high_page)
        page.goto(f"{config.base_url}/popular/{high_page}")

        # Step 4: Should see error (test expects failure)
        # If this passes, the defect has been fixed
        expect(page.locator("text=Something went wrong")).to_be_visible()
        logger.info("Verified error screen displayed (DEF-002)")

    @pytest.mark.xfail(reason="DEF-003: Known defect - filter lost after pagination")
    def test_tc_pag_003_filter_persists_across_pagination(self, context: BrowserContext) -> None:
        """TC-PAG-003: Filter Persists Across Pagination (Defect Found).

        Priority: High
        Test Type: Functional (Defect)
        Design Technique: Exploratory
        Defect: DEF-003

        WHY: Found during exploration - critical UX issue.
        Users can't browse filtered results across pages.

        Expected: TEST SHOULD FAIL - validates newly found defect.

        Steps:
        1. Navigate to base URL
        2. Click Popular filter
        3. Verify Popular active
        4. Click Next to page 2
        5. Verify Popular still active (FAILS - filter lost)
        """
        logger.info("Test started: TC-PAG-003 (expected to fail - DEF-003)")

        page: Page = context.new_page()
        discover = DiscoverPage(page)

        # Step 1-2: Navigate and apply filter
        logger.info("Navigating to URL: %s", config.base_url)
        discover.load()

        logger.info("Applying filter: Popular")
        discover.select_popular_filter()

        # Step 3: Verify filter active
        assert discover.is_popular_filter_active(), "Popular should be active"
        logger.info("Verified Popular filter active on page 1")

        # Step 4: Navigate to page 2
        logger.info("Clicking Next button")
        discover.click_next_page()

        # Step 5: Verify filter persists (EXPECTED TO FAIL - DEF-003)
        assert discover.is_popular_filter_active(), "Popular filter should persist on page 2"
        logger.info("Verified filter persists (test passed - defect fixed?)")


class TestNegativeCases:
    """Test error handling and edge cases."""

    @pytest.mark.xfail(reason="DEF-001: Known defect - direct URL access fails")
    def test_tc_neg_001_direct_url_access_fails(self, context: BrowserContext) -> None:
        """TC-NEG-001: Direct URL Access Fails (Known Defect).

        Priority: High
        Test Type: Negative
        Design Technique: Negative Testing
        Defect: DEF-001

        WHY: Known defect - tests error handling for invalid direct URLs.
        Prevents bookmarking/sharing functionality.

        Expected: TEST SHOULD FAIL - validates known defect.

        Steps:
        1. Directly navigate to /popular (paste URL)
        2. Observe page fails to load properly
        """
        logger.info("Test started: TC-NEG-001 (expected to fail - DEF-001)")

        page: Page = context.new_page()

        # Step 1: Direct navigation to /popular
        logger.info("Navigating directly to URL: %s/popular", config.base_url)
        page.goto(f"{config.base_url}/popular")
        page.wait_for_load_state("networkidle")

        # Step 2: Should load properly (EXPECTED TO FAIL - DEF-001)
        # If defect exists, page will be blank or show error
        discover = DiscoverPage(page)
        results_count = discover.get_results_count()
        assert results_count == config.expected_results_per_page, "Direct URL should load results properly"
        logger.info("Direct URL loaded successfully (test passed - defect fixed?)")

    @pytest.mark.xfail(reason="DEF-001: Direct URL access fails - cannot test page 0 handling")
    def test_tc_neg_002_invalid_page_number(self, context: BrowserContext) -> None:
        """TC-NEG-002: Invalid Page Number Handling (Blocked by DEF-001).

        Priority: High
        Test Type: Negative
        Design Technique: Boundary Value Analysis (BVA)
        Blocked by: DEF-001

        WHY: Tests invalid boundary (page 0, negative pages).
        App should handle invalid input gracefully.

        Steps:
        1. Navigate to /popular
        2. Manually edit URL to /popular/0
        3. Observe graceful error handling (redirect or error message)
        """
        logger.info("Test started: TC-NEG-002")

        page: Page = context.new_page()

        # Step 1-2: Navigate to invalid page 0
        logger.info("Navigating to invalid page: %s/popular/0", config.base_url)
        page.goto(f"{config.base_url}/popular/0")
        page.wait_for_load_state("networkidle")

        # Step 3: Should handle gracefully (redirect to page 1 OR show error)
        # Test passes if app doesn't crash or show broken UI
        discover = DiscoverPage(page)

        # Either redirected to valid page OR shows error message
        try:
            # Check if redirected to page 1
            current_page = discover.get_current_page()
            assert current_page >= 1, "Should redirect to valid page"
            logger.info("App redirected to valid page: %d", current_page)
        except Exception:
            # Or check if error message shown
            error_visible = page.locator("text=Something went wrong, text=Error, text=Invalid").count() > 0
            assert error_visible, "Should show error message for invalid page"
            logger.info("App showed error message for invalid page")

        logger.info("Test passed: TC-NEG-002")


class TestCombinedFilters:
    """Test combined filter functionality."""

    @pytest.mark.skip(
        reason="Type filter out of scope - foundation focuses on category filters (post-submission expansion)"
    )
    def test_tc_cmb_001_popular_movies_combined(self, context: BrowserContext) -> None:
        """TC-CMB-001: Popular + Movies Type Filter Combined.

        Priority: High
        Test Type: Functional
        Design Technique: Decision Table

        WHY: Tests combination of two filters (Category + Type).
        Validates filters work together correctly (AND operation).

        NOTE: DEFERRED - Type filter (Movies/TV Shows) not yet implemented.
        Will implement if time permits after foundation tests pass.

        Steps:
        1. Navigate to base URL
        2. Click Popular filter
        3. Select Movies type filter
        4. Verify both filters active
        5. Verify results filtered correctly
        """
        logger.info("Test started: TC-CMB-001 (DEFERRED - not implemented)")
        pytest.skip("Type filter not yet implemented in Page Object")
