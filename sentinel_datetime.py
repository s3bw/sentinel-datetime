from datetime import datetime


class sentinel:
    def __init__(
        self,
        year=0,
        month=0,
        day=0,
        hour=0,
        minute=0,
        second=0,
        microsecond=0,
        default=None,
    ):
        # We can probably just use the `res` passed
        # to the _build_naive method instead.
        self._year = year
        self._month = month
        self._day = day

        self._hour = hour
        self._minute = minute
        self._second = second
        self._microsecond = microsecond

        if default is None:
            default = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

        self.default = default

    def __getattr__(self, attr):
        return getattr(self.default, attr)

    @property
    def has_year(self):
        return self._year != 0

    @property
    def has_month(self):
        return self._month != 0

    @property
    def has_day(self):
        return self._day != 0

    def todatetime(self):
        res = {
            attr: value
            for attr, value in [
                ("year", self._year),
                ("month", self._month),
                ("day", self._day),
                ("hour", self._hour),
                ("minute", self._minute),
                ("second", self._second),
                ("microsecond", self._microsecond),
            ]
            if value
        }
        return self.default.replace(**res)

    def replace(self, **res):
        return sentinel(**res, default=self.default)

    def __repr__(self):
        return "%s(%d, %d, %d, %d, %d)" % (
            self.__class__.__qualname__,
            self._year,
            self._month,
            self._day,
            self._hour,
            self._minute,
        )
