# Assignment Overview - QA Automation

## Target
**Website:** https://tmdb-discover.surge.sh/
**Repo Name:** movie_db_qa (public GitHub)
**Timeline:** 2 days

## What They're Actually Evaluating

> **"Frameworks matter less than you think. Don't spend too much time deciding on the tool or framework. Better spend it on polishing your deliverable as a whole."**

### Primary Scoring Criteria (from PDF)

1. **Test Design & Strategy**
   - Which cases did you generate? And why?
   - What is your testing strategy?
   - Which test design techniques did you use?

2. **Code Quality**
   - Quality, maintainability and understandability of the code
   - What patterns did you use while coding?
   - Manages dependencies, execution of tests and reporting

3. **Documentation**
   - Step-by-step test descriptions (Be creative!)
   - Framework information (libraries used)
   - How to run tests
   - Which defects did you find?

4. **CI/CD Thinking**
   - How would you integrate on CI? (document only, don't implement)

## Features to Test

### Filtering Options (Core Focus)
- Categories: Popular, Trending, Newest, Top Rated
- Title search
- Type: Movies or TV Shows
- Year of Release
- Rating
- Genre

### Pagination
- Basic navigation
- Edge cases

### Known Issues (Negative Testing)
- Direct URL slug access (e.g., /popular) fails
- Last few pagination pages broken

## Deliverables Required

### 1. Test Documentation ✅ CRITICAL
- Step-by-step test case descriptions
- Be creative in design
- Clearly explain: WHAT you tested and WHY

### 2. Automated Test Suite ✅ CRITICAL
- Fully automated
- **Console + HTML reports**
- Browser API call validation & assertions
- Logging implementation

### 3. Defect Report ✅ CRITICAL
- Report defects found
- Include attachments/evidence

### 4. CI Strategy Document ✅ CRITICAL
- How you'd approach CI integration
- In README or separate doc
- **NOT IMPLEMENTED - just documented**

## Success Formula

### HIGH IMPACT (Focus Here)
1. **Clear Test Strategy** - Show your thinking
2. **Well-Documented Test Cases** - Creative, thorough, justified
3. **Clean, Maintainable Code** - Patterns, readability
4. **Complete Documentation** - All questions answered
5. **Good Defect Reports** - Clear, with evidence

### MEDIUM IMPACT
- HTML + Console reports working
- API validation shown
- Logging demonstrated
- CI strategy documented

### LOW IMPACT (Don't Overthink)
- Which framework you choose
- How fancy your setup is
- Complex patterns if not needed

## Critical Success Factors

✅ **DO:**
- Document your thought process
- Explain WHY you chose test cases
- Show test design techniques used
- Write clean, understandable code
- Be creative in test scenarios
- Find and report defects clearly
- Make it easy to run your tests

❌ **DON'T:**
- Overthink framework selection
- Over-engineer the solution
- Spend too much time on setup
- Skip documentation to code more
- Forget to explain your decisions

## Key Quote from Assignment

> "We've kept the scope of the assignment rather small on purpose. Please document as much as you can."

**Translation:** They want to see your THINKING and APPROACH more than your coding volume.

## Time Allocation Recommendation

| Activity | Time | Priority |
|----------|------|----------|
| Test Case Design & Documentation | 6-8 hrs | 🔴 CRITICAL |
| Framework Setup | 1-2 hrs | 🟡 LOW |
| Test Implementation | 6-8 hrs | 🔴 CRITICAL |
| Defect Finding & Reporting | 3-4 hrs | 🔴 CRITICAL |
| README & Documentation | 4-5 hrs | 🔴 CRITICAL |
| CI Strategy Doc | 2-3 hrs | 🟢 MEDIUM |
| Polish & Review | 2-3 hrs | 🟢 MEDIUM |

**Total: ~24-30 hours over 2 days**

## The Real Test

This assignment evaluates:
1. **Testing mindset** - How you think about quality
2. **Communication** - How you explain your work
3. **Professionalism** - Deliverable quality
4. **Practical skills** - Can you deliver working tests?
5. **Strategic thinking** - CI/CD approach

**It's NOT about:**
- Advanced framework mastery
- Complex architecture
- Maximum automation coverage
- Latest tools/tech

## Bottom Line

> **Make it work. Make it clear. Make it documented.**

The best submission is one that:
- Has well-thought-out test cases (with explanations)
- Works reliably when run
- Is thoroughly documented
- Finds real defects
- Shows professional QA thinking

Pick a framework you know, write clean tests, document everything, and explain your thinking. Quality over quantity.
