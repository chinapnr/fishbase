# coding=utf-8

from datetime import datetime, date
from dateutil.relativedelta import relativedelta

# months of a year const
MONTH = 12


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


# v1.0.13 #19048, edit by David Yi, edit by Hu Jun
def previous_months_date(n):
    """
    previous_months_date，获得当前时间往前n个月的时间（年月）

    :param:
        * n: (int) n个月前，正整数

    :return:
        * result: (string) n个月前的年月

    举例如下::

        print('--- previous_months_date demo---')
        print('now is :', str(datetime.now().year*100 + datetime.now().month))
        print('last month:', previous_months_date(1))
        print('10 months ago:', previous_months_date(10))
        print('---')

    执行结果::

        --- previous_months_date demo---
        now is : 201806
        last month: 201805
        10 months ago: 201708
        ---

    """
    now = datetime.now()
    current_months_count = now.year * MONTH + now.month
    current_months_count -= n
    result_year, result_month = divmod(current_months_count, MONTH)
    if result_month == 0:
        result_year -= 1
        result_month = MONTH
    result = ''.join(['%04d' % result_year, '%02d' % result_month])
    return result
