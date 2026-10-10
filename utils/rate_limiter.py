import time

from fake_useragent import UserAgent

FALLBACK_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)


class RateLimiter:
    def __init__(self, min_interval: float = 1.0):
        self.min_interval = min_interval
        self._last_request: float | None = None

    def wait(self) -> None:
        if self._last_request is not None:
            remaining = self.min_interval - (time.monotonic() - self._last_request)
            if remaining > 0:
                time.sleep(remaining)
        self._last_request = time.monotonic()


def get_random_user_agent() -> str:
    try:
        return UserAgent().random
    except Exception:
        return FALLBACK_USER_AGENT
