# coding=utf-8

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


# v1.0.14 #37, edit by Hu Jun
def get_years(months=0, refer=None):
    """
    get_years，获取基准时月份增量的年月

    :param:
        * months: (int) 月份增量，正数为往后年月，整数为往前年月
        * refer: (datetime obj) datetime 对象，或者有month和year属性的实例，默认为当前时间
    :return:
        * result: (string) 年月字符串

    举例如下::

        print('--- get_years demo ---')
        print(get_years(-5))
        print(get_years(7, datetime.now()))
        print('---')

    执行结果::

        --- get_years demo ---
        201801
        201901
        ---

    """
    if refer is None:
        refer = datetime.now()
    # 计算当前总月份数
    try:
        months_count = refer.year * 12 + refer.month
    except Exception:
        raise TypeError('refer except {}, got an {}'.format(type(datetime.now()), type(refer)))
    
    # 计算结果总月分数
    months_count += months
    
    y, m = divmod(months_count, 12)
    
    # 将m的值转换为1-12
    if m == 0:
        y -= 1
        m = 12
    
    return ''.join(['%04d' % y, '%02d' % m])
