# 2016.4.26 v1.0.8,  get_date_range()

from datetime import datetime, timedelta, date
import calendar


# 2016.4.26
def get_date_range(date_kind):

    today = datetime.today()
    this_month_first_day = today.replace(day=1)

    this_year = datetime.today().year
    # this_month = datetime.today().month

    if date_kind == 'last month':
        # 计算得到需要的 month
        last_month = (this_month_first_day - timedelta(days=1)).month

        year = this_year
        if last_month == 12:
            year = this_year - 1

        month_range = calendar.monthrange(year, last_month)

        month_first_day = date(year, last_month, month_range[0])
        month_end_day = date(year, last_month, month_range[1])

        return month_first_day, month_end_day
