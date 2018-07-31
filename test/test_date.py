# coding=utf-8
# fish_date.py 单元测试
# 2018.6.11 create by Hu Jun

import pytest
import sys
sys.path.append('../fishbase')
from fishbase.fish_date import *
import datetime


# 2018.6.11 v1.0.14 #37 create by Hu Jun
class TestFishDate(object):
    # test get_years() tc
    def test_get_years_01(self):
        this_month = datetime.date(day=1, month=6, year=2018)
        
        assert get_years(7, this_month) == '201901'
        assert get_years(-5, this_month) == '201801'
        assert get_years(-6, this_month) == '201712'

        this_month1 = datetime.datetime.now()
        
        y = this_month1.year
        m = this_month1.month + 1
        if m == 12:
            y += 1
            m = 1
        
        assert get_years(1) == ''.join(['%04d' % y, '%02d' % m])
        
        with pytest.raises(TypeError):
            get_years(-5, 8)

    def test_get_date_range_01(self):
        this_month = datetime.date(day=1, month=2, year=2018)
    
        assert get_date_range(this_month) == ('2018-02-1', '2018-02-28')
        assert get_date_range('201802', separator='/') == ('2018/02/1', '2018/02/28')
        
        with pytest.raises(ValueError):
            get_date_range('2016798')
        
        with pytest.raises(TypeError):
            get_date_range('asdafsd')

    # 测试 GetRandomTime()  tc
    def test_date_time_this_month_01(self):
        this_month = GetRandomTime.date_time_this_month()
        now = datetime.datetime.now()
        this_month_days = calendar.monthrange(now.year, now.month)
        assert now.year == this_month.year
        assert now.month == this_month.month
        assert now.day <= this_month_days[1]

    # 测试 GetRandomTime()  tc
    def test_date_time_this_year_01(self):
        this_month = GetRandomTime.date_time_this_year()
        now = datetime.datetime.now()
        this_year_days = sum(calendar.mdays)
        assert now.year == this_month.year
        assert now.day <= this_year_days
