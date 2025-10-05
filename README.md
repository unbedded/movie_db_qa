# movie_db_qa - QA Automation Assignment

> **Rapyuta Robotics** - QA Automation Assignment for TMDB Discovery Application

[![CI](https://github.com/unbedded/movie_db_qa/workflows/CI/badge.svg)](https://github.com/unbedded/movie_db_qa/actions)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**Application Under Test:** [https://tmdb-discover.surge.sh/](https://tmdb-discover.surge.sh/)

---

## Table of Contents

- [🔗 Requirements Traceability](#-requirements-traceability)
- [📁 Project Structure](#-project-structure)
- [🎯 Quick Start](#-quick-start)
- [📋 Testing Strategy](#-testing-strategy)
- [🧪 Test Cases Overview](#-test-cases-overview)
- [🛠️ Framework Information](#️-framework-information)
- [🚀 How to Run Tests](#-how-to-run-tests)
- [🎨 Test Design Techniques](#-test-design-techniques)
- [🏗️ Coding Patterns](#️-coding-patterns)
- [🐛 Defects Found](#-defects-found)
- [🔄 CI Integration Approach](#-ci-integration-approach)
- [📚 Documentation](#-documentation)

---

## 🔗 Requirements Traceability

This project demonstrates **AI-powered traceability** from source documents to deliverables:

### Traceability Flow

**STEP 1: Source Documents**
- `reference/rr_qa_automation_assignment_.pdf` - Assignment requirements (explicit)
- `docs/requirements.md` - Reverse-engineered from app exploration (inferred)

**STEP 2: Structured Requirements**
- `rubric/requirements.yml` - Machine-readable YAML format with **traceability tags**:
  - `rubric: ["R-1", "R-2"]` - Links to rubric scoring criteria
  - `design: ["DD-4.1"]` - Links to design decision sections
  - `tests: ["TC-FLT-CAT-001"]` - Links to test case IDs
  - `artifacts: ["tests/test_foundation.py::test_name"]` - Links to implementations
  - These tags appear throughout all documentation for cross-referencing

**STEP 3: Design & Test Specifications**
- `docs/design-decisions.md` - Technical decisions with `[REQ-XXX]` tags
- `docs/test-cases.md` - Test specifications with WHY explanations
- `docs/test-strategy.md` - Test approach and techniques

**STEP 4: Automated Implementation**
- `tests/test_foundation.py` - 8 foundation test cases
- `src/movie_db_qa/pages/` - Page Object Model
- `tests/conftest.py` - Fixtures, logging, API validation

**STEP 5: Artifacts & Evidence**
- `report/index.html` - HTML test report
- `htmlcov/index.html` - Coverage report
- `docs/defects-manual-found.md` - 5 defects with screenshots
- `screenshots/*.png` - Automated failure captures

**STEP 6: Manual & AI-Assisted Validation**
- `rubric/requirements.yml` - Structured requirements enable manual traceability verification
  - 17 requirements with full source → design → tests → artifacts linking
  - Tags (`R-1`, `DD-4.1`, `TC-XXX`) allow manual cross-reference validation
- `rubric/` - **AI analysis scores project 0-100** against assignment criteria
  - Evaluates all rubric criteria from `rubric/eval-rubric.md`
  - Validates traceability completeness manually via hot links
  - Generates scored reports: `rubric/reports/phase5-rubric-eval.md` (91/100)

**Future Enhancement:** `make audit` - Automated traceability validation script
  - Would validate all requirements traced to design docs
  - Would verify all artifacts exist at specified paths
  - Would detect orphaned implementations (tests without requirements)
  - See design in `docs/ai-qa-testing.md` (not yet implemented)

### How Traceability Tags Work

Example from `rubric/requirements.yml`:
```yaml
FLT-CAT-1.2:
  desc: "Trending filter displays trending content"
  source: "PDF p.1 'Categories: Popular, Trending...'"
  rubric: ["R-1", "R-2"]        # → Links to rubric/eval-rubric.md criteria
  design: ["DD-4.1"]             # → Links to docs/design-decisions.md sections
  tests: ["TC-FLT-CAT-002"]      # → Links to docs/test-cases.md test case
  artifacts:
    - "tests/test_foundation.py::test_trending_filter_works"  # → Actual code
    - "docs/test-cases.md#TC-FLT-CAT-002"                     # → Documentation
```

**These tags appear throughout all project files:**
- Design docs reference `[REQ-FLT-CAT-1.2]` and `[DD-4.1]`
- Test cases reference `TC-FLT-CAT-002` and trace to requirements
- Rubric criteria `R-1`, `R-2` validated against all linked artifacts
- Manual verification via hot links in rubric evaluation reports

**Key Innovation:** Requirements as structured YAML enables manual traceability verification and AI-powered rubric scoring (with future automation potential via `make audit`).

📖 **[Read full paradigm shift explanation →](docs/ai-qa-testing.md)**

---

## 📁 Project Structure

**Philosophy:** Clean separation of concerns - code, tests, docs, configuration, and evaluation artifacts

```
movie_db_qa/
│
├── .github/
│   └── workflows/
│       └── ci.yml                            # GitHub Actions CI/CD pipeline
│
├── docs/                                     # 📚 Documentation
│   ├── defects-manual-found.md                            # Bug reports with evidence (6 defects)
│   ├── design-decisions.md                   # Design rationale and trade-offs
│   ├── requirements.md                       # Reverse-engineered requirements
│   ├── test-cases.md                         # Test case specifications (Phase 2)
│   ├── test-strategy.md                      # Testing approach (Phase 2)
│   ├── images/                               # Screenshots for defect evidence
│   │   ├── BugPageRefresh_1of1.png
│   │   └── BugPagination_outragousPageNum_2of2.png
│   ├── reports/                              # 📊 Sample test/coverage reports
│   │   ├── test-report-v0.3.0.html           # Sample test results report
│   │   └── coverage-report-v0.3.0.html       # Sample coverage report
│   └── reference/                            # Assignment reference materials
│       ├── assignment-overview.md
│       └── priorities.md
│
├── src/                                      # 🔧 Source Code
│   └── movie_db_qa/
│       ├── __init__.py
│       ├── pages/                            # Page Object Model (Phase 3)
│       │   ├── base_page.py                  # Common page interactions
│       │   └── discover_page.py              # TMDB discovery page
│       └── utils/                            # Helper utilities (Phase 3)
│           ├── logger.py                     # Logging configuration
│           └── config.py                     # Settings management
│
├── tests/                                    # 🧪 Test Suite
│   ├── conftest.py                           # Pytest fixtures + screenshot capture
│   ├── test_foundation.py                    # 8 foundation test cases (Phase 3)
│   ├── test_sanity.py                        # Framework sanity checks
│   └── github_ci_errors/                     # CI debugging logs
│
├── screenshots/                              # 📸 Test Failure Screenshots (gitignored)
│   └── *.png                                 # Auto-captured on test failure
│
├── logs/                                     # 📋 Test Execution Logs (gitignored)
│   └── test_execution.log                    # Full test run trace with timestamps
│
├── rubric/                                   # 📊 Evaluation Framework
│   ├── eval-rubric.md                        # 100-point scoring criteria
│   ├── eval-prompt.md                        # AI evaluation instructions
│   └── reports/                              # Self-assessment reports by phase
│
├── reference/                                # 📄 Assignment Materials
│   └── rr_qa_automation_assignment_.pdf      # Original assignment PDF
│
├── report/                                   # 📈 Test Reports (Phase 3)
│   └── README.md                             # Report generation instructions
│
├── .github/workflows/ci.yml                  # CI/CD pipeline
├── .pre-commit-config.yaml                   # Git hooks for quality gates
├── pyproject.toml                            # Dependencies + tool configs
├── Makefile                                  # Build automation (make test, make quality)
├── rubric/requirements.yml                          # 🔗 Structured requirements (traceability)
├── TODO.md                                   # Project plan and progress tracker
├── CHANGELOG.md                              # Version history
├── CLAUDE.md                                 # AI coding standards
├── VERSION                                   # Semantic version (1.0.0)
└── README.md                                 # This document
```

### Key Directories

| Directory | Purpose | Status |
|-----------|---------|--------|
| `.github/workflows/` | CI/CD pipeline configuration | ✅ Complete |
| `docs/` | All documentation (requirements, strategy, test cases, defects) | ✅ Phase 2 |
| `src/movie_db_qa/` | Application code (Page Objects, utilities) | ⏳ Phase 3 |
| `tests/` | Test implementations and fixtures | ⏳ Phase 3 |
| `rubric/` | Evaluation framework and self-assessments | ✅ Complete |
| `reference/` | Assignment artifacts (read-only) | ✅ Complete |
| `report/` | Test execution reports (HTML, coverage) | ⏳ Phase 3 |

### Configuration Files

| File | Purpose | Used By |
|------|---------|---------|
| `pyproject.toml` | Dependencies, tool configs (ruff, mypy, pytest) | `pip`, `pytest`, `ruff`, `mypy` |
| `Makefile` | Build automation (`make test`, `make quality`) | Developer, CI |
| `.pre-commit-config.yaml` | Git hooks (quality checks before commit) | `pre-commit` tool |
| `.github/workflows/ci.yml` | CI pipeline (quality → tests → coverage) | GitHub Actions |

---

## 🎯 Quick Start

**Get up and running in 5 minutes:**

```bash
# 1. Clone repository
git clone git@github.com:unbedded/movie_db_qa.git
cd movie_db_qa

# 2. Install dependencies
pip install -e .[dev]

# 3. Run quality checks
make quality

# 4. Run tests
make test-full

# 5. View reports
open htmlcov/index.html        # Fresh coverage report
open report/index.html          # Fresh test results report
cat logs/test_execution.log     # Test execution log file

# Or view sample reports (v0.3.0 baseline):
open docs/reports/test-report-v0.3.0.html
open docs/reports/coverage-report-v0.3.0.html
```

---

## 📋 Testing Strategy

**Approach:** Risk-based test prioritization using formal test design techniques

**Summary:**
- **Focus:** Core filters (Popular, Trending), pagination, and known issues
- **Techniques:** Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Negative Testing
- **Scope:** 8-10 Critical/High priority test cases (foundation), defer Medium/Low for time constraint
- **Philosophy:** "Small scope, deep quality" - demonstrate QA thinking over exhaustive coverage

**Priority Framework:**
- **Critical:** Category filters (Popular, Trending, Newest, Top Rated) - Primary user workflows
- **High:** Pagination, Search, Type filters - Essential navigation
- **Medium:** Year/Rating/Genre filters - Advanced features (deferred)
- **Low:** UI polish, edge combinations - Nice-to-have (out of scope)

📖 **[Read full test strategy →](docs/test-strategy.md)**
📖 **[View requirements traceability →](docs/requirements.md)**
📖 **[See design decisions →](docs/design-decisions.md)**

---

## 🧪 Test Cases Overview

**Foundation: 8-10 test cases** (Critical/High priority only)

### Category Filter Tests (2-3 cases)
- **TC-FLT-CAT-001:** Popular filter displays correct results
  - **WHY:** Primary user workflow, most common filter
- **TC-FLT-CAT-002:** Trending filter works independently
  - **WHY:** Second most used feature, validates filter switching

### Pagination Tests (2-3 cases)
- **TC-PAG-001:** Navigate to page 2 successfully
  - **WHY:** Basic pagination validation
- **TC-PAG-002:** Last page boundary handling
  - **WHY:** Known issue (DEF-002), BVA technique
- **TC-PAG-003:** Filter persistence across pagination
  - **WHY:** Found defect (DEF-003), critical UX issue

### Negative Tests (2 cases)
- **TC-NEG-001:** Direct URL slug access fails gracefully
  - **WHY:** Known issue (DEF-001), negative testing
- **TC-NEG-002:** Invalid page numbers handled
  - **WHY:** Error handling validation, BVA technique

### Combined Filter Tests (1-2 cases, if time)
- **TC-CMB-001:** Popular + Movies filter combination
  - **WHY:** Real-world usage, decision table technique

📖 **[View complete test cases →](docs/test-cases.md)**
📖 **[See requirements mapping →](docs/requirements.md)**

---

## 🛠️ Framework Information

### Technology Stack

| Component | Library | Version | Purpose |
|-----------|---------|---------|---------|
| Language | Python | 3.13 | Test implementation |
| Test Framework | pytest | ≥7.0 | Test runner and assertions |
| Coverage | pytest-cov | ≥4.0 | Code coverage reporting |
| Browser Automation | Playwright | ≥1.40 | Web UI testing + API interception |
| Test Plugin | pytest-playwright | ≥0.4 | Playwright integration |
| Linter | ruff | ≥0.1.0 | Fast Python linter |
| Type Checker | mypy | ≥1.0 | Static type checking |
| Formatter | black | ≥23.0 | Code formatting |

### Architecture

**Pattern:** Simple Page Object Model (POM)

**Rationale:**
- **Maintainability:** Separates test logic from page interactions
- **Readability:** Tests read like business scenarios
- **Balance:** Professional pattern without over-engineering

**Structure:**
```
src/movie_db_qa/pages/    # Page objects
tests/test_*.py            # Test cases
tests/conftest.py          # Pytest fixtures + API interception
```

### API Validation

**Playwright Network Interception** - Tests validate browser API calls to TMDB endpoints:

```python
# conftest.py - Automatic API call capture
page.on("request", handle_request)  # Intercept all network requests
page.api_calls  # List of captured API calls

# test_foundation.py - API assertions
api_calls = page.api_calls
movie_calls = [call for call in api_calls if "/movie/" in call["url"]]
assert len(movie_calls) > 0, "Should make API call to TMDB"
```

**Validated Endpoints:**
- `/movie/popular?page=1` - Popular filter
- `/movie/trending` - Trending filter
- `/movie/popular?page=2` - Pagination

**Benefits:**
- Verifies UI actions trigger correct backend calls
- Validates query parameters (page, sort_by, filters)
- Detects API integration issues early

📖 **[View design decisions →](docs/design-decisions.md)**
📖 **[See pyproject.toml →](pyproject.toml)**

---

## 🚀 How to Run Tests

### Prerequisites

- **Python 3.13+** ([Download](https://www.python.org/downloads/))
- **Git** ([Download](https://git-scm.com/downloads))
- **Chrome/Firefox browser** (for Phase 3 web tests)

### Installation

```bash
# Clone repository
git clone git@github.com:unbedded/movie_db_qa.git
cd movie_db_qa

# Install dependencies (development mode)
pip install -e .[dev]

# Install pre-commit hooks (optional but recommended)
pre-commit install
```

### Running Tests

```bash
# Quick test run (no coverage)
make test

# Full test run with coverage
make test-full

# Run specific test file
pytest tests/test_sanity.py -v

# Run with detailed output
pytest -v -s

# Run quality checks (ruff + mypy + black)
make quality
```

### Understanding Test Results

**Current test results:** 2 pass, 4 xfail, 1 xpass, 1 skip

**What this means:**
- ✅ **2 passing** - Features working correctly (Popular filter, Trending filter)
- ✅ **4 xfail** - Known app bugs automated (DEF-001, DEF-002, DEF-003, DEF-007)
- ⚠️ **1 xpass** - Previously failing test now passing (investigate if bug fixed)
- ⏸️ **1 skip** - Deferred test (out of scope)

**CRITICAL:** Tests marked `xfail` are **INTENTIONALLY expected to fail** due to known application bugs, NOT test implementation issues. This is proper pytest usage for:
- Automating defect reproduction (each xfail = automated bug validation)
- Maintaining test coverage on buggy features
- Preventing false CI failures while documenting expected behavior

**Total functional test coverage: 7/8 tests execute (88% execution rate)**

See [Test Strategy - xfail Philosophy](docs/test-strategy.md#xfail-test-philosophy-critical-clarification) for detailed explanation.

### Viewing Reports

```bash
# 1. Fresh HTML test report
open report/index.html

# 2. Fresh coverage report
open htmlcov/index.html

# 3. Test execution log file
cat logs/test_execution.log

# 4. Failure screenshots (auto-captured)
ls screenshots/  # Only populated on test failures

# Or view sample reports (v0.3.0 baseline):
open docs/reports/test-report-v0.3.0.html
open docs/reports/coverage-report-v0.3.0.html
open docs/images/example-test-failure-screenshot.png
```

**Screenshot Capture:**
- Automatically captures screenshots on test failure
- Saved to `screenshots/` directory (gitignored)
- Example: `docs/images/example-test-failure-screenshot.png`
- Triggered by pytest hook in `tests/conftest.py`

### CI Pipeline

Tests run automatically on every push/PR via GitHub Actions:
```bash
# View CI status
https://github.com/unbedded/movie_db_qa/actions
```

📖 **[View CI configuration →](.github/workflows/ci.yml)**

---

## 🎨 Test Design Techniques

### Techniques Applied

| Technique | Application | Example Test Cases |
|-----------|-------------|-------------------|
| **Boundary Value Analysis (BVA)** | Pagination limits, rating ranges | Last page, page 1, invalid page numbers |
| **Equivalence Partitioning (EP)** | Valid/invalid inputs, categories | Valid years (1900-2025), invalid (-1, 9999) |
| **Decision Tables** | Combined filter scenarios | Year + Rating + Genre interactions |
| **Exploratory Testing** | New defect discovery | Found DEF-003 through DEF-006 |
| **Negative Testing** | Error handling, edge cases | Direct URL access (DEF-001) |

### Rationale

**WHY these techniques?**
- **BVA:** Catches off-by-one errors in pagination, filters
- **EP:** Reduces test count while maintaining coverage
- **Decision Tables:** Validates complex filter interactions
- **Exploratory:** Finds bugs formal techniques miss
- **Negative:** Ensures graceful error handling

📖 **[View test strategy details →](docs/test-strategy.md)**
📖 **[See test case specifications →](docs/test-cases.md)**

---

## 🏗️ Coding Patterns

### Page Object Model (POM)

**Implementation:**
```python
# Page Object
class DiscoverPage:
    def select_popular_filter(self):
        """Click Popular filter and wait for results"""

# Test Case
def test_popular_filter(discover_page):
    discover_page.select_popular_filter()
    assert discover_page.get_results_count() > 0
```

**Benefits:**
- ✅ **Maintainability:** UI changes isolated to page objects
- ✅ **Readability:** Tests read like business scenarios
- ✅ **Reusability:** Common actions shared across tests

### Pytest Fixtures

**Setup/Teardown:**
```python
# conftest.py
@pytest.fixture
def browser():
    driver = setup_browser()
    yield driver
    driver.quit()
```

**Why POM + Fixtures?**
- Industry-standard patterns
- Balance between simplicity and professionalism
- No over-engineering for 2-day assignment scope

📖 **[View architecture decisions →](docs/design-decisions.md#4-code-architecture--patterns)**

---

## 🐛 Defects Found

### Summary

**Total:** 5 defects (meets 5 minimum requirement ✅)
- **Known issues:** 2 (disclosed in assignment)
- **New defects:** 3 (found during exploratory testing)

### Severity Breakdown

| Severity | Count | Defect IDs |
|----------|-------|------------|
| High | 3 | DEF-001, DEF-002, DEF-003 |
| Medium | 2 | DEF-004, DEF-005 |

### Notable Defects

- **DEF-002 (High):** Filter + Last page pagination broken - High page numbers cause errors when clicked
- **DEF-003 (High):** Filter lost after pagination - Users can't browse filtered results across pages
- **DEF-005 (Medium):** Page refresh loses state - Can't bookmark or share filtered views

📖 **[View complete defect reports →](docs/defects-manual-found.md)**

---

## 🔄 CI Integration Approach

### Implementation: GitHub Actions ✅

**Status:** Fully implemented (bonus - assignment only required documentation)

**Pipeline:** `.github/workflows/ci.yml`

```yaml
Stages:
1. Checkout code
2. Setup Python 3.13
3. Install dependencies
4. Quality checks (ruff + mypy + black)
5. Run tests with coverage
6. (Future) Upload artifacts
```

**Triggers:**
- Push to `main`, `develop`, `feature/*` branches
- Pull requests to `main`, `develop`
- Manual workflow dispatch

**Quality Gates:**
- ✅ Ruff linting must pass
- ✅ MyPy type checking must pass
- ✅ Black formatting must pass
- ✅ All tests must pass

### Future Enhancements

- **Parallel execution:** Matrix strategy for Python 3.10, 3.11, 3.12, 3.13
- **Browser matrix:** Test on Chrome, Firefox, Safari
- **Scheduled runs:** Nightly regression tests
- **Notifications:** Slack/email on failures
- **Report artifacts:** Upload HTML reports to GitHub Actions

📖 **[View CI configuration →](.github/workflows/ci.yml)**
📖 **[Read CI/CD strategy →](docs/design-decisions.md#9-cicd-strategy)**

---

## 📚 Documentation

### Project Documentation

| Document | Description |
|----------|-------------|
| [README.md](README.md) | This document - project overview and quick start |
| [TODO.md](TODO.md) | Project plan, phases, and progress tracker |
| [CHANGELOG.md](CHANGELOG.md) | Version history and release notes |
| [VERSION](VERSION) | Current semantic version (0.2.0) |

### Technical Documentation

| Document | Description |
|----------|-------------|
| [docs/requirements.md](docs/requirements.md) | Reverse-engineered requirements with semantic IDs |
| [docs/test-strategy.md](docs/test-strategy.md) | Testing approach and rationale |
| [docs/test-cases.md](docs/test-cases.md) | Test case specifications with WHY explanations |
| [docs/defects-manual-found.md](docs/defects-manual-found.md) | Bug reports with reproduction steps and evidence |
| [docs/design-decisions.md](docs/design-decisions.md) | Design rationale, alternatives, and trade-offs |

### Configuration

| File | Description |
|------|-------------|
| [pyproject.toml](pyproject.toml) | Project dependencies and tool configurations |
| [Makefile](Makefile) | Build automation commands |
| [.pre-commit-config.yaml](.pre-commit-config.yaml) | Git hooks for quality gates |
| [.github/workflows/ci.yml](.github/workflows/ci.yml) | CI/CD pipeline configuration |

### Evaluation

| Document | Description |
|----------|-------------|
| [rubric/eval-rubric.md](rubric/eval-rubric.md) | 100-point scoring criteria |
| [rubric/eval-prompt.md](rubric/eval-prompt.md) | AI evaluation instructions |

---

## 🤝 Development Workflow

### Git-Flow Branching Model

```
main              # Production releases (v0.2.0, v1.0.0)
develop           # Integration branch
feature/*         # Feature development branches
```

**Assignment Policy:** Keep ALL remote branches to demonstrate development progression and version control maturity (evaluator requirement).

### Branch Tracking

| Branch | Status | Purpose | Commits | Preserved |
|--------|--------|---------|---------|-----------|
| `main` | ✅ Current | Production releases | v0.2.0 tag | Yes |
| `develop` | ✅ Current | Integration branch | Latest work | Yes |
| `feature/update-todo` | ✅ Merged | Phase 2 documentation & foundation | eed4fa7 | **Remote kept** ✅ |
| `feature/test-impl` | ⏳ Current | Phase 3 test implementation | TBD | Will keep |

**Key Commits:**
- `eed4fa7` - Phase 2 complete: docs + foundation setup (feature/update-todo)
- `3f06fa3` - v0.2.0 release (release/0.2.0 → main)
- `3d07371` - Initial framework setup
- `1b14319` - Initial commit

### Making Changes

```bash
# 1. Create feature branch
git checkout -b feature/my-feature develop

# 2. Make changes and commit
make quality      # Run quality checks
make test-full    # Run tests
git add .
git commit -m "feat: add new feature"

# 3. Push and create PR
git push -u origin feature/my-feature
# Create PR: feature/my-feature → develop
```

### Quality Gates

- ✅ Pre-commit hooks run automatically
- ✅ CI pipeline runs on push
- ✅ All checks must pass before merge

---

## 📊 Project Status

**Current Phase:** Phase 2 - Test Design (in progress)
**Version:** 0.2.0
**Time Remaining:** 1.5 days (~12-15 hours)

### Completed ✅
- Phase 1: Framework setup (v0.2.0 released)
- Requirements documented (reverse-engineered)
- 6 defects found and documented
- CI/CD pipeline implemented

### In Progress 🔄
- Phase 2: Test strategy and test cases
- Documentation review for staleness

### Upcoming ⏳
- Phase 3: Test implementation (4-5 hours)
- Phase 5: Complete README (this document)
- Phase 6: Final polish and delivery

📖 **[View detailed plan →](TODO.md)**

---

## 📝 Assignment Context

**Assignment:** Rapyuta Robotics QA Automation Take-Home
**Application:** [TMDB Discovery](https://tmdb-discover.surge.sh/)
**Duration:** 2 days (24-30 hours)
**Philosophy:** "Frameworks matter less than you think. Better spend time polishing your deliverable as a whole."

**Required Deliverables:**
- ✅ Test automation framework
- ✅ Test cases with WHY explanations
- ✅ Minimum 5 defects documented
- ✅ Complete documentation (8 sections)
- ✅ CI integration approach

---

## 📄 License

This project is for assignment evaluation purposes only.

---

**Generated with ❤️ using Python 3.13 + Pytest**
**Last Updated:** 2025-10-04
