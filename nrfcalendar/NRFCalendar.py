from __future__ import absolute_import
from __future__ import print_function

from datetime import datetime
import calendar

class NRFCalendar(object):
    """ Main class for retail calendar"""
    def __init__(self):
        self.QUARTER_1 = 1
        self.QUARTER_2 = 2
        self.QUARTER_3 = 3
        self.QUARTER_4 = 4
        self.FOUR_WEEK_MONTHS = [2, 5, 8, 11]
        self.FIVE_WEEK_MONTHS = [3, 6, 9, 12]

    def end_of_year(year):
      year_end = datetime((year + 1), 1, 31)
      wday = (year_end.weekday() + 1) % 7
      if wday > 3:
          year_end += 7 - wday
      else:
        year_end -= wday
    return year_end

    def start_of_year(year):
      return end_of_year(year - 1) + 1
