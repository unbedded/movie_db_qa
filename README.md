# movie_db_qa - QA Automation Assignment

> **Rapyuta Robotics** - QA Automation Assignment for TMDB Discovery Application

[![CI](https://github.com/unbedded/movie_db_qa/workflows/CI/badge.svg)](https://github.com/unbedded/movie_db_qa/actions)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**Application Under Test:** [https://tmdb-discover.surge.sh/](https://tmdb-discover.surge.sh/)

---

## Table of Contents

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
│   ├── defects.md                            # Bug reports with evidence (6 defects)
│   ├── design-decisions.md                   # Design rationale and trade-offs
│   ├── requirements.md                       # Reverse-engineered requirements
│   ├── test-cases.md                         # Test case specifications (Phase 2)
│   ├── test-strategy.md                      # Testing approach (Phase 2)
│   ├── images/                               # Screenshots for defect evidence
│   │   ├── BugPageRefresh_1of1.png
│   │   └── BugPagination_outragousPageNum_2of2.png
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
│   ├── conftest.py                           # Pytest fixtures (Phase 3)
│   ├── test_filtering.py                     # Category/search filter tests
│   ├── test_pagination.py                    # Navigation and boundary tests
│   ├── test_negative.py                      # Error handling edge cases
│   ├── test_sanity.py                        # Framework sanity checks
│   └── github_ci_errors/                     # CI debugging logs
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
├── TODO.md                                   # Project plan and progress tracker
├── CHANGELOG.md                              # Version history
├── CLAUDE.md                                 # AI coding standards
├── VERSION                                   # Semantic version (0.2.0)
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
open htmlcov/index.html  # Coverage report
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
| Browser Automation | selenium/playwright | TBD | Web UI testing (Phase 3 decision) |
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
tests/conftest.py          # Pytest fixtures
```

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

### Viewing Reports

```bash
# Coverage report (HTML)
open htmlcov/index.html

# Test report (console output during test run)
pytest -v --tb=short
```

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

**Total:** 6 defects (exceeds 5 minimum requirement ✅)
- **Known issues:** 2 (disclosed in assignment)
- **New defects:** 4 (found during exploratory testing)

### Severity Breakdown

| Severity | Count | Defect IDs |
|----------|-------|------------|
| High | 3 | DEF-001, DEF-002, DEF-003 |
| Medium | 3 | DEF-004, DEF-005, DEF-006 |

### Notable Defects

- **DEF-003 (High):** Filter lost after pagination - Users can't browse filtered results across pages
- **DEF-005 (Medium):** Page refresh loses state - Can't bookmark or share filtered views
- **DEF-006 (Medium):** Outrageous page numbers displayed - Shows impossible page counts

📖 **[View complete defect reports →](docs/defects.md)**

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
| [docs/defects.md](docs/defects.md) | Bug reports with reproduction steps and evidence |
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
