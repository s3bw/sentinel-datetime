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
    ],
)
def test_has_day(datestr, expected):
    default = sentinel()
    result = parser.parse(datestr, default=default)
    assert result.has_day is expected


@freeze_time("Jan 18th, 2008")
def test_default_datetime():
    default = sentinel()
    result = parser.parse("Sep-2020", default=default)
    assert result.todatetime() == datetime(2020, 9, 18)

    default = sentinel(default=datetime(1978, 2, 2))
    result = parser.parse("Sep-2020", default=default)
    assert result.todatetime() == datetime(2020, 9, 2)


@pytest.mark.parametrize(
    "datestr, expected",
    [
        ("Sep-2020", datetime(2020, 9, 18)),
        ("1-Sep-2020", datetime(2020, 9, 1)),
        ("1-Sep", datetime(2021, 9, 1)),
        ("Sep-3rd", datetime(2021, 9, 3)),
        ("11-1", datetime(2021, 11, 1)),
    ],
)
def test_to_datetime(datestr, expected):
    default = sentinel(default=datetime(2021, 9, 18))
    result = parser.parse(datestr, default=default)
    assert result.todatetime() == expected
