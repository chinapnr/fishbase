# coding=utf-8

from datetime import datetime, timedelta
import calendar
import random


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


# v1.0.16 #87, edit by Hu Jun
class GetRandomTime(object):
    """
    获取随机时间

    举例如下::

        print('--- GetRandomTime demo ---')
        print(GetRandomTime.date_time_this_month())
        print(GetRandomTime.date_time_this_year())
        print('---')

    执行结果::

        --- Base64 demo ---
        2018-07-01 12:47:20
        2018-02-08 17:16:09
        ---

    """
    a_day_seconds = 24*60*60

    @staticmethod
    def date_time_this_month():
        """
        获取当前月的随机日期

        :return:
            * date_this_month(datetime) 当前月份的随机时间

        举例如下::

            print('--- GetRandomTime.date_time_this_month demo ---')
            print(GetRandomTime.date_time_this_month())
            print('---')

        执行结果::
    
            --- GetRandomTime.date_time_this_month demo demo ---
            2018-07-01 12:47:20
            ---

       """
        now = datetime.now()
        this_month_start = now.replace(
            day=1, hour=0, minute=0, second=0, microsecond=0)
        this_month_days = calendar.monthrange(now.year, now.month)
        random_seconds = random.randint(0, this_month_days[1]*GetRandomTime.a_day_seconds)

        return this_month_start + timedelta(seconds=random_seconds)

    @staticmethod
    def date_time_this_year():
        """
        获取当前年的随机日期
        
        :return:
            * date_this_year(datetime) 当前月份的随机时间

        举例如下::

            print('--- GetRandomTime.date_time_this_year demo ---')
            print(GetRandomTime.date_time_this_year())
            print('---')

        执行结果::
    
            --- GetRandomTime.date_time_this_year demo demo ---
            2018-02-08 17:16:09
            ---
       """
        now = datetime.now()
        this_year_start = now.replace(
            month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
        this_year_days = sum(calendar.mdays)
        random_seconds = random.randint(0, this_year_days*GetRandomTime.a_day_seconds)
        
        return this_year_start + timedelta(seconds=random_seconds)


# v1.1.0 #90, edit by Hu Jun
def get_time_interval(start_time, end_time):
    """
    获取两个unix时间戳之间的时间间隔

    :param:
        * start_time: (int) 开始时间，unix时间戳
        * end_time: (int) 结束时间，unix时间戳
    :return:
        * interval_dict: (dict) 时间间隔字典

    举例如下::

        print('--- get_time_interval demo ---')
        import time
        start = int(time.time())
        end = start - 98908
        print(get_time_interval(end, start))
        print('---')

    执行结果::

        --- get_time_interval demo ---
        {'days': 1, 'hours': 3, 'minutes': 28, 'seconds': 28}
        ---

    """
    if not isinstance(start_time, int) or not isinstance(end_time, int):
        raise TypeError('start_time and end_time should be int, bu we got {0} and {1}'.
                        format(type(start_time), type(end_time)))
        
    # 计算天数
    time_diff = abs(end_time - start_time)
    days = (time_diff // (60*60*24))

    # 计算小时数
    remain = time_diff % (60*60*24)
    hours = (remain // (60*60))

    # 计算分钟数
    remain = remain % (60*60)
    minutes = (remain // 60)

    # 计算秒数
    seconds = remain % 60
    interval_dict = {"days": days, "hours": hours, "minutes": minutes, "seconds": seconds}

    return interval_dict


# v1.1.0 #93, edit by Hu Jun
def transform_unix_to_datetime(timestamp):
    """
    将unix时间戳转换成datetime类型

    :param:
        * timestamp: (int) unix时间戳
    :return:
        * data_type: (datetime) datetime类型实例

    举例如下::

        print('--- transform_unix_to_datetime demo ---')
        import time
        timestamp = int(time.time())
        date_type = transform_unix_to_datetime(timestamp)
        print(type(date_type))
        print(date_type)
        
        print('---')

    执行结果::

        --- transform_unix_to_datetime demo ---
        <class 'datetime.datetime'>
        2018-08-22 19:48:03
        ---

    """
    if not isinstance(timestamp, float) and not isinstance(timestamp, int):
        raise TypeError('timestamp should be a float or int, but we got {}'.format(type(timestamp)))

    date_type = datetime.fromtimestamp(timestamp)
    return date_type
