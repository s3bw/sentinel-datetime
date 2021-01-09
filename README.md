<h1 align='center'>
    Sentinel Datetime
</h1>

<h4 align='center'>
    For dateutil
</h4>

## Install

```
pip install sentinel-datetime
```

## Usage

```python
from dateutil import parser

from sentinel_datetime import sentinel

date = parser.parse("Sep-2nd 11:00:00", default=sentinel())
print("Day:", date.has_day)
print("Year:", date.has_year)
print(date.todatetime())
```
