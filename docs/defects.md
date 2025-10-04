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
| DEF-002 | Last pagination pages broken | High | Known |
| DEF-003 | Filter lost after pagination | High | New |
| DEF-004 | Pagination skips pages at boundaries | Medium | New |
| DEF-005 | Page refresh loses state | Medium | New |
| DEF-006 | Outrageous page numbers displayed | Medium | New |

**Total:** 6 defects (2 known + 4 new) ✅

---

## Defects

### DEF-001: Direct URL Access Fails

**Severity:** High
**Found:** Known issue from assignment

**Steps:**
1. Navigate directly to `https://tmdb-discover.surge.sh/popular`
2. Observe page fails to load properly

**Expected:** Should load Popular filter view
**Actual:** Page fails or shows blank

**Note:** Assignment disclosed this as known issue

---

### DEF-002: Last Pagination Pages Broken

**Severity:** High
**Found:** Known issue from assignment

**Steps:**
1. Navigate to site
2. Go to last few pages (280+)
3. Try to load page

**Expected:** Should load results
**Actual:** Pages fail to load

**Note:** Assignment disclosed this as known issue

---

### DEF-003: Filter Lost After Pagination

**Severity:** High
**Found:** Exploratory testing

**Steps:**
1. Click "Popular" filter
2. Click "Next" to go to page 2
3. Observe filter state

**Expected:** Popular filter should persist on page 2
**Actual:** Filter clears, shows unfiltered results

**Impact:** Users can't browse filtered results across pages

---

### DEF-004: Pagination Skips Pages at Boundaries

**Severity:** Medium
**Found:** Exploratory testing

**Steps:**
1. Navigate to last page (e.g., 289)
2. Click "Previous" button
3. Observe page number

**Expected:** Should go to page 288
**Actual:** Skips from 289 to 287 (bypasses 288)

**Screenshot:** `docs/images/BugPagination_outragousPageNum_2of2.png`

**Note:** From your exploration - "Previous 123...287 288 289 Next" skips 288

---

### DEF-005: Page Refresh Loses State

**Severity:** Medium
**Found:** Exploratory testing

**Steps:**
1. Apply any filter (e.g., Popular)
2. Press F5 or refresh browser
3. Observe state

**Expected:** Filter should persist after refresh
**Actual:** Page resets, filter is lost

**Screenshot:** `docs/images/BugPageRefresh_1of1.png`

**Impact:** Users can't bookmark or refresh filtered views

---

### DEF-006: Outrageous Page Numbers Displayed

**Severity:** Medium
**Found:** Exploratory testing

**Steps:**
1. Apply specific filter combination (details in screenshot)
2. Navigate to last page
3. Observe page number displayed

**Expected:** Reasonable page count (e.g., 1-300)
**Actual:** Shows extremely large/impossible page numbers

**Screenshot:** `docs/images/BugPagination_outragousPageNum_2of2.png`

**Result:** Clicking on that page shows "something went wrong - please try again later"

**Note:** From your notes - outrageous page number then error on click

---

## Test Environment

- **Browser:** Chrome/Firefox
- **OS:** Ubuntu 24.04
- **Date:** 2025-10-04

---

## Notes

All screenshots stored in `docs/images/`

**Assignment requirement:** 5+ defects ✅
**Found:** 6 defects (exceeds minimum)
- Known issues: 2
- New defects: 4 (exceeds minimum 3)
