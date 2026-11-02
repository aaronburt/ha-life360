"""Test polling interval calculation."""

from datetime import timedelta

import pytest

from custom_components.life360.helpers import ConfigOptions, member_update_interval


@pytest.mark.parametrize(
    ("polled", "budget", "override", "expected"),
    [
        (19, 150_000, None, 11),
        (9, 150_000, None, 6),
        (18, 150_000, None, 11),
        (1, 150_000, None, 5),
        (0, 150_000, None, 5),
        (19, 150_000, 30, 30),
        (19, 150_000, 1, 5),
        (19, 0, None, 1641600),
    ],
)
def test_member_update_interval(
    polled: int, budget: int, override: float | None, expected: int
) -> None:
    """Test interval is spread over budget, floored, and overridable."""
    options = ConfigOptions(daily_request_budget=budget, update_interval=override)
    assert member_update_interval(options, polled) == timedelta(seconds=expected)
