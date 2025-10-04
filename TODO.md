# QA Automation Assignment - Project Plan

> **Assignment Philosophy:** "Frameworks matter less than you think. Better spend time polishing your deliverable as a whole."

## 📊 Project Status: Phase 2 In Progress
- **Current Phase:** Phase 2 - Test Design (partially complete)
- **Time Remaining:** 1.5 days (~12-15 hours)
- **Strategy:** FOUNDATION FIRST, then expand
- **Framework:** Python 3.13 + Pytest
- **Build System:** Makefile automation
- **Quality Tools:** Ruff, MyPy, Pytest-cov (100% coverage)
- **CI/CD:** GitHub Actions configured (needs CI fix)
- **Version Control:** Git-flow workflow

**Phase 2 Progress:**
- ✅ Exploration complete (found 6 defects!)
- ✅ Requirements documented
- ✅ Defects documented
- 🔄 Test strategy (in progress)
- 🔄 Test cases (in progress)
- ⏳ CI fix (pending)

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

## Phase 1: Quick Setup ✅ COMPLETED (v0.2.0)
**Branch:** `feature/initial-setup` → `develop` → `main`
**Goal:** Get basic testing environment running fast

- [x] Create GitHub repo: movie_db_qa (git@github.com:unbedded/movie_db_qa.git)
- [x] Pick framework: **Pytest** (Python 3.13)
- [x] Pick language: **Python**
- [x] Basic project setup with `pyproject.toml`
- [x] Install framework + reporter: pytest, pytest-cov, ruff, mypy
- [x] Verify can run tests: `make test-full` - 5/5 passing, 100% coverage
- [x] Basic folder structure: `/tests`, `/docs`, `/src`
- [x] **BONUS:** CI/CD workflow (GitHub Actions)
- [x] **BONUS:** Git-flow branching model configured
- [x] **BONUS:** Pre-commit hooks for code quality
- [x] **BONUS:** Makefile build automation
- [x] **BONUS:** Released v0.2.0 to main branch

**Success Metric:** ✅ Can run tests with `make test-full` and see HTML + terminal reports

---

## Phase 2: FOUNDATION - Core Test Design (3-4 hours) 🔴 CRITICAL
**Branch:** `feature/test-design`
**Goal:** Minimum viable test documentation to enable coding
**Time Budget:** 3-4 hours MAX

### PRIORITY 1: Quick Exploration (30 min) ✅ COMPLETE
- [x] Manually explore https://tmdb-discover.surge.sh/ (30 min)
- [x] Document 2 known issues in `docs/defects.md` (DEF-001, DEF-002)
- [x] Map core filtering options (Popular, Trending, Search, Pagination)
- [x] Note 2-3 obvious test scenarios per feature
- [x] **BONUS:** Found 4 NEW defects (DEF-003 through DEF-006)
- [x] **BONUS:** Created `docs/requirements.md` (reverse-engineered specs)
- [x] **BONUS:** Captured screenshots in `docs/images/`

### PRIORITY 2: Minimal Test Strategy (30 min) 🚨 DO SECOND
- [ ] Complete `docs/test-strategy.md` - KEEP IT SIMPLE:
  - [ ] Risk-based priorities (Critical → High only for now)
  - [ ] Test design techniques to use (BVA, EP, Negative)
  - [ ] Scope: What's IN (core filters + pagination + known issues)
  - [ ] Scope: What's OUT (defer Medium/Low priority items)
- [ ] Reference `docs/design-decisions.md` for rationale

### PRIORITY 3: Foundation Test Cases (1.5-2 hours) 🚨 DO THIRD
**Target: 8-10 CRITICAL/HIGH test cases only**
- [ ] Create `docs/test-cases.md` with FOUNDATION cases:
  - [ ] 2-3 filtering tests (Popular, Trending, Search) - with WHY
  - [ ] 2-3 pagination tests (navigation, boundaries) - with WHY
  - [ ] 2 negative tests (known issues DEF-001, DEF-002) - with WHY
  - [ ] 1-2 combined filter tests (if time) - with WHY
- [ ] Apply test design techniques (note which used)
- [ ] Prioritize: ALL should be Critical or High
- [ ] **Focus on WHY explanations - this scores 30%**

### PRIORITY 4: CI Fix (30 min) 🚨 BEFORE COMMIT
- [ ] Fix `.github/workflows/ci.yml`: Replace `__MYPY_PY_VERSION__` → `3.13`
- [ ] Commit and push to verify CI passes
- [ ] If CI fails, fix immediately (blocking issue)

### 🚦 Phase Gate 2 Review (10 min)
- [ ] Have 8-10 test cases documented with WHY
- [ ] Test strategy explains approach
- [x] ✅ 6 defects documented (exceeds 5 minimum!)
- [x] ✅ Requirements documented (`docs/requirements.md`)
- [ ] CI pipeline GREEN on GitHub
- [ ] Ready to START CODING

**Success Metric:** Can start implementing tests immediately from this documentation

**COMPLETED EXTRAS:**
- ✅ `docs/defects.md` - 6 defects with simple format
- ✅ `docs/requirements.md` - Reverse-engineered specs with semantic IDs
- ✅ `docs/images/` - Bug screenshots captured
- ✅ Found 4 NEW bugs (exceeds 3 minimum)

**STILL TODO:**
- Test strategy (simple version)
- 8-10 test cases with WHY
- CI fix

---

## Phase 3: FOUNDATION - Core Test Implementation (4-5 hours) 🔴 CRITICAL
**Branch:** `feature/test-implementation`
**Goal:** Working tests for 8-10 CRITICAL/HIGH cases
**Time Budget:** 4-5 hours MAX

### PRIORITY 1: Simple Framework Setup (1 hour) 🚨 DO FIRST
- [ ] Create `src/pages/discover_page.py` - Simple Page Object (NO OVER-ENGINEERING)
- [ ] Create `src/utils/logger.py` - Basic logging utility
- [ ] Create `tests/conftest.py` - Pytest fixtures (setup/teardown)
- [ ] Verify basic test runs: `make test`

### PRIORITY 2: Implement Foundation Tests (2.5-3 hours) 🚨 DO SECOND
**Implement ONLY the 8-10 test cases from docs/test-cases.md**
- [ ] **Filtering Tests** (2-3 tests)
  - [ ] Popular filter works
  - [ ] Trending filter works
  - [ ] Search by title works
- [ ] **Pagination Tests** (2-3 tests)
  - [ ] Navigate to page 2
  - [ ] Navigate to page 3
  - [ ] Boundary test (last valid page)
- [ ] **Negative Tests** (2 tests - known issues)
  - [ ] Direct URL slug fails (DEF-001)
  - [ ] Last pagination page broken (DEF-002)
- [ ] **Combined Filter Test** (1 test if time)
  - [ ] Popular + Movies filter combination

### PRIORITY 3: Essential Features (30-45 min) 🚨 DO THIRD
- [ ] Logging: Log test start/end, key actions
- [ ] Screenshots: Capture on failure (pytest plugin)
- [ ] API validation: Basic assertion on network calls (1-2 examples)
- [ ] Verify: HTML + Console reports generate

### PRIORITY 4: Quality Check (30 min) 🚨 BEFORE COMMIT
- [ ] Run `make quality` - Fix any Ruff/MyPy errors
- [ ] Run `make test-full` - All tests GREEN
- [ ] Check HTML report generated
- [ ] Clean up debug code

### 🚦 Phase Gate 3 Review (10 min)
- [ ] 8-10 tests implemented and PASSING
- [ ] Code is clean (Ruff/MyPy pass)
- [ ] Logging works
- [ ] HTML + Console reports work
- [ ] CI passes (if pushed)

**Success Metric:** Foundation test suite runs end-to-end successfully

**DEFER TO LATER (if time):**
- Type filter (Movies/TV Shows)
- Year/Rating/Genre filters
- Additional combined filter scenarios
- Advanced API validation
- More exploratory tests

---

## Phase 4: FOUNDATION - Defect Documentation ✅ COMPLETE (AHEAD OF SCHEDULE!)
**Branch:** `feature/defect-reporting`
**Goal:** Minimum 5 defects documented with evidence
**Status:** ✅ DONE - 6 defects documented!

### PRIORITY 1: Document Known Issues ✅ COMPLETE
- [x] Complete DEF-001 in `docs/defects.md` (Direct URL fails)
- [x] Complete DEF-002 in `docs/defects.md` (Last pagination broken)

### PRIORITY 2: Find 3+ New Defects ✅ COMPLETE (Found 4!)
- [x] DEF-003: Filter lost after pagination (High severity!)
- [x] DEF-004: Pagination skips pages at boundaries
- [x] DEF-005: Page refresh loses state
- [x] DEF-006: Outrageous page numbers displayed
- [x] Screenshots captured in `docs/images/`
- [x] Simple, clean format (6 lines per bug)

### 🚦 Phase Gate 4 Review ✅ PASSED
- [x] ✅ 6 defects documented (exceeds 5 minimum)
- [x] ✅ Clear reproduction steps for all
- [x] ✅ Screenshot evidence for 3 defects
- [x] ✅ 3 High severity + 3 Medium (exceeds requirement)

**Success Metric:** ✅ ACHIEVED - Professional defect reports ready

**PHASE 4 SKIPPED** - Already completed during Phase 2 exploration!

---

## Phase 5: FOUNDATION - README Documentation (2-3 hours) 🔴 CRITICAL
**Branch:** `feature/documentation`
**Goal:** Answer ALL 8 required questions in README
**Time Budget:** 2-3 hours MAX

### PRIORITY 1: README.md - Answer ALL 8 Questions (2-2.5 hours) 🚨 DO THIS
**Must have ALL sections - this is 25% of your score**

- [ ] **1. Testing Strategy** (15 min)
  - Summary from `docs/test-strategy.md`
  - Risk-based approach explained
  - WHY this strategy

- [ ] **2. Test Cases Overview** (30 min) ⭐ MOST IMPORTANT
  - List test cases from `docs/test-cases.md`
  - **WHY each case chosen** - this is critical!
  - Reference to full details in docs/

- [ ] **3. Framework Information** (15 min)
  - Python 3.13, Pytest, Selenium/Playwright
  - Key libraries and versions
  - Architecture: Simple Page Object Model
  - Reference `docs/design-decisions.md`

- [ ] **4. How to Run Tests** (30 min)
  - Prerequisites (Python, browser, etc.)
  - Installation: `pip install -e .`
  - Run: `make test` or `pytest`
  - View reports: `htmlcov/index.html`
  - Clear, step-by-step instructions

- [ ] **5. Test Design Techniques** (15 min)
  - BVA, EP, Negative Testing used
  - Where applied (reference test cases)
  - WHY these techniques

- [ ] **6. Coding Patterns** (15 min)
  - Page Object Model (simple)
  - Pytest fixtures
  - WHY: Maintainability without over-engineering
  - Reference `docs/design-decisions.md`

- [ ] **7. Defects Found** (15 min)
  - Summary: 5+ defects
  - Severity breakdown
  - Link to `docs/defects.md`

- [ ] **8. CI Integration Approach** (15 min)
  - GitHub Actions (already implemented!)
  - Pipeline: quality checks → tests
  - Triggers: push, PR
  - Future: parallel execution, browser matrix
  - Reference `.github/workflows/ci.yml`

### PRIORITY 2: Documentation Review & Links (30 min) 🚨 CRITICAL
- [ ] **Review all markdown files for staleness** (docs written BEFORE code)
  - [ ] `docs/test-strategy.md` - Still aligned with implementation plan?
  - [ ] `docs/test-cases.md` - Test cases still relevant for Phase 3?
  - [ ] `docs/requirements.md` - Requirements accurate after exploration?
  - [ ] `docs/defects.md` - All 6 defects still reproducible?
  - [ ] `docs/design-decisions.md` - Decisions still valid?
- [ ] **Add links in README to detailed docs**
  - [ ] Testing Strategy → `docs/test-strategy.md`
  - [ ] Test Cases → `docs/test-cases.md`
  - [ ] Requirements → `docs/requirements.md`
  - [ ] Defects → `docs/defects.md`
  - [ ] Design Decisions → `docs/design-decisions.md`
  - [ ] Framework Info → `pyproject.toml`
  - [ ] CI/CD → `.github/workflows/ci.yml`
- [ ] Proofread README
- [ ] Test all commands work
- [ ] Professional formatting

### 🚦 Phase Gate 5 Review (10 min)
- [ ] README has ALL 8 sections
- [ ] Clear, complete answers
- [ ] Professional presentation
- [ ] Commands tested and work

**Success Metric:** Anyone can understand and run tests from README alone

**DEFER TO LATER (if time):**
- Expand test strategy document
- Add more test case details
- Create separate ci-integration.md
- Add diagrams/screenshots to README

---

## Phase 6: CI Strategy Document ✅ COMPLETED (v0.2.0)
**Branch:** `feature/ci-enhancements`
**Goal:** Show you understand CI/CD

- [x] ✅ **IMPLEMENTED:** GitHub Actions CI workflow (`.github/workflows/ci.yml`)
- [x] CI tool choice: **GitHub Actions**
- [x] Pipeline stages: checkout → setup Python → install deps → quality checks → tests
- [x] Triggers: push, pull_request
- [ ] Document CI approach in README or docs/ci-integration.md
- [ ] Enhance workflow with:
  - [ ] Parallel execution strategy
  - [ ] Report artifacts
  - [ ] Notifications
  - [ ] Scheduled runs

**Success Metric:** ✅ CI pipeline implemented and running on GitHub

---

## Phase 6: FOUNDATION - Final Polish (1-2 hours) 🔴 CRITICAL
**Branch:** `feature/polish` → merge to `develop` → release to `main`
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

### 🚦 Phase Gate 6: Final Delivery Check
- [ ] All foundation tests PASS
- [ ] All documentation COMPLETE (8 sections)
- [ ] Minimum 5 defects documented
- [ ] CI pipeline GREEN
- [ ] Repo clean and professional
- [ ] README comprehensive
- [ ] Can clone fresh and run successfully

**Success Metric:** Professional, complete FOUNDATION deliverable ready for review

**IF TIME REMAINS - EXPAND:**
- Add more test cases (Medium priority)
- Find additional defects (beyond 5)
- Enhance documentation
- Add more exploratory tests
- Improve test coverage

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
- [ ] `docs/defects.md` - Defect reports with evidence
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
| Browser Library (Selenium/Playwright) | Choice pending Phase 3 implementation | 30 min |
| API Validation (comprehensive) | UI behavior priority, 1-2 examples only | 2-3 hrs |
| Extended Test Scope | Foundation = 8-10 tests, defer Type/Metadata filters | 6 hrs (15+ tests) |
| Cross-Browser Matrix | Chrome only, not Firefox/Safari/Edge | 1-2 hrs |

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
