# CLAUDE.md — Project Memory & Coding Standards

## Role & Expectations
- You are an experienced Python developer skilled in translating requirements into **Python 3.13.5**-compatible code.
- Implement Pythonic error handling and debugging techniques, ensuring clarity.
- Generate comprehensive, efficient, and maintainable pytest test cases following best practices.

## TODO.md WORKFLOW RULES

### RULE 1: Task-Driven Development
```
BEFORE action → Read TODO.md
Action in TODO? → Execute
Action NOT in TODO? → ASK USER
```

### RULE 2: Checkbox Syntax
```
[ ] = incomplete
[x] = complete
NO emojis, NO other markers
```

### RULE 3: Completed Tasks Are Immutable
```regex
# Completed phase pattern (DO NOT modify):
## <span style="color:green">v\d+\.\d+\.\d+: .+ \(.+\)</span>
.*
- \[x\] .+
```
**Rules:**
- Use Edit tool for surgical changes only
- NO total rewrites, NO deletions of completed phases
- Add new sections at bottom
- If major change needed → ASK USER

### RULE 4: Phase Title Format
```regex
## <span style="color:(green|blue|red)">v\d+\.\d+\.\d+: .+ \(feature/.+\)</span>
```
**Colors:**
- `green` = complete (merged)
- `blue` = in progress (current)
- `red` = planned (future)

### RULE 5: Phase Gate Validation
```
BEFORE starting new phase:
1. grep "## .*${PREV_PHASE}" TODO.md
2. grep "\[ \]" in that section
3. If found → STOP + COMPLAIN + LIST + ASK USER
4. If Phase Gate incomplete → STOP + REQUIRE CONFIRMATION
```

**Output format when blocked:**
```
❌ Phase v1.0.0 incomplete - cannot start v1.1.0
Unchecked: [ ] Step X, [ ] Step Y
Action? (mark complete / defer / proceed anyway)
```

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
- Avoid duplicating constants across modules

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