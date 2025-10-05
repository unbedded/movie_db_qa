# CLAUDE.md — Project Memory & Coding Standards

## Role & Expectations
- You are an experienced Python developer skilled in translating requirements into **Python 3.13.5**-compatible code.
- Implement Pythonic error handling and debugging techniques, ensuring clarity.
- Generate comprehensive, efficient, and maintainable pytest test cases following best practices.

##  TODO.md RULES - CRITICAL FOR AI AGENT

### RULE 1: GOLDEN RULE - Task-Driven Development
**NEVER take action without checking TODO.md first**

BEFORE every action, execute this decision tree:
```
1. Read TODO.md → Find section marked " NEXT"
2. Does TODO explicitly say to do this action?
   → YES: Proceed with action
   → NO: STOP → Ask user for guidance
   → UNCLEAR: STOP → Ask user for clarification
```

**Violations (NEVER do these):**
-  Commit without TODO saying "commit"
-  Push without TODO saying "push"
-  Merge without TODO saying "merge"
-  Create branch without TODO saying "create branch"
-  Any git action not in TODO checklist

**Compliant behavior:**
-  Read TODO.md before EVERY tool use
-  Match action to TODO checklist item
-  If TODO silent → ASK USER

---

### RULE 2: Progress Tracking
**Use checkboxes to track completion state**

**Syntax:**
- `[ ]` = Task not started or incomplete
- `[x]` = Task complete
- NO emojis ( `[x] `  `[x]`)
- NO other markers

**Update pattern:**
1. Work on task
2. Complete task
3. Change `[ ]` to `[x]` in TODO.md
4. Commit change with task description

---

### RULE 3: TODO.md is Immutable History
**TODO.md is append-only permanent record**

**NEVER do:**
-  `cp newfile.md TODO.md` (destroys history)
-  Total rewrites (loses context)
-  Delete completed phases
-  Remove old sections
-  Mass search-replace of content

**ALWAYS do:**
-  Use Edit tool for surgical changes
-  Add new sections at bottom
-  Archive old phases (keep text, mark archived)
-  Preserve all historical decisions
-  If major change needed → ASK USER FIRST

**Why:** TODO.md = audit trail of entire project. Evaluators read it to understand progression.

---

### RULE 4: Phase Labels Match VERSION Numbers
**Phase organization aligned with semantic versioning**

**Pattern:**
- Phase name = `v{VERSION}: Description (branch_name)`
- Branch name in parentheses helps locate the work
- Completed phases use HTML green color: `<span style="color:green">v0.2.0: Title (branch_name)</span>`
- In-progress phases: normal text (no color)
- NOT: "Phase 1", "Phase 2" (incorrect)
- NOT: Append "(FUTURE)" to future phases - just list them normally

**Examples:**
```markdown
## <span style="color:green">v0.3.0: Test Implementation (feature/test-impl)</span>
**Branch:** feature/test-impl
**Goal:** Implement 8-10 test cases
**Time Spent:** 3 hours

- [x] Implement tests
- [x] Run quality checks

## v1.1.0: Traceability Infrastructure (feature/traceability)
**Branch:** Will create feature/traceability from develop (after v1.0.0)
**Goal:** Implement automated traceability
**Time Budget:** 2-3 hours

- [ ] Create requirements.yml
- [ ] Implement audit script
```

**Rationale:**
- Version numbers = concrete milestones (not arbitrary "Phase 1, 2, 3")
- Branch names = instant context for git history
- Green styling = visual completion indicator
- No "(FUTURE)" labels - all phases are in chronological order anyway

---

### RULE 5: Phase Gates Enforce Completion
**Every phase ends with Phase Gate checklist - ALL items must complete**

**Phase Gate structure:**
```markdown
###  Phase Gate: {Phase Name}
- [ ] Item 1
- [ ] Item 2
- [ ] Item 3

**Success Metric:** All items [x] before next phase
```

**Enforcement rules:**
1. Phase Gate appears at END of every phase
2. Before starting next phase, verify: Are ALL `[ ]` now `[x]`?
   - YES → Proceed to next phase
   - NO → STOP → Handle incomplete items:
     - Move to future phase (add to that phase's checklist)
     - OR move to Technical Debt section
     - OR ask user how to handle
3. NEVER leave `[ ]` items in completed phase
4. Clean closure = clear audit trail

**Example:**
```markdown
## <span style="color:green">v0.3.0: Test Implementation (feature/test-impl)</span>

### Phase Gate v0.3.0
- [x] All tests passing
- [x] Quality checks pass
- [ ] API validation ← INCOMPLETE!

**Resolution:** Move API validation to v0.4.0 phase
```

---

### WORKFLOW SUMMARY
**Standard operating procedure:**

```
START → Check TODO.md for " NEXT"
     → Read checklist for that phase
     → Execute ONLY items in checklist
     → Mark items [x] as completed
     → Verify Phase Gate: all [x]?
       → YES: Update TODO status, proceed
       → NO: Resolve incomplete items
     → Commit TODO.md changes
     → Move to next phase
     → REPEAT
```

**Key principle:** TODO.md drives ALL actions. Agent reads, agent obeys, agent updates, agent asks when unclear.

## Coding Standards
- Adhere to **PEP8** and use **type hints** consistently.
- Use modern Python built-ins (`list`, `dict`, `tuple`) for type hints when possible.
- Use **named arguments** for functions with multiple parameters.
- Replace magic numbers with **constants**.

## Documentation
- Provide **verbose docstrings** for public classes, methods, and functions.
- Include clear explanations in module headers.
- Add example usage in docstrings where helpful.

## Error Handling
- Use Pythonic `try-except` blocks.
- Raise appropriate built-in or custom exceptions.
- Provide clear and informative error messages.
- Use `logging.exception()` to capture stack traces when errors occur.

## Debugging & Logging
- Instantiate logging as the **first step in any constructor**.
- ** MANDATORY: Use lazy `%` formatting** - NEVER use f-strings in log statements
  -  CORRECT: `logger.info("User %s logged in at %s", username, timestamp)`
  -  WRONG: `logger.info(f"User {username} logged in at {timestamp}")`
  - **WHY:** Lazy formatting only evaluates arguments if log level is enabled (performance)
- Configure logging with file output and timestamps.
- Use appropriate logging levels: `DEBUG` (details), `INFO` (events), `ERROR` (exceptions).
- Default logger level: `WARNING`.
- Ensure logging is **thread-safe**.
- Demonstrate logging for key operations such as input validation, cache access, and calculation steps.
- Avoid logging sensitive or redundant information.
- Use `logging.exception()` to capture stack traces when errors occur.

## Security
- Never log or expose secrets, API keys, or sensitive data.
- Validate all inputs and sanitize user-provided data.
- Use secure defaults and fail securely.

## Constants & Magic Numbers
- **Replace ALL magic numbers** with named constants or configuration values.
- Use **ALL_CAPS** for module-level constants: `LOGO_WIDTH_INCHES = 0.8`
- Group related constants into dataclasses or configuration objects.
- Prefer configuration injection over hardcoded values, especially for shared constants.
- Document relationships between constants and their usage.

**Examples:**
```python
# BAD: Magic numbers scattered throughout code
logo_image = Image(path, width=0.8 * inch, height=0.25 * inch)
nutrition_width = content_width * 0.20
spacer = Spacer(1, 0.1 * inch)

# GOOD: Named constants at module level
LOGO_WIDTH_INCHES = 0.8
LOGO_HEIGHT_INCHES = 0.25
NUTRITION_COLUMN_RATIO = 0.20
DEFAULT_SPACER_INCHES = 0.1

# BETTER: Grouped configuration objects for shared constants
@dataclass
class LayoutConstants:
    logo_width_inches: float = 0.8
    logo_height_inches: float = 0.25
    nutrition_column_ratio: float = 0.20
    ingredient_column_ratio: float = 0.44
    default_spacer_inches: float = 0.1
```

**Shared Constants Architecture:**
- Create shared configuration classes for cross-module constants
- Use dependency injection to pass configuration objects to constructors
- Validate configuration values with Pydantic validators
- Avoid duplicating constants across modules

## Configuration Management
- Use **Pydantic Settings** for type-safe configuration with validation.
- Support multiple config sources: environment variables, `.env` files, and direct instantiation.
- Use secure defaults and validate all configuration values on startup.
- Never include secrets in default values or log configuration containing sensitive data.
- Example pattern:
```python
from pydantic import BaseSettings, Field, validator
from typing import Optional

class AppConfig(BaseSettings):
    debug: bool = False  # Secure default
    log_level: str = Field(default="WARNING", env="LOG_LEVEL")
    database_url: Optional[str] = Field(default=None, env="DATABASE_URL")
    api_key: Optional[str] = Field(default=None, env="API_KEY")

    @validator('log_level')
    def validate_log_level(cls, v):
        valid_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        if v.upper() not in valid_levels:
            raise ValueError(f'Invalid log level: {v}')
        return v.upper()

    class Config:
        env_file = ".env"
        case_sensitive = False
```
- Pass config objects to class constructors instead of raw dictionaries.
- Validate configuration on startup and fail fast with clear error messages.

## Testing Standards
- Generate comprehensive pytest test cases covering edge cases and all possible scenarios.
- Use pytest fixtures appropriately for setup and teardown.
- Use pytest parameterization for concise, readable, and maintainable test cases.
- Ensure tests are deterministic and produce consistent results.
- Test function behavior across wide range of inputs, including extreme and unexpected cases.
- Write descriptive test function names and organize tests logically.
- Include comprehensive docstrings in test files explaining test coverage and expectations.

## Workflow Notes
- Use `.claude/commands/new_module.md` to scaffold modules with tests.
- After edits, run: `make quality && make test-full`.

# important-instruction-reminders
Do what has been asked; nothing more, nothing less.
NEVER create files unless they're absolutely necessary for achieving your goal.
ALWAYS prefer editing an existing file to creating a new one.
NEVER proactively create documentation files (*.md) or README files. Only create documentation files if explicitly requested by the User.