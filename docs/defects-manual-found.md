# Defect Report

**Project:** movie_db_qa
**App:** https://tmdb-discover.surge.sh/
**Date:** 2025-10-04
**Tester:** QA Engineer

---

## Summary

| ID | Title | Severity | Status |
|----|-------|----------|--------|
| DEF-001 | Direct URL access fails | High | Known |
| DEF-002 | Filter + Last page pagination broken | High | Known |
| DEF-003 | Filter lost after pagination | High | New |
| DEF-004 | Pagination skips pages at boundaries | Medium | New |
| DEF-005 | Page refresh loses state | Medium | New |

**Total:** 5 defects (2 known + 3 new) ✅

---

## Defects

### DEF-001: Direct URL Access Fails

**Severity:** High
**Found:** Known issue from assignment

**Preconditions:** Incognito/private browser window (fresh session, no cache)

**Steps:**
1. Navigate directly to `https://tmdb-discover.surge.sh/popular`
2. Observe page fails to load properly

**Expected:** Should load Popular filter view
**Actual:** Page fails or shows blank

**Note:** Assignment disclosed this as known issue

---

### DEF-002: Filter + Last Page Pagination Broken

**Severity:** High
**Found:** Known issue from assignment

**Preconditions:** Incognito/private browser window (fresh session, no cache)

**Steps:**
1. Navigate to `https://tmdb-discover.surge.sh/`
2. Apply any filter (e.g., Popular, Trending)
3. Navigate to last pagination page
4. Click on the high page number
5. Observe error screen

**Expected:** Should load filtered results for that page
**Actual:** "Something went wrong - please try again later" error

**Screenshot:**
<img src="images/BugPagination_outragousPageNum_2of2.png" alt="Pagination error with high page numbers" width="50%">

**Note:** Assignment disclosed this as known issue. The high page numbers (e.g., 289) are a symptom of this bug when filtering is applied.

---

### DEF-003: Filter Lost After Pagination

**Severity:** High
**Found:** Exploratory testing

**Preconditions:** Incognito/private browser window (fresh session, no cache)

**Steps:**
1. Navigate to `https://tmdb-discover.surge.sh/`
2. Click "Popular" filter
3. Click "Next" to go to page 2
4. Observe filter state

**Expected:** Popular filter should persist on page 2
**Actual:** Filter clears, shows unfiltered results

**Impact:** Users can't browse filtered results across pages

---

### DEF-004: Pagination Skips Pages at Boundaries

**Severity:** Medium
**Found:** Exploratory testing

**Preconditions:** Incognito/private browser window (fresh session, no cache)

**Steps:**
1. Navigate to `https://tmdb-discover.surge.sh/`
2. Navigate to last page (e.g., page 289)
3. Click "Previous" button
4. Observe page number

**Expected:** Should go to page 288
**Actual:** Skips from 289 to 287 (bypasses 288)

**Screenshot:**
<img src="images/BugPagination_outragousPageNum_2of2.png" alt="Pagination skipping pages at boundaries" width="50%">

**Note:** From your exploration - "Previous 123...287 288 289 Next" skips 288

---

### DEF-005: Page Refresh Loses State

**Severity:** Medium
**Found:** Exploratory testing

**Preconditions:** Incognito/private browser window (fresh session, no cache)

**Steps:**
1. Navigate to `https://tmdb-discover.surge.sh/`
2. Site auto-forwards to `https://tmdb-discover.surge.sh/popular`
3. Press F5 to refresh browser
4. Observe state

**Expected:** Popular filter should persist after refresh (URL should stay at `/popular`)
**Actual:** Page resets to base URL `/`, filter is lost

**Screenshot:**
<img src="images/BugPageRefresh_1of1.png" alt="Page refresh loses filter state" width="50%">

**Impact:** Users can't bookmark or refresh filtered views

---

## Test Environment

- **Browser:** Chrome/Firefox
- **OS:** Ubuntu 24.04
- **Date:** 2025-10-04

---

## Notes

All screenshots stored in `docs/images/`

**Assignment requirement:** 5+ defects ✅
**Found:** 5 defects (meets minimum)
- Known issues: 2
- New defects: 3 (meets minimum)
