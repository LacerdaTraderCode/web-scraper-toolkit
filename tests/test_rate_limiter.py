import pytest

from utils import rate_limiter
from utils.rate_limiter import FALLBACK_USER_AGENT, RateLimiter, get_random_user_agent


@pytest.fixture
def clock(monkeypatch):
    state = {"now": 100.0, "slept": []}

    def fake_sleep(seconds):
        state["slept"].append(seconds)
        state["now"] += seconds

    monkeypatch.setattr(rate_limiter.time, "monotonic", lambda: state["now"])
    monkeypatch.setattr(rate_limiter.time, "sleep", fake_sleep)
    return state


def test_first_request_does_not_wait(clock):
    RateLimiter(min_interval=1.0).wait()

    assert clock["slept"] == []


def test_consecutive_requests_wait_for_full_interval(clock):
    limiter = RateLimiter(min_interval=1.0)

    limiter.wait()
    limiter.wait()

    assert clock["slept"] == [pytest.approx(1.0)]


def test_wait_only_covers_remaining_interval(clock):
    limiter = RateLimiter(min_interval=1.0)
    limiter.wait()
    clock["now"] += 0.4

    limiter.wait()

    assert clock["slept"] == [pytest.approx(0.6)]


def test_no_wait_after_interval_elapsed(clock):
    limiter = RateLimiter(min_interval=1.0)
    limiter.wait()
    clock["now"] += 5

    limiter.wait()

    assert clock["slept"] == []


def test_random_user_agent_comes_from_library(monkeypatch):
    class FakeUserAgent:
        random = "Test-Agent/1.0"

    monkeypatch.setattr(rate_limiter, "UserAgent", FakeUserAgent)

    assert get_random_user_agent() == "Test-Agent/1.0"


def test_random_user_agent_falls_back_on_failure(monkeypatch):
    def broken():
        raise RuntimeError("no network")

    monkeypatch.setattr(rate_limiter, "UserAgent", broken)

    assert get_random_user_agent() == FALLBACK_USER_AGENT
