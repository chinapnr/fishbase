# 2016.4.26 v1.0.8,  get_date_range()

from datetime import datetime, date
from dateutil.relativedelta import relativedelta


# 2016.4.26
# 输入: date_kind, eg 'last month', 'this month'
# 输出: tuple, type datetime.date eg '2016-03-01' '2016-03-31'
def get_date_range(date_kind):

    today = datetime.today()
    this_year = datetime.today().year
    this_month = datetime.today().month

    first_day = last_day = today

    # 上个月
    if date_kind == 'last month':
        first_day = ((today - relativedelta(months=1)).replace(day=1)).date()
        last_day = date(this_year, this_month, 1) - relativedelta(days=1)

    # 本月
    if date_kind == 'this month':
        first_day = today.replace(day=1).date()

        next_month = this_month + 1
        if next_month == 13:
            next_month = 1

        this_month_last_day = date(this_year, next_month, 1) - relativedelta(days=1)
        last_day = this_month_last_day

    return first_day, last_day
