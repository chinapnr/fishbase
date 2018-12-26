# coding=utf-8
# fish_date.py 单元测试
# 2018.6.11 create by Hu Jun

import pytest

from fishbase.fish_random import *


# 2018.6.11 v1.1.5 #163 create by Hu Jun
class TestFishRandom(object):
    # test gen_string_by_range() tc
    def test_gen_string_by_range_01(self):
        assert 1 <= len(gen_string_by_range(1, 5)) <= 5
        assert gen_string_by_range(1, 5, prefix='fishbase_').startswith('fishbase_')
        assert gen_string_by_range(1, 5, suffix='.py')[-3:] == '.py'

    # test gen_string_by_range() tc
    def test_gen_string_by_range_02(self):
        with pytest.raises(ValueError):
            gen_string_by_range(1, '12', prefix='fishbase_')
        
        with pytest.raises(ValueError):
            gen_string_by_range(10, 4, prefix='fishbase_')
