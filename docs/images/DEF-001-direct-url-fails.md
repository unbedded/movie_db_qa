# DEF-001: Direct URL Access Fails - Screenshot Placeholder

**Note:** This is a known issue from the assignment PDF (page 1):
> "Refreshing/Accessing the page using specific slugs (e.g., https://tmdb-discover.surge.sh/popular) may not work as expected"

**Expected Screenshot:** Browser error or blank page when accessing `/popular` directly

**Why no screenshot:** 
This defect manifests as navigation failure - the page doesn't load, so capturing a meaningful screenshot is challenging. The test automation validates this via xfail marker in test_foundation.py:

```python
@pytest.mark.xfail(reason="DEF-001: Direct URL access fails")
def test_tc_neg_001_direct_url_access_fails(self, page: Page) -> None:
    """TC-NEG-001: Direct URL Access Fails (Known Defect)."""
```

**Evidence Location:** tests/test_foundation.py line 262
