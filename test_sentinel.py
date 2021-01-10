from datetime import datetime

import pytest
from freezegun import freeze_time

from dateutil import parser

from sentinel_datetime import sentinel


@pytest.mark.parametrize(
    "datestr, expected",
    [
        ("Sep-2020", False),
        ("1-Sep-2020", True),
        ("2020-11", False),
        ("11-1", True),
        ("1993", False),
    ],
)
def test_has_day(datestr, expected):
    default = sentinel()
    result = parser.parse(datestr, default=default)
    assert result.has_day is expected


@pytest.mark.parametrize(
    "datestr, expected",
    [
        ("Sep-2020", True),
        ("1-Sep-2020", True),
        ("2020-11", True),
        ("11-1", False),
        ("1993", True),
    ],
)
def test_has_year(datestr, expected):
    default = sentinel()
    result = parser.parse(datestr, default=default)
    assert result.has_year is expected


@freeze_time("Jan 18th, 2008")
@pytest.mark.parametrize(
    "datestr, expected_today, expected_default",
    [
        ("Sep-2020", datetime(2020, 9, 18), datetime(2020, 9, 2)),
        ("2020", datetime(2020, 1, 18), datetime(2020, 2, 2)),
    ],
)
def test_default_datetime(datestr, expected_today, expected_default):
    default = sentinel()
    result = parser.parse(datestr, default=default)
    assert result.todatetime() == expected_today

    default = sentinel(default=datetime(1978, 2, 2))
    result = parser.parse(datestr, default=default)
    assert result.todatetime() == expected_default


@pytest.mark.parametrize(
    "datestr, expected",
    [
        ("Sep-2020", datetime(2020, 9, 18)),
        ("1-Sep-2020", datetime(2020, 9, 1)),
        ("1-Sep", datetime(2021, 9, 1)),
        ("Sep-3rd", datetime(2021, 9, 3)),
        ("11-1", datetime(2021, 11, 1)),
        ("1993", datetime(1993, 9, 18)),
        ("2020-08", datetime(2020, 8, 18)),
        ("2020", datetime(2020, 9, 18)),
    ],
)
def test_to_datetime(datestr, expected):
    default = sentinel(default=datetime(2021, 9, 18))
    result = parser.parse(datestr, default=default)
    assert result.todatetime() == expected
