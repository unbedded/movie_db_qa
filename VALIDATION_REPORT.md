# Requirements.yml Validation Report

**Date:** 2025-10-05
**Validator:** Automated Script + Manual Review
**Status:** ❌ FAIL - Multiple broken references found

---

## Executive Summary

The validation of `/home/preact/sw/job/rapyuta/movie_db_qa/rubric/requirements.yml` against referenced documentation has identified **26 broken references** across 3 categories:

| Category | Total Tags | Valid | Broken | Status |
|----------|-----------|-------|--------|--------|
| **Design Tags** | 16 | 0 | 16 | ❌ FAIL |
| **Test Tags** | 11 | 11 | 0 | ✅ PASS |
| **Artifact Paths** | 35 | 25 | 10 | ⚠️ PARTIAL |
| **Defect Tags** | 4 | 4 | 0 | ✅ PASS |

**Overall Status:** ❌ FAIL

---

## Detailed Findings

### 1. Design Tags (DD-X.Y) - 16 BROKEN REFERENCES

**Issue:** All design tags in requirements.yml use format `DD-X.Y` (e.g., `DD-4.1`, `DD-9.2`), but `docs/design-decisions.md` uses numbered section headers (e.g., `## 4. Code Architecture & Patterns`).

**Root Cause:** Mismatch between tagging scheme in requirements.yml and actual documentation structure.

**Broken References:**

| Requirement | Missing Design Tag | Expected Location |
|-------------|-------------------|-------------------|
| FLT-CAT-1.1 | DD-4.1 | docs/design-decisions.md |
| FLT-CAT-1.2 | DD-4.1 | docs/design-decisions.md |
| PAG-1.1 | DD-4.2 | docs/design-decisions.md |
| PAG-2.1 | DD-4.2 | docs/design-decisions.md |
| PAG-2.2 | DD-4.2 | docs/design-decisions.md |
| URL-2.1 | DD-4.3 | docs/design-decisions.md |
| URL-2.2 | DD-4.3 | docs/design-decisions.md |
| NEG-1.1 | DD-5.2 | docs/design-decisions.md |
| FLT-CMB-1.1 | DD-4.1 | docs/design-decisions.md |
| ASSIGN-1 | DD-5 | docs/design-decisions.md |
| ASSIGN-2 | DD-9 | docs/design-decisions.md |
| ASSIGN-3 | DD-9.2 | docs/design-decisions.md |
| ASSIGN-4 | DD-10 | docs/design-decisions.md |
| ASSIGN-5 | DD-6 | docs/design-decisions.md |
| ASSIGN-6 | DD-8 | docs/design-decisions.md |
| ASSIGN-7 | DD-11 | docs/design-decisions.md |

**Actual Structure in design-decisions.md:**
```
## 1. Framework & Technology Selection
## 2. Version Control Strategy
## 3. Test Design Strategy
## 4. Code Architecture & Patterns
## 5. Test Scope & Coverage
## 6. Quality & Standards
## 7. Configuration Management
## 8. Logging Strategy
## 9. Test Reporting Strategy
## 10. CI/CD Strategy
## 11. Defect Reporting Approach
## 12. Documentation Strategy
## 13. Time Allocation & Prioritization
## 14. Success Metrics & Quality Gates
## 15. Traceability & Requirements Management
```

**Mapping Analysis:**
- `DD-4.1` → Should map to Section 4 subsection (doesn't exist as explicit header)
- `DD-5` → Should map to Section 5 (exists as "## 5. Test Scope & Coverage")
- `DD-9.2` → Should map to Section 9 subsection (doesn't exist as explicit header)

---

### 2. Test Tags (TC-XXX-YYY-ZZZ) - ✅ ALL VALID

**Status:** All 11 test tags found in `docs/test-cases.md`

**Valid References:**
- TC-FLT-CAT-001 ✅
- TC-FLT-CAT-002 ✅
- TC-PAG-001 ✅
- TC-PAG-002 ✅
- TC-PAG-003 ✅
- TC-NEG-001 ✅
- TC-NEG-002 ✅
- TC-CMB-001 ✅

---

### 3. Artifact Paths - 10 BROKEN REFERENCES

**Issue:** Some artifact paths reference pytest test names that don't match actual function names, and some reference directories/patterns that don't exist.

#### 3.1 Test Function Name Mismatches (8 files)

**Root Cause:** requirements.yml uses simplified test names, but actual test functions use TC-prefixed names.

| Requirement | Referenced Path | Actual Function Name | Status |
|-------------|----------------|---------------------|--------|
| FLT-CAT-1.1 | `tests/test_foundation.py::test_popular_filter_works` | `test_tc_flt_cat_001_popular_filter_works` | ❌ MISMATCH |
| FLT-CAT-1.2 | `tests/test_foundation.py::test_trending_filter_works` | `test_tc_flt_cat_002_trending_filter_works` | ❌ MISMATCH |
| PAG-1.1 | `tests/test_foundation.py::test_navigate_to_page_2` | `test_tc_pag_001_navigate_to_page_2` | ❌ MISMATCH |
| PAG-2.1 | `tests/test_foundation.py::test_filter_persistence_across_pagination` | `test_tc_pag_003_filter_persists_across_pagination` | ❌ MISMATCH |
| PAG-2.2 | `tests/test_foundation.py::test_last_page_boundary_error` | `test_tc_pag_002_last_page_boundary_error` | ❌ MISMATCH |
| URL-2.1 | `tests/test_foundation.py::test_direct_url_access_fails` | `test_tc_neg_001_direct_url_access_fails` | ❌ MISMATCH |
| NEG-1.1 | `tests/test_foundation.py::test_invalid_page_number_handling` | `test_tc_neg_002_invalid_page_number` | ❌ MISMATCH |
| FLT-CMB-1.1 | `tests/test_foundation.py::test_popular_plus_movies_filter` | `test_tc_cmb_001_popular_movies_combined` | ❌ MISMATCH |

#### 3.2 Non-Existent Files/Directories (2 items)

| Requirement | Referenced Path | Issue |
|-------------|----------------|-------|
| ASSIGN-4 | `tests/conftest.py::tmdb_api_calls fixture` | Not a valid pytest path (descriptive reference) |
| ASSIGN-5 | `logs/*.log` | Directory `/logs/` does not exist |

---

### 4. Defect Tags (DEF-XXX) - ✅ ALL VALID

**Status:** All 4 defect tags found in `artifacts/defect-manual-reports/defects-manual-found.md`

**Valid References:**
- DEF-001 ✅
- DEF-002 ✅
- DEF-003 ✅
- DEF-004 ✅

---

## Root Cause Analysis

### 1. Design Tag Mismatch

The requirements.yml uses a sub-section tagging scheme (`DD-X.Y`) that doesn't exist in the actual design-decisions.md document. The design document uses simple numbered sections without explicit sub-section IDs.

**Problem:** Requirements expect granular design decision tags (e.g., `DD-4.1` for a specific filtering decision), but the design doc only has section-level headers (e.g., `## 4. Code Architecture & Patterns`).

### 2. Test Function Naming Convention Change

At some point, the test function naming convention changed from simple names (e.g., `test_popular_filter_works`) to TC-prefixed names (e.g., `test_tc_flt_cat_001_popular_filter_works`). The requirements.yml wasn't updated to reflect this change.

### 3. Missing Logs Directory

The `logs/` directory referenced in ASSIGN-5 doesn't exist. Logging may be configured but not actively writing to disk, or the directory is gitignored and not present.

---

## Recommendations

### Option 1: Update requirements.yml (RECOMMENDED)

**Effort:** Low
**Impact:** Aligns requirements with actual implementation

**Actions:**
1. Update all `DD-X.Y` tags to reference actual section numbers (e.g., `DD-4` instead of `DD-4.1`)
2. Update test function paths to match actual pytest function names
3. Fix or remove broken artifact references
4. Create missing directories (e.g., `logs/`)

### Option 2: Update Documentation

**Effort:** High
**Impact:** Adds explicit design decision IDs to documentation

**Actions:**
1. Add explicit `DD-X.Y` headers to design-decisions.md
2. Rename test functions to match requirements.yml
3. Create missing directories and files

### Option 3: Hybrid Approach

**Effort:** Medium
**Impact:** Best of both approaches

**Actions:**
1. Add design decision anchors to design-decisions.md without restructuring
2. Update requirements.yml test paths to match actual functions
3. Document known discrepancies in a TRACEABILITY.md file

---

## Validation Statistics

```
Total Requirements Checked:     17
Total Tags Validated:           66

Breakdown:
- Design Tags:       16 (0 valid, 16 broken)
- Test Tags:         11 (11 valid, 0 broken)
- Artifact Paths:    35 (25 valid, 10 broken)
- Defect Tags:       4 (4 valid, 0 broken)

Overall Pass Rate:   75.8% (50/66 references valid)
```

---

## Conclusion

The requirements.yml file has **26 broken references** that need to be addressed. The primary issues are:

1. **Design tag format mismatch** - All 16 design tags use a format that doesn't exist in the documentation
2. **Test function name changes** - 8 test paths reference old function names
3. **Missing directories** - 1 directory path doesn't exist
4. **Non-standard artifact reference** - 1 artifact uses descriptive text instead of actual path

**Recommended Action:** Update requirements.yml to match actual implementation (Option 1), as this is the lowest effort and highest accuracy approach.

---

## Appendix: Full Validation Output

```
================================================================================
REQUIREMENTS.YML VALIDATION REPORT
================================================================================

SUMMARY:
  Total Requirements:     17
  Total Design Tags:      16
  Total Test Tags:        11
  Total Artifact Paths:   35
  Total Defect Tags:      4

VALIDATION RESULTS:
  Missing Design Tags:    16
  Missing Test Tags:      0
  Missing Artifact Paths: 10
  Missing Defect Tags:    0

❌ OVERALL STATUS: FAIL - Some references are broken!
```
