# coding=utf-8
# fish_date.py 单元测试
# 2018.6.2 create by Hu Jun

import sys
sys.path.append('../fishbase')
from fishbase.fish_date import *


# 2018.6.2 v1.0.13 create by Hu Jun
class TestFishDate(object):

    # test previous_months_date() tc
    def test_previous_months_date_01(self):
        # 因为测试日期会变，所以断言一月前加1是否为当前月
        now = datetime.now()
        assert int(previous_months_date(1)) + 1 == now.year * 100 + now.month
