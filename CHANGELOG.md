# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- xfail test philosophy documentation in test-strategy.md
- Test results interpretation section in README.md
- Clarifying comments in conftest.py about xfail usage
- Requirements traceability diagram in README.md (shows source documents → deliverables flow)
- Requirements origin section in ai-qa-testing.md (explains PDF + app exploration sources)
- Comprehensive rubric clarification document (docs/rubric-xfail-clarification.md)
- "How Traceability Tags Work" section in README.md with concrete YAML example
- Explanation of rubric AI evaluation role in automated validation (0-100 score)
- Claude Code dependency analysis in ai-qa-testing.md (what requires CLI vs. portable)
- API migration path documentation (Claude Code CLI → Anthropic API automation)

### Changed
- Enhanced documentation to clarify xfail tests indicate application bugs, not test implementation issues
- Reorganized README with traceability as first major section after header
- Replaced ASCII flowchart with structured STEP format (PDF-safe rendering)
- Clarified requirements.yml header to explain "PDF" citations refer to assignment document

## [1.0.0] - 2025-10-04

### Summary
**Foundation Complete - First Production Release**
- All assignment requirements met (84/100 rubric score)
- 8 test cases with WHY documentation + 5 defects documented
- Complete documentation (README + 6 supporting docs)
- CI/CD pipeline passing

### Added (v0.3.0 - Test Implementation)
- 8 foundation test cases in `tests/test_foundation.py` with WHY explanations
- Page Object Model implementation (`src/movie_db_qa/pages/discover_page.py`)
- Test documentation (`docs/test-strategy.md`, `docs/test-cases.md`)
- HTML + coverage test reporting
- Logging with lazy % formatting throughout
- Screenshot capture on test failure
- Tests: 2 pass, 4 xfail, 1 xpass, 1 skip

### Added (v0.4.0 - API Validation)
- Playwright network interception for TMDB API validation
- API assertions in 3 tests (Popular, Trending, Pagination)
- Screenshot capture demonstration (`docs/images/example-test-failure-screenshot.png`)
- CI fix: Playwright browser installation in GitHub Actions

### Added (v0.5.0 - Planning & Documentation)
- CLAUDE.md with 5 TODO.md workflow rules for AI agent
- v1.1.0 Traceability Infrastructure design (`docs/ai-qa-testing.md`)
- TODO.md phase naming with VERSION numbers and branch names
- HTML green styling for completed phases

### Changed (v0.4.0)
- Magic numbers eliminated: moved to `src/movie_db_qa/utils/config.py`
- Test configuration centralized in config.py
- Documentation updated with API validation sections

### Changed (v0.5.0)
- TODO.md phases renamed: v0.1.0 through v0.5.0 (VERSION-based naming)
- Branch preservation policy: "KEEPING REMOTE BRANCH" explicit in all steps
- .gitignore: CLAUDE.md now tracked (removed from ignore)

### Achieved
- Rubric progression: v0.3.0 (78/100) → v0.4.0 (84/100) → v1.0.0 (foundation complete)
- All assignment requirements satisfied
- Professional deliverable ready for evaluation

## [0.2.0] - 2025-10-03

### Added
- Python 3.13 project structure with pyproject.toml
- Build automation via Makefile (quality, test, format, lint, typecheck targets)
- Quality tools configuration: ruff (format/lint), mypy (typecheck), pytest (testing)
- CI/CD workflow with GitHub Actions
- Git-flow branching model configuration
- Pre-commit hooks for code quality enforcement
- Project documentation and assignment materials
- Basic package structure with initial tests
- VERSION file for version management

### Changed
- Updated .gitignore to exclude development artifacts
