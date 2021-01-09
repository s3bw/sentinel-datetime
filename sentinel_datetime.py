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
        self.year = year
        self.month = month
        self.day = day

        self.hour = hour
        self.minute = minute
        self.second = second
        self.microsecond = microsecond

        if default is None:
            default = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        self.default = default

    @property
    def has_year(self):
        return self.year != 0

    @property
    def has_month(self):
        return self.month != 0

    @property
    def has_day(self):
        return self.day != 0

    def todatetime(self):
        res = {
            attr: value
            for attr, value in [
                ("year", self.year),
                ("month", self.month),
                ("day", self.day),
                ("hour", self.hour),
                ("minute", self.minute),
                ("second", self.second),
                ("microsecond", self.microsecond),
            ]
            if value
        }
        return self.default.replace(**res)

    def replace(self, **res):
        return sentinel(**res, default=self.default)

    def __repr__(self):
        return "%s(%d, %d, %d, %d, %d)" % (
            self.__class__.__qualname__,
            self.year,
            self.month,
            self.day,
            self.hour,
            self.minute,
        )
