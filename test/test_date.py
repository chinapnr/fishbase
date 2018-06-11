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

        with pytest.raises(TypeError):
            get_years(-5, 8)
