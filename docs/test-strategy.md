# Test Strategy

**Project:** movie_db_qa - QA Automation for TMDB Discovery App
**Version:** 1.0
**Last Updated:** 2025-10-04
**Status:** ✅ Complete

---

## Overview

**Approach:** Risk-based test prioritization using formal test design techniques

This strategy focuses on **quality over quantity** - implementing a foundation of 8-10 Critical/High priority test cases that demonstrate QA thinking and test design skills, rather than exhaustive coverage.

**Philosophy:** "Small scope, deep quality" - Better to have 10 well-designed tests with clear WHY explanations than 50 shallow tests.

---

## Testing Objectives

### Primary Goals

1. **Validate core user workflows** - Ensure primary features (Popular/Trending filters, pagination) work correctly
2. **Verify known issues** - Reproduce and document the 2 disclosed defects (DEF-001, DEF-002)
3. **Demonstrate test design skills** - Apply BVA, EP, and negative testing techniques
4. **Find new defects** - Exploratory testing to discover additional issues beyond known bugs

### Success Criteria

- ✅ All 8-10 foundation test cases implemented and passing (or intentionally failing for known defects)
- ✅ Each test case has clear WHY explanation showing test design rationale
- ✅ Known defects (DEF-001, DEF-002) are reproducible via automated tests
- ✅ Test execution generates HTML reports with screenshots on failure
- ✅ Code quality gates pass (ruff, mypy, 100% of test code covered)

---

## Scope

### In Scope - FOUNDATION (8-10 test cases)

**Priority:** Critical + High only

| Feature Area | Test Cases | Priority | Rationale |
|--------------|------------|----------|-----------|
| **Category Filters** | 2-3 tests | Critical | Primary user workflow - Popular, Trending filters |
| **Pagination** | 2-3 tests | High | Essential navigation - forward/backward, boundaries |
| **Negative Testing** | 2 tests | High | Known defects - DEF-001 (direct URL), DEF-002 (last page) |
| **Combined Filters** | 1-2 tests | High | Real-world usage - filter combinations |

**Features to Test:**
- ✅ Popular filter (most common user action)
- ✅ Trending filter (second most common)
- ✅ Pagination navigation (Next/Previous buttons)
- ✅ Pagination boundaries (last page - known defect)
- ✅ Direct URL access (known defect)
- ✅ Combined filters (e.g., Popular + Movies type)

### Out of Scope - DEFERRED

**Priority:** Medium + Low (defer to post-submission if time permits)

| Feature/Area | Reason for Exclusion | Effort Estimate |
|--------------|---------------------|-----------------|
| Year/Rating/Genre filters | Medium priority, not core workflow | 3-4 hours (10+ tests) |
| Type filter (Movies/TV Shows) | Already covered in combined filter test | 1 hour (2 tests) |
| Search functionality | Medium priority, separate feature | 2 hours (5 tests) |
| Cross-browser testing | Chrome only for foundation | 2 hours setup |
| Mobile/Responsive testing | Not assignment requirement | 4 hours |
| Performance testing | Not assignment requirement | 6 hours |
| Accessibility testing | Not assignment requirement | 8 hours |
| API data accuracy | No backend access to verify TMDB API | N/A |

**Rationale for Exclusions:**
- **Time constraint:** 1.5 days remaining, focus on demonstrating skills not exhaustive coverage
- **Assignment scope:** Foundation over expansion - quality explanations matter more than test count
- **Diminishing returns:** 10 well-designed tests > 50 shallow tests

---

## Test Design Techniques

### Techniques Applied

| Technique | Definition | Application in This Project |
|-----------|------------|------------------------------|
| **Boundary Value Analysis (BVA)** | Test at boundaries of input ranges | Pagination: first page, last page, invalid page numbers |
| **Equivalence Partitioning (EP)** | Divide inputs into valid/invalid classes | Filters: valid categories (Popular, Trending) vs invalid direct URLs |
| **Decision Tables** | Test combinations of inputs | Combined filters: Category + Type combinations |
| **Negative Testing** | Test error handling and edge cases | Direct URL access (DEF-001), last page error (DEF-002) |
| **Exploratory Testing** | Ad-hoc testing to find unexpected issues | Found 3 new defects (DEF-003, DEF-004, DEF-005) during exploration |

### WHY These Techniques?

**Boundary Value Analysis:**
- Pagination is a perfect BVA candidate (page 1, page N, page N+1)
- Catches off-by-one errors (common in pagination logic)
- DEF-002 (last page broken) found via BVA thinking

**Equivalence Partitioning:**
- Filter types: Valid (Popular, Trending, Newest, Top Rated) vs Invalid (direct URLs)
- Reduces test count while maintaining coverage
- Tests representative samples from each equivalence class

**Decision Tables:**
- Combined filters have multiple inputs (Category, Type, Year, Rating, Genre)
- Decision table ensures we test key combinations
- Example: Popular + Movies, Trending + TV Shows

**Negative Testing:**
- Both known defects (DEF-001, DEF-002) are negative scenarios
- Validates error handling and edge cases
- Ensures app fails gracefully

**Exploratory Testing:**
- Found defects formal techniques missed:
  - DEF-003: Filter lost after pagination
  - DEF-004: Pagination skips pages at boundaries
  - DEF-005: Page refresh loses state
- Complements structured testing with ad-hoc discovery

---

## Risk Assessment

### High Risk Areas (Test First)

| Risk Area | Impact | Likelihood | Priority | Mitigation |
|-----------|--------|------------|----------|------------|
| **Category filters broken** | High | Medium | Critical | Test Popular/Trending filters first |
| **Pagination fails** | High | High | Critical | BVA on boundaries, test navigation |
| **Known defects** | High | Certain | High | Negative tests for DEF-001, DEF-002 |
| **State management issues** | Medium | Medium | High | Test filter persistence across actions |

### Low Risk Areas (Defer)

- Advanced filters (Year, Rating, Genre) - less frequently used
- Search functionality - separate from core discovery workflow
- UI polish and edge cases - low business impact

---

## Test Environment

### Browser Contexts

**Precondition for ALL tests:** Incognito/private browser window (fresh session, no cache)

**Rationale:**
- Playwright's `new_context()` provides isolated browser context (= incognito mode)
- No shared state between tests (cookies, localStorage, sessionStorage)
- Reproducible defects - each test starts with clean slate
- Matches manual testing preconditions in defect reports

### Configuration

| Component | Value | Source |
|-----------|-------|--------|
| Browser | Chromium | `config.browser` |
| Headless | True (CI), False (local debug) | `config.headless` |
| Viewport | 1920x1080 | `conftest.py` context fixture |
| Timeout | 30000ms | `config.timeout` |
| Base URL | https://tmdb-discover.surge.sh | `DiscoverPage.BASE_URL` |

---

## Test Execution Strategy

### Execution Order

1. **Sanity tests** - Verify framework works (existing `test_sanity.py`)
2. **Category filter tests** - Core functionality (TC-FLT-CAT-001, TC-FLT-CAT-002)
3. **Pagination tests** - Essential navigation (TC-PAG-001, TC-PAG-002, TC-PAG-003)
4. **Negative tests** - Known defects (TC-NEG-001, TC-NEG-002)
5. **Combined filter tests** - Real-world scenarios (TC-CMB-001)

### Defect Handling

| Defect | Test Case | Expected Behavior |
|--------|-----------|-------------------|
| DEF-001: Direct URL fails | TC-NEG-001 | Test SHOULD FAIL (validates defect exists) |
| DEF-002: Last page broken | TC-NEG-002 | Test SHOULD FAIL (validates defect exists) |
| DEF-003: Filter lost | TC-PAG-003 | Test SHOULD FAIL (new defect found) |

**Strategy:** Use `@pytest.mark.xfail` for known defects to document expected failures

---

## API Validation Strategy

### Approach: Playwright Network Interception

**Tool:** Playwright's `page.on("request")` event handler

**Implementation:**
```python
# tests/conftest.py - Automatic capture for all tests
def handle_request(request):
    if "api.themoviedb.org" in request.url:
        api_calls.append({
            "url": request.url,
            "method": request.method,
            "resource_type": request.resource_type
        })
        logger.info("API call captured: %s %s", request.method, request.url)

page.on("request", handle_request)
page.api_calls = api_calls  # Attach to page for test access
```

### Validated Endpoints

| Test Case | API Endpoint Validated | Query Parameters |
|-----------|------------------------|------------------|
| TC-FLT-CAT-001 | `/movie/popular` | `page=1`, `api_key` |
| TC-FLT-CAT-002 | `/movie/trending` | Filter change detection |
| TC-PAG-001 | `/movie/popular` | `page=2` (pagination) |

### What We Validate

1. **Correct endpoint called** - Verify UI action triggers expected API call
2. **Query parameters present** - Ensure page numbers, filters passed correctly
3. **API call timing** - Detect unnecessary duplicate calls

### Benefits

- **UI-API integration testing** - Catch mismatches between frontend and backend
- **Regression detection** - API calls logged in test execution log
- **Defect evidence** - Failed tests show what API calls were (or weren't) made

---

## Logging Strategy

### What to Log

| Event | Log Level | Example |
|-------|-----------|---------|
| Test start/end | INFO | `logger.info("Test started: %s", test_name)` |
| Page navigation | INFO | `logger.info("Navigating to URL: %s", url)` |
| Filter applied | INFO | `logger.info("Applied filter: %s", filter_name)` |
| Assertion validation | DEBUG | `logger.debug("Validating result count: %d", count)` |
| Error/Exception | ERROR | `logger.exception("Test failed with error")` |

### Lazy % Formatting (MANDATORY)

**✅ CORRECT:**
```python
logger.info("User %s applied filter %s at page %d", username, filter_name, page_num)
```

**❌ WRONG:**
```python
logger.info(f"User {username} applied filter {filter_name} at page {page_num}")
```

**WHY:** Lazy formatting only evaluates arguments if log level is enabled (performance)

---

## Reporting

### Reports Generated

| Report Type | Tool | Output Location | Purpose |
|-------------|------|-----------------|---------|
| **HTML Report** | pytest-html | `htmlcov/index.html` | Human-readable test results |
| **Coverage Report** | pytest-cov | `htmlcov/` | Code coverage metrics |
| **Console Output** | pytest | stdout | Quick feedback during development |
| **Screenshots** | playwright | `screenshots/` (on failure) | Visual defect evidence |

### Metrics Tracked

- ✅ Test pass/fail count
- ✅ Code coverage percentage (target: 100% of test code)
- ✅ Test execution time
- ✅ Defects found vs reproduced

---

## Continuous Integration

### CI Pipeline (GitHub Actions)

**Quality Gates:**
1. Ruff linting (format + lint)
2. MyPy type checking
3. Black formatting verification
4. Pytest test execution
5. Coverage report generation

**Triggers:**
- Push to `main`, `develop`, `feature/*` branches
- Pull requests to `main`, `develop`

**Status:** ✅ CI workflow fixed (`.github/workflows/ci.yml` - Python 3.13)

---

## References

- [Test Cases](test-cases.md) - Detailed test specifications
- [Requirements](requirements.md) - Reverse-engineered requirements
- [Defects](defects-manual-found.md) - Bug reports with evidence
- [Design Decisions](design-decisions.md) - Technical rationale

---

## Appendix: Test Prioritization Matrix

| Test Case ID | Feature | Priority | Technique | Effort | Value |
|--------------|---------|----------|-----------|--------|-------|
| TC-FLT-CAT-001 | Popular filter | Critical | EP | Low | High |
| TC-FLT-CAT-002 | Trending filter | Critical | EP | Low | High |
| TC-PAG-001 | Navigate page 2 | High | BVA | Low | High |
| TC-PAG-002 | Last page boundary | High | BVA | Low | High |
| TC-PAG-003 | Filter persistence | High | Exploratory | Medium | High |
| TC-NEG-001 | Direct URL (DEF-001) | High | Negative | Low | High |
| TC-NEG-002 | Last page (DEF-002) | High | Negative | Low | High |
| TC-CMB-001 | Popular + Movies | High | Decision Table | Medium | Medium |

**Foundation Score:** 8 test cases × High value = Strong demonstration of test design skills
