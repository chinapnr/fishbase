# coding=utf-8

import time
from datetime import datetime, timedelta
import calendar
import random

A_DAY_SECONDS = 24 * 60 * 60


# 2016.4.26
# 输入: date_kind, eg 'last month', 'this month'
# 输出: tuple, type datetime.date eg '2016-03-01' '2016-03-31'
# v1.0.14 edit by Hu Jun #61
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
        if (len(y) != 4) or (not 1 <= int(m) <= 12):
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


# v1.0.14 edit by Hu Jun #37
def get_years(months=0, refer=None):
    """
    获取基准时月份增量的年月

    :param:
        * months: (int) 月份增量，正数为往后年月，整数为往前年月
        * refer: (datetime obj) datetime 对象，或者有 month 和 year 属性的实例，默认为当前时间
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


# v1.0.16 edit by Hu Jun #87
# v1.1.14 edit by Hu Jun #142
# v1.1.15 edit by Jia Chunying #142 #164
# v1.4 edit by David Yi, #287, 修改 函数 gen_date_by_range()
# 2021.6.2, #287, 修改 gen_date_by_range() 为 random_date_by_range；gen_date_by_range() 为 random_date_by_range()
# 2021.6.4, #288, 修改 date_time_this_month() 为 random_datetime_this_month()
# 2021.6.7, #288, 修改 date_time_this_year() 为 random_datetime_this_year()
# 2021.6.23, #288, 修改类名称和函数名，更加符合标准
class RandomTime(object):
    """
    获取随机时间

    举例如下::

        print('--- RandomTime demo ---')
        print(RandomTime.get_date_time_this_month())
        print(RandomTime.get_date_time_this_year())
        print('---')

    执行结果::

        --- Base64 demo ---
        2018-07-01 12:47:20
        2018-02-08 17:16:09
        ---

    """
    @staticmethod
    def get_random_datetime_this_month():
        """
        生成一个属于当前月的随机日期时间

        :return:
            * random_date: (datetime) 个属于当前月的随机日期时间

        举例如下::

            print('--- RandomTime.get_random_datetime_this_month demo ---')
            print(RandomTime.get_random_datetime_this_month)
            print('---')

        执行结果::
    
            --- RandomTime.get_date_time_this_month demo demo ---
            2018-07-01 12:47:20
            ---

       """
        now = datetime.now()
        begin_this_month = now.replace(
            day=1, hour=0, minute=0, second=0, microsecond=0)
        this_month_days = calendar.monthrange(now.year, now.month)
        random_seconds = random.randint(0, this_month_days[1]*A_DAY_SECONDS)

        random_date = begin_this_month + timedelta(seconds=random_seconds)

        return random_date

    @staticmethod
    def get_random_datetime_this_year():
        """
        获取当前年的随机时间字符串
        
        :return:
            * date_this_year: (datetime) 当前月份的随机时间

        举例如下::

            print('--- RandomTime.get_date_time_this_year demo ---')
            print(RandomTime.get_date_time_this_year())
            print('---')

        执行结果::
    
            --- RandomTime.get_date_time_this_year demo demo ---
            2018-02-08 17:16:09
            ---
       """
        now = datetime.now()
        this_year_start = now.replace(
            month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
        this_year_days = sum(calendar.mdays)
        random_seconds = random.randint(0, this_year_days*A_DAY_SECONDS)

        return this_year_start + timedelta(seconds=random_seconds)

    @staticmethod
    def get_random_date_by_year(year):
        """
        获取当前年的随机日期字符串

        :param:
            * year: (string) 长度为 4 位的年份字符串，eg. 2018

        :return:
            * date_str: (string) 传入年份内的随机合法日期字符串，eg. 20180201
        
        举例如下::
        
            print('--- RandomTime.get_random_date_by_year demo ---')
            print(RandomTime.get_random_date_by_year("2010"))
            print('---')
        
        执行结果::
        
            --- RandomTime.gen_date_by_year demo ---
            20100505
            ---
        """
        if isinstance(year, int) and len(str(year)) != 4:
            raise ValueError("year should be int year like 2018, but we got {}, {}".
                             format(year, type(year)))
        if isinstance(year, str) and len(year) != 4:
            raise ValueError("year should be string year like '2018', but we got {}, {}".
                             format(year, type(year)))
        if isinstance(year, int):
            year = str(year)

        date_str = RandomTime.get_random_date_by_range(year + "-01-01", year + "-12-31", "%Y-%m-%d")

        return date_str

    @staticmethod
    def get_random_date_by_range(begin_date, end_date, date_format="%Y-%m-%d"):
        """

        生成指定日期范围内的一个随机日期

        :param:
            * begin_date: (string) 起始日期，yyyy-MM-dd，eg. 2018-01-01
            * end_date: (string) 结束日期，yyyy-MM-dd，eg. 2018-12-31
            * date_format: (string) 输入的日期格式，默认格式 "%Y-%m-%d"

        :return:
            * date_str: (string) 日期范围内的一个指定格式的随机日期，指定格式默认为 "%Y%m%d"，eg. 20180530

        举例如下::

            print('--- RandomTime.get_random_date_by_range demo ---')
            print(RandomTime.get_random_date_by_range("2010-01-01","2010-12-31"))
            print('---')

        执行结果::

            --- RandomTime.get_random_date_by_range demo ---
            20100124
            ---
        """

        d0 = datetime.strptime(begin_date, date_format)
        d1 = datetime.strptime(end_date, date_format)
        random_date = d0 + (d1-d0)*random.random()

        return datetime.strftime(random_date, "%Y%m%d")


# v1.1.0 edit by Hu Jun #90
def get_time_interval(start_time, end_time):
    """
    获取两个unix时间戳之间的时间间隔

    :param:
        * start_time: (int) 开始时间，unix 时间戳
        * end_time: (int) 结束时间，unix 时间戳
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


# v1.1.0 edit by Hu Jun #93
def transform_unix_to_datetime(timestamp):
    """
    将 unix 时间戳转换成 datetime 类型

    :param:
        * timestamp: (int) unix 时间戳
    :return:
        * data_type: (datetime) datetime 类型实例

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


# v1.1.1 edit by Hu Jun #101
def transform_datetime_to_unix(dtime=None):
    """
    将 datetime 类型转换成 unix 时间戳

    :param:
        * dtime: (datetime) datetime 类型实例,默认为当前时间
    :return:
        * data_type: (datetime) datetime 类型实例

    举例如下::

        print('--- transform_datetime_to_unix demo ---')
        dtime = datetime.datetime.now()
        ans_time = transform_datetime_to_unix(dtime)
        print(ans_time)
        print('---')

    执行结果::

        --- transform_datetime_to_unix demo ---
        1535108620.0
        ---

    """
    if not dtime:
        dtime = datetime.now()

    if not isinstance(dtime, datetime):
        raise TypeError('dtime should be datetime, but we got {}'.format(type(dtime)))

    return time.mktime(dtime.timetuple())


# v1.1.3 edit by Hu Jun #116
class FishDateTimeFormat(object):
    """
    实现 datetime 和 str 之间相互转换，基于 Python 的 datetime.datetime 进行封装和扩展；

    举例如下::

        print('--- FishDateTimeFormat demo ---')
        datetime_obj = date(year=2018, month=11, day=23)
        print(FishDateTimeFormat.strftime(datetime_obj, '%Y-%m-%d'))
        date_time_str = '2018-11-23 23:17:20'
        time_format = '%Y-%m-%d %H:%M:%S'
        print(FishDateTimeFormat.strptime(date_time_str, time_format))
        print('---')

    执行结果::

        --- FishDateTimeFormat demo ---
        2018-11-23
        2018-11-23 23:17:20
        <class 'datetime.datetime'>
        ---

        """
    @staticmethod
    def strftime(date_time=None, time_format=None):
        """
        将 datetime 对象转换为 str

        :param:
            * date_time: (obj) datetime 对象
            * time_format: (sting) 日期格式字符串
        :return:
            * date_time_str: (string) 日期字符串
        """
        if not date_time:
            datetime_now = datetime.now()
        else:
            datetime_now = date_time
        if not time_format:
            time_format = '%Y/%m/%d %H:%M:%S'
        return datetime.strftime(datetime_now, time_format)

    @staticmethod
    def strptime(time_str, time_format):
        """
        将 str 转换为 datetime 对象

        :param:
            * time_str: (string) 日期字符串
            * time_format: (sting) 日期格式字符串
        :return:
            * datetime_obj: (obj) datetime 对象
        """
        try:
            datetime_obj = datetime.strptime(time_str, time_format)
            return datetime_obj
        except ValueError as ex:
            raise ValueError(ex)
