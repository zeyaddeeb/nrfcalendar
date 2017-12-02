from __future__ import absolute_import
from __future__ import print_function

from datetime import datetime

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
        y_end = datetime((year + 1), 1, 31)
        w_day = (year_end.weekday() + 1) % 7
        if w_day > 3:
            y_end += 7 - w_day
        else:
            y_end -= w_day
        return y_end

    def start_of_year(year):
        return end_of_year(year - 1) + 1

    def start_of_month(year, merch_month):
        m_start = start_of_year(year) + int((merch_month - 1) / 3) * 91
        if merch_month in FOUR_WEEK_MONTHS:
            m_start = m_start + 28
        elif merch_month in FIVE_WEEK_MONTHS:
            m_start = m_start + 63
        else:
            print("Invalid merch month")
        return m_start

    def end_of_month(year, merch_month):
        if merch_month == 12:
            y_end = end_of_year(year)
        else:
            y_end = start_of_month(year, merch_month + 1) - 1
        return y_end

    def start_of_week(year, month, merch_week):
        return start_of_month(year, month) + ((merch_week - 1) * 7)

    def end_of_week(year, month, merch_week):
        return start_of_month(year, month) + (6 + ((merch_week - 1) * 7))

    def start_of_quarter(year, quarter):
        if quarter == QUARTER_1:
            q_start =  start_of_month(year, 1)
        elif quarter == QUARTER_2:
            q_start = start_of_month(year, 4)
        elif quarter == QUARTER_3:
            q_start = start_of_month(year, 7)
        elif quarter == QUARTER_4:
            q_start = start_of_month(year, 10)
        else:
            print("Invalid quarter")
        return q_start

    def end_of_quarter(year, quarter):
        if quarter == QUARTER_1:
            q_end = start_of_month(year, 3)
        elif quarter == QUARTER_2:
            q_end = start_of_month(year, 6)
        elif quarter == QUARTER_3:
            q_end = start_of_month(year, 9)
        elif quarter == QUARTER_4:
            q_end = start_of_month(year, 12)
        else:
            print("Invalid quarter")
        return q_end
