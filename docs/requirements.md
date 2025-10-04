# TMDB Discovery - Reverse-Engineered Requirements

**Project:** movie_db_qa - QA Automation Assignment
**Application Under Test:** https://tmdb-discover.surge.sh/
**Version:** Demo Site (No Version Info Available)
**Date:** 2025-10-04
**Author:** QA Engineer (Reverse-Engineered from Observation)

---

## Requirement ID Naming Convention

**Format:** `[FEATURE]-[COMPONENT]-[NUMBER]`

**Feature Codes:**
- **FLT** = Filtering (Category, Type, Metadata)
  - **FLT-CAT** = Category Filters (Popular, Trending, Newest, Top Rated)
  - **FLT-TYP** = Type Filter (Movies/TV Shows)
  - **FLT-YR** = Year Filter
  - **FLT-RAT** = Rating Filter
  - **FLT-GEN** = Genre Filter
  - **FLT-CMB** = Combined Filters
- **SRH** = Search Functionality
- **PAG** = Pagination
- **URL** = URL State Management
- **NFR** = Non-Functional Requirements
- **KI** = Known Issues (From Assignment)

**Examples:**
- `FLT-CAT-1.1` = Filter > Category > Popular Filter
- `SRH-1.1` = Search > Title Search
- `PAG-2.1` = Pagination > Filter Persistence
- `URL-2.1` = URL Management > Direct URL Access

**Benefits:**
- Self-documenting (easy to understand at a glance)
- Logical grouping (all FLT-CAT together)
- Easier traceability to test cases
- More maintainable than generic FR-1, FR-2 numbering

---

## Document Purpose

**Context:** This assignment provides no formal requirements documentation.

**Approach:** This document captures **observed behavior** and **reasonable user expectations**
based on:
- Manual exploration of the application
- Industry-standard UX patterns (IMDb, Netflix, Amazon)
- Web usability best practices
- Known issues disclosed in assignment

**Status:** These are **ASSUMED REQUIREMENTS** based on observation, not official specifications.

**Risk:** Cannot validate business logic correctness or data accuracy without ground truth.

---

## Application Overview

**Purpose:** Movie and TV show discovery platform (similar to IMDb)

**Core Features:**
- Browse content by category (Popular, Trending, Newest, Top Rated)
- Search by title
- Filter by type (Movies vs TV Shows)
- Filter by metadata (Year, Rating, Genre)
- Paginate through results

---

## Functional Requirements

### FLT-CAT: Category Filtering

**FLT-CAT-1.1: Popular Filter**
- **Requirement:** User can filter content to show "Popular" items
- **Expected Behavior:**
  - Click "Popular" button/link
  - Results display movies/shows marked as popular
  - URL reflects filter state (e.g., `?category=popular`)
  - Results differ from other categories
- **Assumption:** Based on standard filtering UX patterns
- **Priority:** High (Core feature)

**FLT-CAT-1.2: Trending Filter**
- **Requirement:** User can filter content to show "Trending" items
- **Expected Behavior:**
  - Click "Trending" button/link
  - Results display trending content
  - URL reflects filter state
  - Results differ from Popular
- **Assumption:** Based on standard filtering UX patterns
- **Priority:** High (Core feature)

**FLT-CAT-1.3: Newest Filter**
- **Requirement:** User can filter content to show newest releases
- **Expected Behavior:**
  - Click "Newest" button/link
  - Results display recently released content
  - URL reflects filter state
  - Results differ from other categories
- **Assumption:** Based on standard filtering UX patterns
- **Priority:** High (Core feature)

**FLT-CAT-1.4: Top Rated Filter**
- **Requirement:** User can filter content by highest ratings
- **Expected Behavior:**
  - Click "Top Rated" button/link
  - Results display highly-rated content
  - URL reflects filter state
  - Results differ from other categories
- **Assumption:** Based on standard filtering UX patterns
- **Priority:** High (Core feature)

---

### SRH: Search Functionality

**SRH-1.1: Title Search**
- **Requirement:** User can search for content by title
- **Expected Behavior:**
  - Enter search term in search field
  - Results filter to titles containing search term
  - Search should be case-insensitive (UX best practice)
  - Empty search shows all results
- **Assumption:** Based on standard search UX (Google, Amazon, IMDb)
- **Priority:** Critical (Primary discovery method)

**SRH-1.2: Search Results Validation**
- **Requirement:** Search results match search criteria
- **Expected Behavior:**
  - All displayed titles contain search term
  - No irrelevant results shown
  - Results update dynamically or on submit
- **Assumption:** Standard search behavior
- **Priority:** Critical

---

### FLT-TYP: Type Filtering

**FLT-TYP-1.1: Movies vs TV Shows Filter**
- **Requirement:** User can filter between Movies and TV Shows
- **Expected Behavior:**
  - Select "Movies" → Only movies displayed
  - Select "TV Shows" → Only TV shows displayed
  - Filter state reflected in URL
  - Filter persists across pagination
- **Assumption:** Based on IMDb-like filtering
- **Priority:** High

---

### FLT-META: Metadata Filters

**FLT-YR-1.1: Year of Release Filter**
- **Requirement:** User can filter content by release year
- **Expected Behavior:**
  - Select year range or specific year
  - Results filtered to selected year(s)
  - Boundary values handled correctly (min/max years)
- **Assumption:** Standard filtering pattern
- **Priority:** Medium

**FLT-RAT-1.1: Rating Filter**
- **Requirement:** User can filter by rating threshold
- **Expected Behavior:**
  - Select rating range (e.g., 7.0+)
  - Results filtered to match criteria
  - Boundary values handled (0-10 scale assumed)
- **Assumption:** Standard TMDB/IMDb rating scale
- **Priority:** Medium

**FLT-GEN-1.1: Genre Filter**
- **Requirement:** User can filter by genre (Action, Comedy, etc.)
- **Expected Behavior:**
  - Select genre(s)
  - Results filtered to selected genre(s)
  - Multiple genres should work (AND/OR logic unclear)
- **Assumption:** Standard genre filtering
- **Priority:** Medium

---

### PAG: Pagination

**PAG-1.1: Page Navigation**
- **Requirement:** User can navigate through paginated results
- **Expected Behavior:**
  - Click "Next" advances to next page
  - Click "Previous" goes back
  - Page number displayed and accurate
  - URL updates with page parameter
- **Assumption:** Standard pagination UX
- **Priority:** High (Core navigation)

**PAG-2.1: Filter Persistence Across Pagination**
- **Requirement:** Applied filters persist when navigating pages
- **Expected Behavior:**
  - Apply filter (e.g., Popular)
  - Navigate to page 2
  - Filter remains active
  - Results on page 2 still filtered
- **Assumption:** Industry standard (Amazon, Netflix, IMDb all do this)
- **Priority:** High (Critical UX)
- **⚠️ DEFECT FOUND:** This does NOT work (DEF-003)

**PAG-2.2: Pagination Boundary Handling**
- **Requirement:** Pagination handles first/last page correctly
- **Expected Behavior:**
  - "Previous" disabled on page 1
  - "Next" disabled on last page
  - No index errors at boundaries
- **Assumption:** Standard pagination behavior
- **Priority:** Medium
- **⚠️ DEFECT FOUND:** Index errors at last page (DEF-004)

---

### URL: URL State Management

**URL-1.1: URL Reflects Application State**
- **Requirement:** Current filters/page reflected in URL
- **Expected Behavior:**
  - URL parameters show active filters
  - URL shows current page number
  - URL is bookmarkable
- **Assumption:** RESTful web standards
- **Priority:** High (Shareability, bookmarking)

**URL-2.1: Direct URL Access**
- **Requirement:** User can access filtered views via direct URL
- **Expected Behavior:**
  - Navigate to `/popular` → Popular filter applied
  - Navigate to `?page=2` → Page 2 loaded
  - State matches URL parameters
- **Assumption:** Standard web behavior
- **Priority:** High
- **⚠️ KNOWN ISSUE:** Direct URL access fails (DEF-001 - disclosed in assignment)

**URL-2.2: Browser Refresh Preserves State**
- **Requirement:** Refreshing page preserves filters/page
- **Expected Behavior:**
  - Apply filters
  - Refresh browser (F5)
  - Filters remain active
- **Assumption:** Standard web application behavior
- **Priority:** Medium
- **⚠️ DEFECT FOUND:** Refresh loses state (DEF-005)

---

### FLT-CMB: Combined Filters

**FLT-CMB-1.1: Multiple Filters Applied Together**
- **Requirement:** User can apply multiple filters simultaneously
- **Expected Behavior:**
  - Apply Category + Type + Year (e.g., Popular + Movies + 2020)
  - Results match ALL criteria (AND logic assumed)
  - Filters clearly indicated in UI
- **Assumption:** Advanced filtering capability (Amazon-like)
- **Priority:** Medium

---

## Non-Functional Requirements

### NFR-1: Performance

**NFR-1.1: Page Load Time**
- **Requirement:** Pages load within acceptable time
- **Expected Behavior:** < 3 seconds (industry standard)
- **Priority:** Medium
- **Note:** Cannot measure without baseline

### NFR-2: Usability

**NFR-2.1: Intuitive UI**
- **Requirement:** Users can discover features without documentation
- **Expected Behavior:** Standard UI patterns, clear labels
- **Priority:** High

**NFR-2.2: Responsive Feedback**
- **Requirement:** UI provides feedback on actions
- **Expected Behavior:** Loading indicators, state changes visible
- **Priority:** Medium

### NFR-3: Browser Compatibility

**NFR-3.1: Cross-Browser Support**
- **Requirement:** Works on major browsers
- **Expected Behavior:** Chrome, Firefox, Safari, Edge support
- **Priority:** High
- **Note:** Testing Chrome/Firefox only (scope limitation)

---

## Known Issues (From Assignment)

### KI-1: Direct URL Slug Access Fails
- **Description:** Accessing specific slugs (e.g., `/popular`) doesn't work as expected
- **Source:** Assignment document
- **Priority:** High
- **Test Case:** TC-007 (Negative test)
- **Defect:** DEF-001

### KI-2: Last Pagination Pages Broken
- **Description:** Last few pagination pages don't function properly
- **Source:** Assignment document
- **Priority:** High
- **Test Case:** TC-006 (Boundary test)
- **Defect:** DEF-002

---

## Out of Scope (Cannot Test Without Ground Truth)

### Data Accuracy
- ❌ Cannot verify if "Popular" rankings are correct
- ❌ Cannot validate if "Trending" matches TMDB API
- ❌ Cannot confirm release years are accurate
- ❌ Cannot validate ratings against source data

**Rationale:** No access to backend, API, or source data. Testing UI behavior only.

### Business Logic
- ❌ Cannot verify ranking algorithms
- ❌ Cannot validate filtering logic against spec (no spec exists)
- ❌ Cannot confirm data freshness

**Rationale:** No business requirements document provided.

---

## Requirements Traceability Matrix

| Requirement ID | Feature | Test Case(s) | Priority | Status |
|----------------|---------|--------------|----------|--------|
| FLT-CAT-1.1 | Popular Filter | TC-FLT-CAT-001 | High | ✅ Testable |
| FLT-CAT-1.2 | Trending Filter | TC-FLT-CAT-002 | High | ✅ Testable |
| SRH-1.1 | Title Search | TC-SRH-001 | Critical | ✅ Testable |
| PAG-1.1 | Pagination Navigation | TC-PAG-001, TC-PAG-002 | High | ✅ Testable |
| PAG-2.1 | Filter Persistence | TC-PAG-003 | High | ❌ FAILS (DEF-003) |
| PAG-2.2 | Boundary Handling | TC-PAG-004 | Medium | ❌ FAILS (DEF-004) |
| URL-2.1 | Direct URL Access | TC-URL-001 | High | ❌ FAILS (DEF-001) |
| URL-2.2 | Refresh State | TC-URL-002 | Medium | ❌ FAILS (DEF-005) |
| FLT-CMB-1.1 | Combined Filters | TC-FLT-CMB-001 | Medium | 🔍 To Test |

---

## Assumptions & Risks

### Assumptions Made

1. **Industry Standards Apply:**
   - Filtering patterns follow IMDb/Netflix conventions
   - Search is case-insensitive (UX best practice)
   - URLs should be RESTful and bookmarkable

2. **User Expectations:**
   - Filters persist across pagination (critical UX)
   - State survives browser refresh (standard web behavior)
   - Boundary conditions handled gracefully (no crashes)

3. **Scope:**
   - Testing UI functionality, not data accuracy
   - Desktop web only (not mobile responsive)
   - Chrome/Firefox only (not full cross-browser)

### Risks

1. **No Ground Truth:**
   - Cannot validate if displayed data is correct
   - Cannot verify business logic
   - Assuming reasonable behavior based on observation

2. **No Official Spec:**
   - Requirements are reverse-engineered
   - May miss intended behavior
   - Edge cases may be incomplete

3. **Demo Application:**
   - May have intentional bugs for assignment
   - Backend logic unknown
   - API contract unknown

---

## Test Coverage Goals

### High Priority (Must Test)
- ✅ Category filtering (Popular, Trending, Newest, Top Rated)
- ✅ Title search functionality
- ✅ Pagination (basic + boundaries)
- ✅ Known issues (negative tests)
- ✅ Filter persistence (defect validation)

### Medium Priority (Should Test)
- 🟡 Type filtering (Movies/TV Shows)
- 🟡 Combined filters
- 🟡 Year/Rating/Genre filters
- 🟡 Browser state management

### Low Priority (Nice to Have)
- 🟢 Performance testing
- 🟢 Cross-browser validation beyond Chrome/Firefox
- 🟢 Mobile responsiveness
- 🟢 Accessibility

---

## References

- **Assignment PDF:** `reference/rr_qa_automation_assignment_.pdf`
- **Application URL:** https://tmdb-discover.surge.sh/
- **Design Decisions:** `docs/design-decisions.md`
- **Test Strategy:** `docs/test-strategy.md`
- **Test Cases:** `docs/test-cases.md`
- **Defects Found:** `docs/defects.md`

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-10-04 | QA Engineer | Initial requirements captured from exploration |

---

## Approval

**Note:** These are reverse-engineered requirements for testing purposes only.
In a production scenario, requirements would be:
- Validated with Product Owner
- Approved by stakeholders
- Baselined in requirements management system
- Traceable to user stories/epics

**For this assignment:** These requirements serve as the foundation for test case generation and defect reporting.
