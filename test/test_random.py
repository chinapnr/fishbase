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

    # test gen_name() tc
    def test_gen_name(self):
        full_name = gen_name()
        assert isinstance(full_name, str)
        assert 2 <= len(full_name) <= 3
        full_name_2 = gen_name("赵", "01", 3)
        assert isinstance(full_name_2, str)
        assert len(full_name_2) == 3
        assert full_name_2.startswith("赵")

    # test gen_mobile() tc
    def test_gen_mobile(self):
        mobile = gen_mobile()
        assert isinstance(mobile, str)
        assert len(mobile) == 11

    # test gen_float_by_range() tc
    def test_gen_float_by_range_01(self):
        assert 1.0 <= gen_float_by_range(1.0, 9.0) <= 9.0
        assert len(str(gen_float_by_range(1.0, 9.0, decimals=4)).split('.')[-1]) == 4

    # test gen_float_by_range() tc
    def test_gen_float_by_range_02(self):
        with pytest.raises(ValueError):
            gen_float_by_range(1, '9')
        with pytest.raises(ValueError):
            gen_float_by_range(1, 9, decimals='12')

    # test get_random_zone_name() tc
    def test_get_random_zone_name_01(self):
        zone_name = get_random_zone_name(310000)
        assert zone_name in ['市辖区', '黄浦区', '南市区', '卢湾区', '徐汇区', '长宁区', '静安区',
                             '普陀区', '闸北区', '虹口区', '扬浦区', '闵行区', '宝山区', '嘉定区',
                             '浦东新区', '金山区', '松江区', '青浦区', '南汇区', '奉贤区', '市辖县',
                             '南汇县', '奉贤县', '松江县', '金山县', '青浦县', '崇明县']

    # test get_random_zone_name() tc
    def test_get_random_zone_name_02(self):
        with pytest.raises(ValueError):
            get_random_zone_name('123456')
