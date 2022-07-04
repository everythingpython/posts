import sys
from typing import Tuple, no_type_check
import pandas as pd

YYYY_MM_DD = str


def date_to_day(dt: YYYY_MM_DD) -> str:
    """Simple program to find the day of week of a given date"""
    date = pd.DataFrame({'inputDate': [dt]})
    date['inputDate'] = pd.to_datetime(date['inputDate'])
    day_of_week = date['inputDate'].dt.day_name()
    return day_of_week.values[0]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing list argument of the type '2020-07-07'.")
    else:
        date_str = sys.argv[1]
        day = date_to_day(date_str)
        print(f"{date_str=}. Equivalent {day=}")
