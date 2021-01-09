<h1 align='center'>
    Sentinel Datetime
</h1>

<h4 align='center'>
    For python-dateutil
</h4>

Inspired by [a stackoverflow question](https://stackoverflow.com/q/65643971/3407256),
for when you want to know a little more about the
datetime strings you are parsing with python-dateutil

## Install

```
pip install sentinel-datetime
```

## Usage

```python
>>> from dateutil import parser
>>>
>>> from sentinel_datetime import sentinel
>>>
>>> date = parser.parse("Sep-2nd 11:00:00", default=sentinel())
>>> date.has_day
True
>>> date.has_year
False
>>> date.todatetime()
2021-09-02 11:00:00
```
