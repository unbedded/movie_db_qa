# QA Automation Assignment - Project Plan

> **Assignment Philosophy:** "Frameworks matter less than you think. Better spend time polishing your deliverable as a whole."

## Table of Contents
- [📊 Project Status: Phase 4 Complete - Ready for v0.4.0](#-project-status-phase-4-complete---ready-for-v040)
  - [📋 Git Branch Tracking (for Assignment Evaluation)](#-git-branch-tracking-for-assignment-evaluation)
- [🎯 CRITICAL SUCCESS FACTORS](#-critical-success-factors)
- [Phase 1: Initial Framework Setup ✅ COMPLETED (v0.2.0)](#phase-1-initial-framework-setup--completed-v020)
- [Phase 2: Documentation & Foundation ✅ COMPLETED](#phase-2-documentation--foundation--completed)
- [Phase 3: Test Implementation ✅ COMPLETE](#phase-3-test-implementation--complete)
- [Phase 4: API Validation & Technical Debt Cleanup ✅ COMPLETE](#phase-4-api-validation--technical-debt-cleanup--complete)
- [Phase 5: Final Polish & Delivery ⏳ NEXT](#phase-5-final-polish--delivery--next)
- [📦 TECHNICAL DEBT & DEFERRED ITEMS](#-technical-debt--deferred-items)
- [💡 FOUNDATION STRATEGY - 1.5 DAYS](#-foundation-strategy---15-days)
- [🎯 REMEMBER](#-remember)

## 📊 Project Status: Phase 4 Complete - Ready for v0.4.0
- **Current Branch:** `feature/test-api-and-debt` (ready to push)
- **Next Phase:** Phase 5 Final Polish & Delivery (1-2 hours)
- **Phase 3 Rubric:** 78/100 → **Phase 4 Rubric: 84/100** (+6 points from API validation)
- **Phase 4 Changes:** API validation + screenshot demo + magic numbers cleanup + CI fix
- **Tests:** 2 pass, 4 xfail, 1 xpass, 1 skip (8 total) + API assertions
- **Defects:** 5 documented with evidence
- **CI/CD:** GitHub Actions (CI fix added - pending push to test)

### 📋 Git Branch Tracking (for Assignment Evaluation)
**Policy:** Keep ALL remote branches to show development progression

| Branch | Status | Purpose | Commits | Preserved |
|--------|--------|---------|---------|-----------|
| `main` | ✅ Current | Production releases | v0.2.0 tag | Yes |
| `develop` | ✅ Current | Integration branch | Latest work | Yes |
| `feature/update-todo` | ✅ Merged | Phase 2 documentation & foundation | eed4fa7 | **Remote kept** ✅ |
| `feature/test-impl` | ⏳ Current | Phase 3 test implementation | TBD | Will keep |

**Commit History:**
- `eed4fa7` - Phase 2 complete: docs + foundation setup (feature/update-todo)
- `3f06fa3` - v0.2.0 release (release/0.2.0 → main)
- `3d07371` - Initial framework setup
- `1b14319` - Initial commit

---

## 🎯 CRITICAL SUCCESS FACTORS

### What Scores High (Focus 80% of effort here)
1. **Test Case Design + Documentation** - WHY you chose these cases
2. **Clean, Maintainable Code** - Readable, well-structured
3. **Complete Documentation** - Answer all required questions
4. **Defect Reports** - Clear, with evidence
5. **Test Strategy** - Show your thinking

### What Matters Less (Don't overthink)
- Framework choice (picking most expeditious: Python 3.13 + Pytest + Git-flow)
- Complex architecture
- Advanced patterns

---

## Phase 1: Initial Framework Setup ✅ COMPLETED (v0.2.0)
**Branch:** `release/0.2.0` → `main` + `develop`
**Goal:** Get basic testing environment running fast
**Commits:** `1b14319` (initial) → `3d07371` (framework) → `d5774b1` (v0.2.0)

- [x] Create GitHub repo: movie_db_qa (git@github.com:unbedded/movie_db_qa.git)
- [x] Pick framework: **Pytest** (Python 3.13)
- [x] Pick language: **Python**
- [x] Basic project setup with `pyproject.toml`
- [x] Install framework + reporter: pytest, pytest-cov, ruff, mypy
- [x] Verify can run tests: `make test-full` - 5/5 passing, 100% coverage
- [x] Basic folder structure: `/tests`, `/docs`, `/src`
- [x] CI/CD workflow (GitHub Actions)
- [x] Git-flow branching model configured
- [x] Pre-commit hooks for code quality
- [x] Makefile build automation
- [x] Released v0.2.0 to main branch

**Success Metric:** ✅ Can run tests with `make test-full` and see HTML + terminal reports

---

## Phase 2: Documentation & Foundation ✅ COMPLETED (feature/update-todo)
**Branch:** `feature/update-todo` (commit `eed4fa7`) → merged to `develop`
**Goal:** Complete ALL documentation (requirements, defects, test strategy, test cases, README) + foundation code
**Time Spent:** ~6-8 hours (over multiple sessions)
**What This Phase Included:** Requirements, Defects (5 bugs), Test Strategy, Test Cases (8 WHYs), README (568 lines), Foundation Code

### What Was Accomplished:
- [x] **Exploration & Requirements:**
  - [x] Manually explored https://tmdb-discover.surge.sh/
  - [x] Created `docs/requirements.md` (reverse-engineered specs with semantic IDs)
  - [x] Found 5 defects (DEF-001 through DEF-005) - meets 5 minimum!
  - [x] Created `docs/defects-manual-found.md` with simple 6-line format
  - [x] Captured screenshots in `docs/images/`

- [x] **Documentation (25% of assignment score!):**
  - [x] Created comprehensive `docs/design-decisions.md` (14 sections)
  - [x] Enhanced with Config & Logging philosophy (data-driven code)
  - [x] Documented Playwright vs Selenium decision with comparison tables
  - [x] Completed README.md with all 8 required sections
  - [x] Created placeholder `docs/test-strategy.md` (needs content in Phase 3)
  - [x] Created placeholder `docs/test-cases.md` (needs content in Phase 3)

- [x] **Foundation Code:**
  - [x] Fixed CI workflow (replaced `__MYPY_PY_VERSION__` with '3.13')
  - [x] Created Page Object stubs (`base_page.py`, `discover_page.py`)
  - [x] Created utils (`config.py`, `logger.py`) with backend abstraction
  - [x] Created Playwright fixtures (`tests/conftest.py`)
  - [x] Installed Playwright and dependencies
  - [x] Updated gitflow commands to preserve branches for evaluation

- [x] **Project Governance:**
  - [x] Updated TODO.md with Technical Debt section
  - [x] Added Git Branch Tracking to README and TODO
  - [x] Added .gitignore rule for CI debugging artifacts

**Success Metric:** ✅ All documentation complete, foundation ready for Phase 3 coding

---

## Phase 3: Test Implementation ✅ COMPLETE (v0.3.0 Ready)
**Branch:** `feature/test-impl` ✅ CREATED
**Goal:** Implement 8-10 test cases and complete test documentation
**Time Budget:** 4-5 hours
**Time Spent:** ~3 hours

### PRIORITY 1: Complete Test Documentation ✅ DONE (1.5 hours)
- [x] Complete `docs/test-strategy.md` (280 lines):
  - [x] Risk-based priorities (Critical → High only)
  - [x] Test design techniques (BVA, EP, Negative, Decision Table, Exploratory)
  - [x] Scope: IN (core filters + pagination + known issues)
  - [x] Scope: OUT (defer Medium/Low)
  - [x] Logging strategy with lazy % formatting
  - [x] Reference `docs/design-decisions.md`

- [x] Complete `docs/test-cases.md` (496 lines - 8 CRITICAL/HIGH cases):
  - [x] 2 filtering tests (Popular, Trending) - with WHY ✅
  - [x] 3 pagination tests (page 2, last page, filter persistence) - with WHY ✅
  - [x] 2 negative tests (direct URL DEF-001, invalid page) - with WHY ✅
  - [x] 1 combined filter test (Popular + Movies - deferred) - with WHY ✅
  - [x] **WHY explanations complete for all 8 test cases**

### PRIORITY 2: Implement Foundation Tests ✅ DONE (1.5 hours)
- [x] Implement Page Object methods in `discover_page.py`:
  - [x] Filter actions (Popular, Trending, Newest, Top Rated)
  - [x] Pagination actions (Next, Previous, navigate to page)
  - [x] Getters (results count, current page, movie titles)
  - [x] Filter state checkers (is_popular_active, etc.)
  - [x] All with lazy % logging

- [x] Implement 8 test cases in `tests/test_foundation.py`:
  - [x] TC-FLT-CAT-001: Popular filter works (Critical, EP)
  - [x] TC-FLT-CAT-002: Trending filter works (Critical, EP)
  - [x] TC-PAG-001: Navigate to page 2 (High, BVA)
  - [x] TC-PAG-002: Last page boundary error (High, BVA, xfail DEF-002)
  - [x] TC-PAG-003: Filter persistence (High, Exploratory, xfail DEF-003)
  - [x] TC-NEG-001: Direct URL access (High, Negative, xfail DEF-001)
  - [x] TC-NEG-002: Invalid page number (High, BVA)
  - [x] TC-CMB-001: Popular + Movies (High, Decision Table, skip - deferred)

- [x] Add logging (test start/end, key actions, lazy % formatting)
- [x] Add screenshots on failure (pytest hook in conftest.py → `screenshots/` dir)
- [x] Basic API validation (deferred - UI focus for foundation)

### PRIORITY 3: Quality & Reports ✅ DONE (30 min)
- [x] Run `make quality` - Fixed logger issue, all checks PASS ✅
- [ ] Run `make test-full` - Verify tests work
- [ ] Verify HTML + Console reports
- [ ] Clean up debug code (none needed)

### 🚦 Phase Gate 3 Review - ALL COMPLETE ✅
- [x] ✅ 8 test cases documented with WHY (docs/test-cases.md)
- [x] ✅ Test strategy complete (docs/test-strategy.md)
- [x] ✅ All tests implemented (tests/test_foundation.py)
- [x] ✅ Tests verified PASSING (2 pass, 4 xfail, 1 xpass, 1 skip)
- [x] ✅ Reports generated (HTML + coverage + logs)
- [x] ✅ Rubric evaluation complete (78/100 - Good)
- [x] ✅ Code quality checks pass (ruff, mypy, black)

### ✅ CI Status
**Status:** CI should be working on `feature/test-impl` branch
**Fix Applied:** Commit `eed4fa7` replaced `__MYPY_PY_VERSION__` placeholder with `'3.13'`
**Note:** Old `feature/update-todo` branch had CI issues at commit `fb84905`, but this branch includes the fix

**Success Metric:** Foundation test suite runs end-to-end successfully

---

## Phase 4: API Validation & Technical Debt Cleanup ✅ COMPLETE
**Branch:** `feature/test-api-and-debt` (commit 5104f12)
**Goal:** Complete missing assignment requirement (API validation) + low-risk cleanup items
**Time Spent:** 1.5 hours
**Achievement:** API validation implemented - Assignment requirement R-5.3 satisfied!

### PRIORITY 1: API Validation (ASSIGNMENT REQUIREMENT) ✅ DONE
**Gap:** Rubric R-5.3 - "Missing API validation" → lose 3-4 points
**Assignment PDF Page 2:** "Usage of browser APIs calls and how you are asserting them"

- [x] Add Playwright network interception to conftest.py
  - [x] Create fixture to capture network requests
  - [x] Filter for TMDB API calls (api.themoviedb.org)
  - [x] Log API calls with lazy % formatting
- [x] Add API assertions to 3 existing tests:
  - [x] TC-FLT-CAT-001: Verify `/movie/popular?page=1` called
  - [x] TC-FLT-CAT-002: Verify `/trending/movie/week?page=1` called
  - [x] TC-PAG-001: Verify `page=2` parameter in API call
- [x] Update test-strategy.md with API validation approach
- [x] Update README with API validation explanation

### PRIORITY 2: Demonstrate Screenshot Capture ✅ DONE
**Gap:** Feature implemented but not demonstrated (screenshots/ folder empty)
**Why:** Shows complete error reporting pipeline (logs + HTML + screenshots)

- [x] Temporarily break TC-FLT-CAT-001 test
- [x] Run test to generate failure screenshot
- [x] Copy screenshot to `docs/images/example-test-failure-screenshot.png`
- [x] Revert test to passing state
- [x] Update README: Add screenshot capture section with example
- [x] Add comment in conftest.py explaining screenshot trigger conditions

### PRIORITY 3: Magic Numbers Cleanup ✅ DONE
**Gap:** Hardcoded values in test_foundation.py (violates CLAUDE.md standards)

- [x] Move to `src/movie_db_qa/utils/config.py`:
  - [x] `expected_results_per_page = 20`
  - [x] Remove duplicate `BASE_URL` from test_foundation.py (use config.base_url)
- [x] Update test_foundation.py to import from config
- [x] Verify tests still pass

### PRIORITY 4: CI Fix ✅ DONE
**Gap:** GitHub Actions CI failing - Playwright browsers not installed
**Why:** Evaluators need to see CI pipeline GREEN

- [x] Add `playwright install --with-deps chromium` to .github/workflows/ci.yml
- [x] Ready to push and verify CI passes

### 🚦 Phase Gate 4: Requirements Complete - ALL DONE ✅
- [x] ✅ API validation implemented (R-5.3 satisfied)
  - [x] Playwright network interception in conftest.py
  - [x] API assertions in 3 tests (TC-FLT-CAT-001, TC-FLT-CAT-002, TC-PAG-001)
  - [x] TMDB endpoints validated: `/movie/popular`, `/trending/movie/week`, page parameters
- [x] ✅ Screenshot capture demonstrated
  - [x] Example screenshot: `docs/images/example-test-failure-screenshot.png`
  - [x] Auto-capture working (pytest hook verified)
- [x] ✅ Magic numbers eliminated
  - [x] `config.base_url` and `config.expected_results_per_page` in config.py
  - [x] All hardcoded values removed from test_foundation.py
- [x] ✅ All tests passing (2 pass, 4 xfail, 1 xpass, 1 skip)
- [x] ✅ Quality checks pass (ruff, mypy, black)
- [x] ✅ CI fix added (playwright install --with-deps chromium)
- [x] ✅ Documentation updated (README + test-strategy.md with API validation sections)
- [x] ✅ **Rubric Re-evaluation: 84/100** - achieved +6 points from Phase 3 (78→84) via API validation

**Success Metric:** All explicit assignment requirements satisfied

---

## Phase 5: Final Polish & Delivery ⏳ AFTER PHASE 4
**Branch:** Will create `feature/polish` after Phase 4 complete
**Goal:** Clean, professional deliverable
**Time Budget:** 1-2 hours MAX

### PRIORITY 1: Quality Verification (30 min) 🚨 DO FIRST
- [ ] Run `make quality` - Fix all Ruff/MyPy issues
- [ ] Run `make test-full` 2-3 times - Verify stable
- [ ] Check HTML report looks professional
- [ ] Check console output is clear
- [ ] Verify CI is GREEN on GitHub

### PRIORITY 2: Code Cleanup (30 min) 🚨 DO SECOND
- [ ] Remove any debug code, print statements
- [ ] Clean up comments (keep useful, remove clutter)
- [ ] Verify consistent naming throughout
- [ ] Check no unused imports/dependencies

### PRIORITY 3: Documentation Final Check (30 min) 🚨 DO THIRD
- [ ] Proofread README - fix typos
- [ ] Test ALL commands in README work
- [ ] Verify all links work (docs/, rubric/)
- [ ] Check all 8 sections present and complete

### PRIORITY 4: Delivery (30 min) 🚨 FINAL STEP
- [ ] Review git history - meaningful commits
- [ ] Merge to develop
- [ ] Create release branch from develop
- [ ] Tag and release to main (if ready)
- [ ] Verify repo is public
- [ ] Final verification: Clone fresh and run tests

### 🚦 Phase Gate 5: Final Delivery Check
- [ ] All foundation tests PASS
- [ ] All documentation COMPLETE (8 sections)
- [ ] Minimum 5 defects documented
- [ ] CI pipeline GREEN
- [ ] Repo clean and professional
- [ ] README comprehensive
- [ ] Can clone fresh and run successfully
- [ ] **Final Rubric Evaluation (target: 85-90/100)**

**Success Metric:** Professional, complete FOUNDATION deliverable ready for review

**IF TIME REMAINS - EXPAND:**
- Add more test cases (Medium priority)
- Find additional defects (beyond 5)
- Enhance documentation
- Add more exploratory tests
- Improve test coverage

### Future Enhancement: CI Report Archival (Post-v0.3.0)
- [ ] GitHub Actions: Upload test reports as CI artifacts
- [ ] Version reports by commit SHA (automatic)
- [ ] Add download links to README
- [ ] Keep `report/` and `htmlcov/` gitignored (regenerate fresh)
- [ ] Sample reports in `docs/reports/` show baseline

**Implementation:**
```yaml
# .github/workflows/ci.yml
- name: Archive test reports
  uses: actions/upload-artifact@v3
  with:
    name: test-reports-${{ github.sha }}
    path: |
      report/
      htmlcov/
```

### Future Enhancement: Demonstrate Screenshot Capture (Post-v0.3.0)
**Goal:** Show screenshot-on-failure artifact collection works

**Why:** Currently `screenshots/` is empty because no unexpected failures occurred (xfail tests don't trigger screenshot hook). Adding sample demonstrates the feature works.

**Options:**
1. **Temporarily break a passing test** → run → capture screenshot → revert
2. **Add commented-out test with intentional failure** → documentation example
3. **Add sample screenshot to docs/** → `docs/images/example-test-failure.png`
4. **Update README** → explain when/how screenshots are captured

**Implementation:**
- [ ] Add sample failure screenshot to `docs/images/`
- [ ] Update README section on screenshot capture
- [ ] Add code comment in conftest.py explaining trigger conditions
- [ ] Consider: Add one test WITHOUT xfail to demonstrate live failure capture

**Value:** Shows evaluator the full error reporting pipeline (logs + HTML + screenshots)

---

## 📋 DELIVERABLES CHECKLIST

Before submission, verify:

### Code Deliverables
- [ ] GitHub repo: movie_db_qa (public) - git@github.com:unbedded/movie_db_qa.git
- [ ] Working test suite (all tests pass)
- [ ] HTML report generated
- [ ] Console report shown
- [ ] Logging implemented
- [ ] API validation included

### Documentation Deliverables
- [ ] `README.md` - Answers ALL 8 required questions
- [ ] `docs/test-cases.md` - Step-by-step test descriptions
- [ ] `docs/test-strategy.md` - Testing approach and rationale
- [ ] `docs/defects-manual-found.md` - Defect reports with evidence
- [ ] `docs/design-decisions.md` - Design choices and trade-offs (shows thinking)
- [ ] `docs/ci-integration.md` - CI approach (or in README)

### Quality Checks
- [ ] Code is clean and maintainable
- [ ] Tests are reliable (not flaky)
- [ ] Documentation is complete and clear
- [ ] Found minimum 5 defects
- [ ] Easy to install and run
- [ ] Git history is professional

---

## ⏰ TIME ALLOCATION - REVISED FOR 1.5 DAYS (12-15 hours remaining)

**Strategy: FOUNDATION FIRST → Build complete minimum viable deliverable → Expand if time**

| Phase | Foundation | Expand (if time) | Status |
|-------|-----------|------------------|---------|
| Phase 1: Setup | ✅ 2-3 hrs | - | COMPLETE (v0.2.0) |
| Phase 2: Test Design | 3-4 hrs | +2 hrs more cases | 🔴 NEXT |
| Phase 3: Implementation | 4-5 hrs | +2 hrs more tests | 🔴 CRITICAL |
| Phase 4: Defects | 1.5-2 hrs | +1 hr more bugs | 🔴 CRITICAL |
| Phase 5: README | 2-3 hrs | +1 hr polish | 🔴 CRITICAL |
| Phase 6: Polish | 1-2 hrs | - | 🔴 FINAL |
| **TOTAL** | **12-16 hrs** | **+6 hrs** | |

**Foundation = Passing Score (70/100):**
- 8-10 test cases designed with WHY
- 8-10 tests implemented and PASSING
- 5 defects documented with evidence
- README answers ALL 8 questions
- CI GREEN

**Expansion = Excellence (85/100):**
- 15+ test cases
- 10+ defects found
- Enhanced documentation
- More coverage

---

## 📦 TECHNICAL DEBT & DEFERRED ITEMS

### ✅ Implemented (Demonstrable Proof)

| Feature | Implementation Location |
|---------|------------------------|
| PEP8 + Type Hints + 100% Coverage | `Makefile` + `.pre-commit-config.yaml` + `.github/workflows/ci.yml` |
| Git-Flow Workflow | Branch protection (`develop` + `main`), feature branches required |
| Quality Gates | `make quality` (ruff + mypy + black) |
| CI/CD Pipeline | `.github/workflows/ci.yml` (quality → tests on push/PR) |
| Test Framework | `pyproject.toml` (pytest ≥7.0, pytest-cov ≥4.0) |

### 🔄 Deferred (Post-Submission)

| Item | Reason | Effort |
|------|--------|--------|
| AI Traceability System | Innovation feature, not assignment requirement | 2-3 hrs |
| Extended Test Scope | Foundation = 8-10 tests, defer Type/Metadata filters | 6 hrs (15+ tests) |
| Cross-Browser Matrix | Chrome only, not Firefox/Safari/Edge | 1-2 hrs |
| Comprehensive API Validation | 2-3 examples sufficient for assignment | 2-3 hrs |

### ❌ Out of Scope (Won't Do)

| Item | Reason | Effort |
|------|--------|--------|
| Mobile/Accessibility/Performance | Not assignment requirements | 10+ hrs |
| Data Accuracy Validation | No backend access, cannot verify TMDB API | N/A |
| Advanced POM | Simple 1-2 page classes sufficient | 3-4 hrs |
| Parallel Execution | Small suite, sequential acceptable | 1 hr |

**Expansion Effort:** 20-30 hrs for 90-95/100 vs 1.5 days for 70-80/100

---

## 💡 FOUNDATION STRATEGY - 1.5 DAYS

### Critical Path (Must Do - 12-16 hours)
1. ✅ **Phase 2 (3-4 hrs):** Document 8-10 test cases with WHY + CI fix
2. ✅ **Phase 3 (4-5 hrs):** Implement those 8-10 tests - WORKING
3. ✅ **Phase 4 (1.5-2 hrs):** Find and document 5 defects with evidence
4. ✅ **Phase 5 (2-3 hrs):** README answers ALL 8 questions
5. ✅ **Phase 6 (1-2 hrs):** Polish, CI GREEN, professional delivery

### High-Impact Actions (Do These!)
1. ⭐ **Explain WHY** for every test case (30% of score)
2. ⭐ **Complete README** with all 8 sections (25% of score)
3. ⭐ **Find 5+ defects** with clear evidence (15% of score)
4. ⭐ **Clean code** that runs end-to-end (25% of score)
5. ⭐ **CI GREEN** on GitHub

### Time Savers (Don't Over-Engineer!)
1. Use pytest-html (built-in) - don't build custom reporter
2. Use Python logging (built-in) - don't add loguru
3. Simple Page Object (1-2 files) - don't build framework
4. 8-10 tests first - expand later if time
5. Reference docs/design-decisions.md - don't re-explain everything

### If You Get Stuck (Time Limits!)
- Exploration stuck? → 30 min max, document what you found
- Test case design stuck? → Focus on Critical/High only
- Implementation stuck? → Skip hard tests, do simple ones first
- Can't find 5 defects? → Known issues + boundary tests + search edge cases
- README stuck? → Use design-decisions.md as source material

---

## 🎯 REMEMBER

**The Real Evaluation Criteria:**
1. Can you design good tests? (Strategy + Cases)
2. Can you write clean code? (Maintainability)
3. Can you communicate? (Documentation)
4. Can you find defects? (QA mindset)
5. Can you think strategically? (CI approach)

**NOT being evaluated on:**
- Framework complexity
- Advanced patterns
- Cutting-edge tech
- Volume of tests

**Success = Working tests + Clear thinking + Good documentation**

Pick familiar tools, write clean code, document thoroughly, find bugs, explain your thinking.

**Less is more when it's clean, clear, and complete.**
