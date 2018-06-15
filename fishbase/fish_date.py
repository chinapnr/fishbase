# coding=utf-8

from datetime import datetime
import calendar


# 2016.4.26
# 输入: date_kind, eg 'last month', 'this month'
# 输出: tuple, type datetime.date eg '2016-03-01' '2016-03-31'
# v1.0.14 #61, edit by Hu Jun
def get_date_range(dates, separator='-'):
    """
    获取某个月的日期范围，返回该月第一天和最后一天的字符串表示
    
    :param:
        * dates: (string 或者 datetime obj) 月份信息
        * separator: (string) 分隔符，默认为 '-'
    :return:
        * first_day: (string) 该月份的第一天
        * last_day: (string) 该月份的最后一天

    举例如下::

        print('--- get_date_range demo ---')
        now_time = datetime.now()
        print(get_date_range(now_time))
        print(get_date_range('201802',separator='/'))
        print('---')

    执行结果::

        --- get_years demo ---
        ('2018-06-1', '2018-06-30')
        ('2018/02/1', '2018/02/28')
        ---

    """
    if isinstance(dates, str) and dates.isdigit():
        y = dates[:4]
        m = dates[4:]
        if (len(y) != 4) or (not 1 < int(m) < 12):
            raise (ValueError("date must be a date string like '201806', but get {}".format(dates)))
    elif hasattr(dates, 'year') and hasattr(dates, 'month'):
        y = str(dates.year)
        m = str(dates.month)
    else:
        raise (TypeError("date except a years string like '201806' or a object has 'year' "
                         "and 'month' attribute, but get a {}".format(type(dates))))
    
    # set month to length 2 if month less than 10
    m = '0'+m if len(m) != 2 else m
    
    mr = calendar.monthrange(int(y), int(m))
    
    first_day = separator.join([y, m, '1'])
    last_day = separator.join([y, m, str(mr[1])])

    return first_day, last_day


# v1.0.14 #37, edit by Hu Jun
def get_years(months=0, refer=None):
    """
    获取基准时月份增量的年月

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
