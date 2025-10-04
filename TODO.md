# QA Automation Assignment - Project Plan

> **Assignment Philosophy:** "Frameworks matter less than you think. Better spend time polishing your deliverable as a whole."

## 🎯 CRITICAL SUCCESS FACTORS

### What Scores High (Focus 80% of effort here)
1. **Test Case Design + Documentation** - WHY you chose these cases
2. **Clean, Maintainable Code** - Readable, well-structured
3. **Complete Documentation** - Answer all required questions
4. **Defect Reports** - Clear, with evidence
5. **Test Strategy** - Show your thinking

### What Matters Less (Don't overthink)
- Framework choice (pick what you know)
- Complex architecture
- Advanced patterns

---

## Phase 1: Quick Setup (2-3 hours MAX)
**Goal:** Get basic testing environment running fast

- [ ] Create GitHub repo: movie_db_qa
- [ ] Pick framework you know best (Playwright/Cypress/Selenium) - **30 min decision MAX**
- [ ] Pick language you know best (TypeScript/JavaScript/Python)
- [ ] `npm init` / `pip init` - basic project setup
- [ ] Install framework + reporter - **use defaults**
- [ ] Verify can run 1 dummy test
- [ ] Basic folder structure: `/tests`, `/docs`, `/reports`

**Success Metric:** Can run a test and see a report

---

## Phase 2: Test Design & Documentation (6-8 hours) 🔴 CRITICAL
**Goal:** Design test cases and document WHY

### Exploration & Analysis
- [ ] Manually explore https://tmdb-discover.surge.sh/ (30 min)
- [ ] Map all filtering options and behaviors
- [ ] Find and document defects (aim for 5+)
- [ ] Test pagination boundaries

### Test Case Design
- [ ] Create `docs/test-cases.md` with step-by-step tests
- [ ] Apply test design techniques:
  - [ ] Boundary Value Analysis (years, ratings)
  - [ ] Equivalence Partitioning (filter types)
  - [ ] Decision Tables (combined filters)
  - [ ] Exploratory (find bugs!)
- [ ] Document WHY each test case is important
- [ ] Prioritize: Critical, High, Medium, Low

### Test Strategy Document
- [ ] Write `docs/test-strategy.md`:
  - [ ] What are you testing and why?
  - [ ] Risk-based approach
  - [ ] Coverage goals
  - [ ] Which techniques and why?
  - [ ] What you're NOT testing (scope)

### 🚦 Phase Gate 2 Review
- [ ] Test cases are creative and justified
- [ ] Documentation explains the "WHY"
- [ ] Coverage addresses all features
- [ ] Found defects during exploration

**Success Metric:** Someone can read your test cases and understand your thinking

---

## Phase 3: Test Implementation (6-8 hours) 🔴 CRITICAL
**Goal:** Implement clean, working tests

### Framework Basics (Keep Simple!)
- [ ] Create 1-2 page objects (don't over-engineer)
- [ ] Setup/teardown helpers
- [ ] Simple logging utility
- [ ] Screenshot on failure

### Implement Tests
- [ ] **Filtering Tests** (Priority: High)
  - [ ] Category filters (Popular, Trending, Newest, Top Rated)
  - [ ] Title search
  - [ ] Type filter (Movies/TV Shows)
  - [ ] Year/Rating/Genre filters
  - [ ] Combined filters
- [ ] **Pagination Tests** (Priority: High)
  - [ ] Navigate pages 1-3
  - [ ] Last page (negative case)
- [ ] **Negative Tests** (Priority: High)
  - [ ] Direct URL slug access
  - [ ] Invalid inputs
  - [ ] Edge cases

### API Validation
- [ ] Intercept/monitor network calls
- [ ] Assert on key API responses
- [ ] Log API calls in tests

### Logging
- [ ] Log test start/end
- [ ] Log key actions
- [ ] Log API calls
- [ ] Log failures with context

### 🚦 Phase Gate 4 Review
- [ ] All tests run successfully
- [ ] Code is clean and readable
- [ ] Logging is working
- [ ] Reports generate (HTML + Console)

**Success Metric:** `npm test` or `pytest` runs all tests with clear output

---

## Phase 4: Defect Reporting (3-4 hours) 🔴 CRITICAL
**Goal:** Document defects clearly with evidence

- [ ] Create `docs/defects.md`
- [ ] Document each defect:
  - [ ] ID, Title, Severity, Priority
  - [ ] Steps to reproduce (clear!)
  - [ ] Expected vs Actual
  - [ ] Screenshots/evidence
  - [ ] Environment details
- [ ] Minimum 5 defects (2 known + 3 new)
- [ ] At least 1-2 medium/high severity

**Success Metric:** Developer could fix bugs from your reports

---

## Phase 5: Documentation (4-5 hours) 🔴 CRITICAL
**Goal:** Answer ALL required questions clearly

### README.md (Most Important!)
Must include these sections:

- [ ] **1. Testing Strategy**
  - What is your approach?
  - Why this strategy?

- [ ] **2. Test Cases Overview**
  - Which cases did you generate?
  - **WHY did you choose them?** (Critical!)

- [ ] **3. Framework Information**
  - Libraries used and versions
  - Architecture decisions

- [ ] **4. How to Run Tests**
  - Prerequisites
  - Installation steps
  - Run commands
  - View reports

- [ ] **5. Test Design Techniques**
  - Which techniques used?
  - Where applied?

- [ ] **6. Coding Patterns**
  - What patterns used?
  - Why chosen?

- [ ] **7. Defects Found**
  - Summary of defects
  - Link to detailed reports

- [ ] **8. CI Integration Approach** (document only)
  - How would you set up CI?
  - Pipeline stages
  - Tools (GitHub Actions/Jenkins)
  - Triggers and scheduling

### 🚦 Phase Gate 5 Review
- [ ] README answers ALL 8 questions
- [ ] Documentation is clear and complete
- [ ] Test cases are documented
- [ ] Defects are well-reported

**Success Metric:** Anyone can understand and run your tests from README

---

## Phase 6: CI Strategy Document (2-3 hours)
**Goal:** Show you understand CI/CD (don't implement!)

- [ ] Create `docs/ci-integration.md` or add to README
- [ ] Document approach:
  - [ ] CI tool choice (GitHub Actions/Jenkins/GitLab)
  - [ ] Pipeline stages (install → test → report)
  - [ ] Triggers (PR, push, scheduled)
  - [ ] Environment setup
  - [ ] Parallel execution strategy
  - [ ] Report artifacts
  - [ ] Notifications
  - [ ] Sample config (optional)

**Success Metric:** Shows understanding of CI/CD best practices

---

## Phase 7: Polish & Delivery (2-3 hours)
**Goal:** Final quality check

### Code Review
- [ ] Remove debug code
- [ ] Clean up comments
- [ ] Consistent naming
- [ ] Remove unused dependencies

### Testing
- [ ] Run full suite 3 times - verify stable
- [ ] Check both HTML and Console reports
- [ ] Verify screenshots captured on failure
- [ ] Test on clean machine (if possible)

### Documentation Review
- [ ] Proofread all docs
- [ ] Check all links work
- [ ] Verify commands in README work
- [ ] Ensure all required sections present

### Git & Delivery
- [ ] Review git history (meaningful commits)
- [ ] Final commit with all deliverables
- [ ] Verify repo is public
- [ ] Double-check repo name: movie_db_qa

### 🚦 Phase Gate 7: Final Delivery Check
- [ ] All tests pass
- [ ] All documentation complete
- [ ] All defects reported
- [ ] CI strategy documented
- [ ] Repo is clean and professional
- [ ] README is comprehensive
- [ ] Reports work correctly

**Success Metric:** Professional, complete deliverable ready for review

---

## 📋 DELIVERABLES CHECKLIST

Before submission, verify:

### Code Deliverables
- [ ] GitHub repo: movie_db_qa (public)
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
- [ ] `docs/ci-integration.md` - CI approach (or in README)

### Quality Checks
- [ ] Code is clean and maintainable
- [ ] Tests are reliable (not flaky)
- [ ] Documentation is complete and clear
- [ ] Found minimum 5 defects
- [ ] Easy to install and run
- [ ] Git history is professional

---

## ⏰ TIME ALLOCATION (24-30 hours total)

| Phase | Time | Why This Matters |
|-------|------|------------------|
| Setup | 2-3 hrs | Get unblocked fast |
| Test Design & Docs | 6-8 hrs | **HIGHEST SCORER** - shows thinking |
| Implementation | 6-8 hrs | **MUST WORK** - but keep simple |
| Defect Reports | 3-4 hrs | **CRITICAL** - show you found issues |
| Documentation | 4-5 hrs | **HIGHEST SCORER** - communication |
| CI Strategy | 2-3 hrs | Required deliverable |
| Polish | 2-3 hrs | Professional finish |

---

## 💡 QUICK WINS

### Easy Points
1. Use framework's built-in HTML reporter - don't build custom
2. Use built-in logging - don't over-engineer
3. Simple page object pattern - don't overcomplicate
4. Clear test names - `test('should filter by Popular category')`
5. README template - start with structure, fill in as you go

### Stand Out
1. **Explain WHY** - for every test case, explain the reasoning
2. **Be Creative** - think beyond obvious tests
3. **Find Real Bugs** - they're there, find them!
4. **Clear Docs** - someone should understand without you explaining
5. **Professional** - clean code, good structure, complete deliverable

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
