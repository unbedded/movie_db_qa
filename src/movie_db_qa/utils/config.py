"""Configuration management for test framework."""

from dataclasses import dataclass
from typing import Literal


@dataclass
class TestConfig:
    """Test configuration settings.

    Attributes:
        base_url: Base URL of application under test
        browser: Browser type for Playwright
        headless: Run browser in headless mode
        timeout: Default timeout in milliseconds
        slow_mo: Slow down operations by milliseconds (for debugging)
    """

    base_url: str = "https://tmdb-discover.surge.sh"
    browser: Literal["chromium", "firefox", "webkit"] = "chromium"
    headless: bool = True
    timeout: int = 30000  # 30 seconds
    slow_mo: int = 0  # No slowdown by default

    @classmethod
    def from_env(cls) -> "TestConfig":
        """Create config from environment variables.

        Returns:
            TestConfig instance with values from env vars or defaults
        """
        # TODO: Phase 3 - Add environment variable support
        return cls()


# Global config instance
config = TestConfig()
