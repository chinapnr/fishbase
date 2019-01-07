# coding=utf-8
# fish_random.py 单元测试
# 2018.12.26 create by Hu Jun

import pytest
import datetime

from fishbase.fish_random import *


# 2018.12.26 v1.1.5 #163 create by Hu Jun
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
            get_random_zone_name('aa1234')

    # test gen_address() tc
    def test_gen_address_01(self):
        random_address = gen_address('310000')
        assert random_address.startswith('上海市')

    # test gen_address() tc
    def test_gen_address_02(self):
        with pytest.raises(ValueError):
            gen_address('aa1234')

    # test gen_bank_card() tc
    def test_gen_bank_card_01(self):
        random_bank_card = gen_bank_card('中国银行', 'CC')
        assert CardBin.check_bankcard(random_bank_card)

    # test gen_bank_card() tc
    def test_gen_bank_card_02(self):
        with pytest.raises(ValueError):
            gen_bank_card('fishbase银行', 'CC')

    # test gen_id() tc
    def test_gen_id_01(self):
        random_id_list = gen_id()
        assert len(random_id_list[0]) == 18
        # 测试身份证是否合法
        assert IdCard.check_number(random_id_list[0])

        random_id_list_1 = gen_id('310000')
        assert (random_id_list_1[0]).startswith('310')
        # 测试身份证是否合法
        assert IdCard.check_number(random_id_list_1[0])

        random_id_list_2 = gen_id('310000', age=30)
        year_now = datetime.datetime.now().year
        id_card_year = int(year_now) - 30
        # 测试身份证是否合法
        assert IdCard.check_number(random_id_list_2[0])
        assert (random_id_list_2[0]).startswith('310')
        assert int((random_id_list_2[0][6:10])) == id_card_year

        random_id_list_3 = gen_id('110000', age=20, gender='01', result_type='LIST')
        # 测试身份证是否合法
        check_valid_list = list(map(IdCard.check_number, random_id_list_3))
        assert all(check_valid_list)

        # 测试 province
        check_province_list = list(map(lambda item: item.startswith('110'), random_id_list_3))
        assert all(check_province_list)

        assert len(random_id_list_3) > 1
        # 测试性别选项
        check_gender_list = list(map(lambda item: int(item[16]) % 2 == 1, random_id_list_3))
        assert all(check_gender_list)
        # 测试 age
        year_now = datetime.datetime.now().year
        id_card_year = int(year_now) - 20
        check_age_list = list(map(lambda item: int(item[6:10]) == id_card_year, random_id_list_3))
        assert all(check_age_list)

    # test gen_id() tc
    def test_gen_id_02(self):
        with pytest.raises(ValueError):
            gen_id('123456')

    # test gen_company_name() tc
    def test_gen_company_name_01(self):
        random_name = gen_company_name()
        assert len(random_name) > 1
        assert random_name.endswith('公司')
