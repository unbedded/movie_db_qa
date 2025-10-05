# Auto-Captured Bug Screenshots

This directory contains screenshots automatically captured during test execution when tests fail (expected or unexpected).

## How Screenshots Are Generated

Screenshots are automatically captured by the pytest fixture in `tests/conftest.py` when:

1. **Unexpected test failures** - Test fails due to implementation bug
2. **Expected failures (xfail tests)** - Tests marked with `@pytest.mark.xfail` that document known application defects

## Screenshot Capture Logic

```python
# From tests/conftest.py - page fixture teardown
# Capture screenshot on test failure (including xfail tests to show actual bug state)
if hasattr(request.node, "rep_call"):
    # Capture for both unexpected failures and expected failures (xfail)
    # xfail screenshots demonstrate the actual defect behavior
    if request.node.rep_call.failed or (
        hasattr(request.node.rep_call, "wasxfail") and request.node.rep_call.wasxfail
    ):
        screenshot_name = f"{request.node.name}_{request.node.rep_call.when}.png"
        screenshot_path = SCREENSHOT_DIR / screenshot_name
        status = "xfail" if hasattr(request.node.rep_call, "wasxfail") else "failed"
        logger.info("Test %s - capturing screenshot: %s", status, screenshot_path)
        page.screenshot(path=str(screenshot_path))
```

## Current Screenshots

### test_tc_pag_001_navigate_to_page_2_call.png (816KB)

**Source:** TC-PAG-001 - Navigate to page 2
**Defect:** DEF-007 - Pagination navigation broken
**Status:** Expected failure (xfail)
**Captured:** 2025-10-05 09:35:37

**What it shows:**
- Application state after clicking "Next" button
- URL should be `/popular/2` but remains `/popular`
- API correctly called `page=2` endpoint (visible in logs)
- Browser state frozen at moment of assertion failure

**How it was generated:**
1. Test execution: `make test-full`
2. TC-PAG-001 test runs (marked xfail for DEF-007)
3. Test clicks "Next" button
4. Test expects URL to change to `/popular/2`
5. Assertion fails (URL stays `/popular`)
6. pytest hook detects xfail status
7. Screenshot automatically captured to this directory

**Value:**
- Visual proof of defect behavior
- Shows exact application state at failure moment
- Demonstrates automated artifact collection works
- Supplements defect report with visual evidence

## Why xfail Tests Generate Screenshots

Unlike typical test automation where screenshots only capture **unexpected** failures, this framework also captures screenshots for **expected failures (xfail)**. This design choice provides:

1. **Visual defect documentation** - Screenshots show actual bug behavior
2. **Evidence preservation** - Visual proof supplements written defect reports
3. **Regression detection** - If xfail test starts passing, we have before/after comparison

## Naming Convention

Screenshot filenames follow pytest convention:
```
{test_function_name}_{test_phase}.png
```

Example: `test_tc_pag_001_navigate_to_page_2_call.png`
- `test_tc_pag_001_navigate_to_page_2` - Test function name
- `call` - Test phase (setup/call/teardown)

## Manual vs Automated Screenshots

This directory contains **automated** screenshots captured during test execution.

For **manual** defect screenshots from exploratory testing, see:
- `artifacts/defect-manual-reports/screenshots/`
