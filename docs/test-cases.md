# Test Cases

**Project:** movie_db_qa - QA Automation for TMDB Discovery App
**Version:** 1.0
**Last Updated:** 2025-10-04
**Status:** ✅ Complete - Foundation (8 test cases)

---

## Overview

This document contains detailed, step-by-step test case descriptions for the TMDB Discovery application.

**Assignment Requirement:**
> "Be creative!" and explain **WHY** each test case was chosen.

**Focus:** Quality over quantity - 8 Critical/High priority test cases with clear WHY explanations demonstrating test design skills.

---

## Test Case Summary

| ID | Title | Priority | Technique | Type | Defect Link |
|----|-------|----------|-----------|------|-------------|
| TC-FLT-CAT-001 | Popular filter works | Critical | EP | Functional | - |
| TC-FLT-CAT-002 | Trending filter works | Critical | EP | Functional | - |
| TC-PAG-001 | Navigate to page 2 | High | BVA | Functional | - |
| TC-PAG-002 | Last page boundary error | High | BVA | Negative | DEF-002 |
| TC-PAG-003 | Filter persists across pagination | High | Exploratory | Functional | DEF-003 |
| TC-NEG-001 | Direct URL access fails | High | Negative | Negative | DEF-001 |
| TC-NEG-002 | Invalid page number | High | BVA | Negative | - |
| TC-CMB-001 | Popular + Movies combined | High | Decision Table | Functional | - |

**Total:** 8 foundation test cases (all Critical/High priority)

---

## Category Filter Test Cases

### TC-FLT-CAT-001: Popular Filter Works

**Priority:** Critical
**Test Type:** Functional
**Design Technique:** Equivalence Partitioning (EP)
**Estimated Time:** 3 minutes
**Traceability:** FLT-CAT-1.1 (Requirements)

**WHY This Test Case?**
- **Primary user workflow** - Popular is the most commonly used filter (auto-loaded on homepage)
- **Core functionality** - If this fails, app is essentially broken for most users
- **Equivalence Partitioning** - Tests valid category filter (Popular = valid equivalence class)
- **Foundation test** - Other filter tests build on this pattern

**Preconditions:**
- Incognito/private browser window (fresh session, no cache)
- Site accessible at `https://tmdb-discover.surge.sh/`

**Test Steps:**
1. Navigate to `https://tmdb-discover.surge.sh/`
2. Observe that site auto-forwards to `/popular`
3. Verify "Popular" filter button is in active/selected state
4. Verify movie cards are displayed
5. Count number of movie results on page

**Expected Result:**
- Popular filter button shows active state (highlighted/selected)
- Movie grid displays 20 results (standard page size)
- Movie cards show title, image, and metadata
- Page title/heading indicates "Popular Movies"

**Test Data:**
- Base URL: `https://tmdb-discover.surge.sh/`
- Expected forward: `/popular`
- Expected result count: 20 movies per page

**Notes:**
- This validates the default user experience
- Success criteria: Filter active + results displayed
- Failure indicates critical issue affecting all users

---

### TC-FLT-CAT-002: Trending Filter Works

**Priority:** Critical
**Test Type:** Functional
**Design Technique:** Equivalence Partitioning (EP)
**Estimated Time:** 3 minutes
**Traceability:** FLT-CAT-1.2 (Requirements)

**WHY This Test Case?**
- **Second most common workflow** - Users frequently switch to Trending
- **Filter switching validation** - Tests that multiple filters work independently
- **Equivalence Partitioning** - Tests another valid category (Trending = same equivalence class as Popular)
- **State management** - Verifies app can change filter state correctly

**Preconditions:**
- Incognito/private browser window (fresh session, no cache)

**Test Steps:**
1. Navigate to `https://tmdb-discover.surge.sh/`
2. Click "Trending" filter button
3. Wait for page to reload/update
4. Verify "Trending" filter button is in active state
5. Verify "Popular" filter button is no longer active
6. Verify movie cards are displayed

**Expected Result:**
- Trending filter button shows active state
- Popular filter button returns to inactive state (only one active at a time)
- Movie grid displays 20 results
- Results are different from Popular filter (different trending movies)

**Test Data:**
- Filter to click: "Trending" button
- Expected result count: 20 movies
- Expected state: Only Trending active, Popular inactive

**Notes:**
- Validates filter exclusivity (only one category active at a time)
- Different results expected vs Popular (proves filter is working)
- Tests basic filter switching behavior

---

## Pagination Test Cases

### TC-PAG-001: Navigate to Page 2

**Priority:** High
**Test Type:** Functional
**Design Technique:** Boundary Value Analysis (BVA)
**Estimated Time:** 2 minutes
**Traceability:** PAG-1.1 (Requirements)

**WHY This Test Case?**
- **Essential navigation** - Users must paginate to browse results
- **Boundary Value Analysis** - Page 2 is first boundary (page 1 → page 2 transition)
- **Basic pagination** - Validates core pagination functionality works
- **Foundation for pagination testing** - Other pagination tests build on this

**Preconditions:**
- Incognito/private browser window
- On page 1 of any filter (e.g., Popular)

**Test Steps:**
1. Navigate to `https://tmdb-discover.surge.sh/popular`
2. Verify currently on page 1 (URL shows `/popular` or `/popular/1`)
3. Click "Next" button at bottom of page
4. Wait for navigation to complete
5. Verify URL changed to `/popular/2`
6. Verify movie results are different from page 1
7. Verify page indicator shows "Page 2"

**Expected Result:**
- URL changes to `/popular/2`
- Movie cards refresh with new set of 20 results
- Page indicator updates to show current page (2)
- "Previous" button becomes enabled
- "Next" button remains enabled (more pages available)

**Test Data:**
- Starting page: 1
- Target page: 2
- Expected URL: `/popular/2`
- Expected results: 20 movies (different from page 1)

**Notes:**
- Tests forward pagination (Next button)
- Page 2 is critical boundary (validates pagination works at all)
- Success enables testing higher page numbers

---

### TC-PAG-002: Last Page Boundary Error (Known Defect)

**Priority:** High
**Test Type:** Negative
**Design Technique:** Boundary Value Analysis (BVA)
**Estimated Time:** 3 minutes
**Traceability:** PAG-1.1, DEF-002 (Requirements, Defects)

**WHY This Test Case?**
- **Known defect reproduction** - Assignment disclosed this as known issue (DEF-002)
- **Boundary Value Analysis** - Last page is upper boundary (most likely to have off-by-one errors)
- **Negative testing** - Validates error handling at boundary
- **High user impact** - Users trying to browse all results hit this error

**Preconditions:**
- Incognito/private browser window
- Filter applied (e.g., Popular) to generate high page numbers

**Test Steps:**
1. Navigate to `https://tmdb-discover.surge.sh/`
2. Apply Popular filter (if not auto-applied)
3. Navigate to last pagination page (e.g., page 289)
   - Can jump directly via URL or click through pages
4. Click on the high page number link
5. Observe error screen

**Expected Result (DEFECT):**
- **Test SHOULD FAIL** - This is a known defect
- Error message: "Something went wrong - please try again later"
- Page fails to load results
- High page numbers (e.g., 289+) are symptom of bug when filtering

**Test Data:**
- Filter: Popular
- Page number: Last page (varies, typically 280-289 range)
- Expected: Error screen

**Notes:**
- Mark test as `@pytest.mark.xfail` (expected to fail)
- Validates that known defect still exists
- Screenshot on failure provides defect evidence
- High page numbers are symptom of filter + pagination interaction bug

---

### TC-PAG-003: Filter Persists Across Pagination (Defect Found)

**Priority:** High
**Test Type:** Functional (Defect)
**Design Technique:** Exploratory
**Estimated Time:** 3 minutes
**Traceability:** PAG-2.1, DEF-003 (Requirements, Defects)

**WHY This Test Case?**
- **Found during exploration** - New defect discovered (DEF-003)
- **Critical UX issue** - Users can't browse filtered results across pages
- **State management validation** - Tests filter persistence across navigation
- **Real-world scenario** - Users naturally paginate through filtered results

**Preconditions:**
- Incognito/private browser window

**Test Steps:**
1. Navigate to `https://tmdb-discover.surge.sh/`
2. Click "Popular" filter
3. Verify Popular filter is active (button highlighted)
4. Click "Next" button to navigate to page 2
5. Observe filter state after navigation
6. Verify Popular filter is still active

**Expected Result (DEFECT):**
- **Test SHOULD FAIL** - This is a newly found defect
- Popular filter SHOULD remain active on page 2
- URL SHOULD be `/popular/2` or similar
- Results SHOULD still be filtered Popular movies

**Actual Result (Bug):**
- Filter clears after pagination
- Shows unfiltered results on page 2
- Users lose their filter context

**Test Data:**
- Initial filter: Popular
- Action: Click Next to page 2
- Expected: Filter persists
- Actual: Filter lost

**Notes:**
- Mark as `@pytest.mark.xfail` (expected to fail)
- High impact - prevents users from browsing filtered results
- Demonstrates exploratory testing value (found defect formal techniques missed)

---

## Negative Test Cases

### TC-NEG-001: Direct URL Access Fails (Known Defect)

**Priority:** High
**Test Type:** Negative
**Design Technique:** Negative Testing
**Estimated Time:** 2 minutes
**Traceability:** FLT-CAT-1.1, DEF-001 (Requirements, Defects)

**WHY This Test Case?**
- **Known defect validation** - Assignment disclosed this as known issue (DEF-001)
- **Negative testing** - Tests error handling for invalid direct URLs
- **Equivalence Partitioning** - Direct URL = invalid equivalence class (vs valid UI navigation)
- **Bookmarking/sharing impact** - Users can't share or bookmark filtered views

**Preconditions:**
- Incognito/private browser window
- No previous session/cache

**Test Steps:**
1. Directly navigate to `https://tmdb-discover.surge.sh/popular` (paste URL in address bar)
2. Wait for page load
3. Observe page behavior

**Expected Result (DEFECT):**
- **Test SHOULD FAIL** - This is a known defect
- Page fails to load properly
- May show blank page or error
- SPA routing doesn't handle direct URL access

**Test Data:**
- Direct URL: `https://tmdb-discover.surge.sh/popular`
- Expected: Failure/blank page
- Root cause: Client-side routing issue

**Notes:**
- Mark as `@pytest.mark.xfail` (expected to fail)
- Demonstrates negative testing technique
- Different from DEF-005 (page refresh) - this is direct navigation
- Prevents bookmarking/sharing functionality

---

### TC-NEG-002: Invalid Page Number Handling

**Priority:** High
**Test Type:** Negative
**Design Technique:** Boundary Value Analysis (BVA)
**Estimated Time:** 2 minutes
**Traceability:** PAG-1.1 (Requirements)

**WHY This Test Case?**
- **Boundary Value Analysis** - Tests invalid boundary (page 0, negative pages)
- **Negative testing** - Validates error handling for invalid input
- **Edge case coverage** - Users might manually edit URL to invalid page
- **Graceful degradation** - App should handle invalid input gracefully

**Preconditions:**
- Incognito/private browser window

**Test Steps:**
1. Navigate to `https://tmdb-discover.surge.sh/popular`
2. Manually edit URL to `/popular/0` (page 0 - invalid)
3. Press Enter to navigate
4. Observe error handling

**Expected Result:**
- App should handle gracefully (one of):
  - Redirect to page 1
  - Show error message
  - Stay on current page
- Should NOT crash or show broken UI

**Test Data:**
- Invalid pages to test:
  - Page 0: `/popular/0`
  - Negative page: `/popular/-1`
  - Non-numeric: `/popular/abc`
- Expected: Graceful error handling

**Notes:**
- Validates input validation and error handling
- Multiple invalid inputs test robustness
- May pass or fail depending on implementation

---

## Combined Filter Test Cases

### TC-CMB-001: Popular + Movies Type Filter Combined

**Priority:** High
**Test Type:** Functional
**Design Technique:** Decision Table
**Estimated Time:** 3 minutes
**Traceability:** FLT-CAT-1.1, FLT-TYP-1.1 (Requirements)

**WHY This Test Case?**
- **Decision Table technique** - Tests combination of two filters (Category + Type)
- **Real-world usage** - Users commonly apply multiple filters together
- **Filter interaction** - Validates filters work together correctly (not just individually)
- **State management** - Tests multiple filter state persistence

**Preconditions:**
- Incognito/private browser window

**Test Steps:**
1. Navigate to `https://tmdb-discover.surge.sh/`
2. Click "Popular" filter (if not auto-applied)
3. Locate Type filter (Movies/TV Shows dropdown or buttons)
4. Select "Movies" type filter
5. Verify both filters are active
6. Verify results are filtered correctly

**Expected Result:**
- Popular filter button shows active state
- Movies type filter shows active state
- Results show only Popular Movies (not TV shows)
- Result count shows movies matching both filters
- Both filters persist together

**Test Data:**
- Category filter: Popular
- Type filter: Movies
- Expected: Intersection of both filters (Popular AND Movies)

**Decision Table:**
| Category | Type | Expected Results |
|----------|------|-----------------|
| Popular | Movies | Popular movies only |
| Popular | TV Shows | Popular TV shows only |
| Trending | Movies | Trending movies only |

**Notes:**
- Tests filter combination logic (AND operation)
- Validates multiple filter state management
- Could expand to 3+ filter combinations (out of scope for foundation)
- Demonstrates decision table test design technique

---

## Test Execution Notes

### Defect-Related Tests

Tests marked with `@pytest.mark.xfail` (expected to fail):
- TC-PAG-002: Last page boundary error (DEF-002)
- TC-PAG-003: Filter persistence (DEF-003)
- TC-NEG-001: Direct URL access (DEF-001)

These tests **SHOULD FAIL** to validate that known defects still exist.

### Test Data Management

All tests use **fresh browser context** (incognito mode via Playwright):
- No shared cookies between tests
- No localStorage/sessionStorage carryover
- Each test starts with clean slate
- Reproducible results

### Logging Strategy

Each test logs (using lazy % formatting):
```python
logger.info("Test started: %s", test_case_id)
logger.info("Navigating to URL: %s", url)
logger.info("Applying filter: %s", filter_name)
logger.debug("Validating result count: %d", count)
logger.exception("Test failed with error")
```

### Screenshot Capture

Playwright captures screenshot on failure:
- Saved to `screenshots/{test_name}_{timestamp}.png`
- Provides visual evidence for defects
- Useful for debugging test failures

---

## Traceability Matrix

| Test Case | Requirement | Defect | Priority | Status |
|-----------|-------------|--------|----------|--------|
| TC-FLT-CAT-001 | FLT-CAT-1.1 | - | Critical | ✅ Spec complete |
| TC-FLT-CAT-002 | FLT-CAT-1.2 | - | Critical | ✅ Spec complete |
| TC-PAG-001 | PAG-1.1 | - | High | ✅ Spec complete |
| TC-PAG-002 | PAG-1.1 | DEF-002 | High | ✅ Spec complete |
| TC-PAG-003 | PAG-2.1 | DEF-003 | High | ✅ Spec complete |
| TC-NEG-001 | FLT-CAT-1.1 | DEF-001 | High | ✅ Spec complete |
| TC-NEG-002 | PAG-1.1 | - | High | ✅ Spec complete |
| TC-CMB-001 | FLT-CAT-1.1, FLT-TYP-1.1 | - | High | ✅ Spec complete |

**Coverage:**
- Requirements: 5 unique requirements covered
- Defects: 3 defects reproducible via tests
- Priority: 2 Critical + 6 High = 8 foundation test cases
- Test techniques: EP, BVA, Negative, Decision Table, Exploratory

---

## Future Expansion (Deferred)

Additional test cases if time permits (post-submission):

| ID | Title | Priority | Effort |
|----|-------|----------|--------|
| TC-FLT-CAT-003 | Newest filter works | Medium | 10 min |
| TC-FLT-CAT-004 | Top Rated filter works | Medium | 10 min |
| TC-PAG-004 | Previous button navigation | Medium | 10 min |
| TC-PAG-005 | Jump to specific page | Medium | 15 min |
| TC-SRH-001 | Search by title | Medium | 15 min |
| TC-FLT-YR-001 | Year filter (2020-2025) | Medium | 15 min |
| TC-FLT-RT-001 | Rating filter (7.5+) | Medium | 15 min |
| TC-CMB-002 | Trending + TV Shows + 2024 | Low | 20 min |

**Total deferred effort:** ~2 hours (15 additional test cases)

---

## References

- [Test Strategy](test-strategy.md) - Overall testing approach and rationale
- [Requirements](requirements.md) - Reverse-engineered requirements with traceability IDs
- [Defects](defects-manual-found.md) - Bug reports with reproduction steps and screenshots
- [Design Decisions](design-decisions.md) - Technical decisions and alternatives
