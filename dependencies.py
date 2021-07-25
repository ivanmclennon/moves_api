from typing import Optional, Dict
from enum import Enum


class Period(Enum):
    """
    Enum for Moves data directories.
    """
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"
    FULL = "full"


def date_kwargs(year: Optional[int] = None,
                month: Optional[int] = None,
                day: Optional[int] = None) -> Dict[str, Optional[int]]:
    """Common date dependencies for injection."""
    return {
        "year": year,
        "month": month,
        "day": day
    }