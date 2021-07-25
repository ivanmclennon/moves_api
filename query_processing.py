import os
from typing import Optional
from datetime import datetime as dt, timedelta

from fastapi import Depends, HTTPException

from dependencies import Period, date_kwargs
from exceptions import InvalidDateError, ActivityNotFound


class QueryParamsProcessor():

    """
    Class for processing period and {year,month,date} query parameters.
    """

    period: Period
    date: dict

    DEFAULT_DATE: dict = {
        "year": 2014,
        "month": 1,
        "day": 1
    }
    _given_date: dict
    _dt_format: str = ""
    _dt_string: str = ""

    def __init__(self, period: Optional[Period], date: dict = Depends(date_kwargs)) -> None:
        """
        Initialize QueryParamsProcessor object,
        based on period and date query params.

        Sets corresponding attributes, providing defaults for None values.

        :param period: Period enum
        :param date: {year, month, day} dict based on date_kwargs dependency       
        """
        self._given_date = date
        self.date = date
        if period:
            self.period = period
        else:
            if not any(date.values()):
                self.period = Period.FULL
            else:
                self._period_from_date()
        self._fill_date()

    def __str__(self) -> str:
        return f"QueryParamsProcessor[" + \
            f"{self.period.value}," + \
            f"{self.date}," + \
            f"{self._dt_format}," + \
            f"{self._dt_string}" + \
            "]"

    def _set_dt_format(self):
        """Sets _dt_format attr to coresponding value based on Period."""
        formats = {
            Period.DAILY: "%Y%m%d",
            Period.WEEKLY: "%Y%m%d",
            Period.MONTHLY: "%Y-%m",
            Period.YEARLY: "%Y",
            Period.FULL: "",
        }
        self._dt_format = formats[self.period]

    def _get_datetime_or_error(self) -> dt:
        """
        Parse date attr into a datetime object.
        Returns a datetime object or raises ValueError.
        """
        return dt(
            *(self.date[key] for key in ['year', 'month', 'day'] if key in self.date)
        )

    def _set_date_weekly(self):
        """
        Set date attr to a first weekday for requested date.
        Raises Invalid Date Error if datetime parse fails.
        """
        dt_weekday = dt.now()
        try:
            dt_weekday = self._get_datetime_or_error()
        except ValueError:
            self._dt_string = ""
            raise InvalidDateError(detail={
                "message": "Invalid Date Provided",
                "period": self.period.value,
                "date": self._given_date
            })
        week_start = dt_weekday - timedelta(days=dt_weekday.weekday())
        self.date['year'] = week_start.year
        self.date['month'] = week_start.month
        self.date['day'] = week_start.day

    def _set_dt_string(self):
        """
        Sets _dt_string to datetime string in specified format,
        or empty string if date is invalid.
        """
        if self.period is Period.WEEKLY:
            self._set_date_weekly()
        try:
            self._dt_string = self._get_datetime_or_error().strftime(self._dt_format)
        except ValueError:
            self._dt_string = ""
            raise InvalidDateError(detail={
                "message": "Invalid Date Provided",
                "period": self.period.value,
                "date": self._given_date
            })

    def _get_filepath(self) -> str:
        """Returns filepath from combined period and _dt_string."""
        return os.path.join(
            os.sep.join(
                [
                    self.period.value,
                    'activities',
                    f'activities_{self._dt_string}.json'
                ]
            )
        )

    def _period_from_date(self):
        """Sets period attr based on existing date values."""
        if self.date['year']:
            if self.date['month']:
                if self.date['day']:
                    self.period = Period.DAILY
                else:
                    self.period = Period.MONTHLY
            else:
                self.period = Period.YEARLY
        else:
            self.period = Period.FULL

    def _fill_date(self):
        """Sets missing date values to defaults from DEFAULT_DATE"""
        if not self.date['year']:
            self.date['year'] = self.DEFAULT_DATE['year']
        if not self.date['month']:
            self.date['month'] = self.DEFAULT_DATE['month']
        if not self.date['day']:
            self.date['day'] = self.DEFAULT_DATE['day']

    def __call__(self) -> str:
        """
        Process period and date query param attrs.
        Return filepath on success.
        """
        self._set_dt_format()
        self._set_dt_string()
        return self._get_filepath()
