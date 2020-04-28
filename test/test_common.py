# coding=utf-8
# fish_common.py 单元测试
# 2018.5.15 create by David Yi
# 2020.3.27 #257, edit by David Yi

import pytest

from fishbase.fish_common import *

# 定义当前路径
current_path = os.path.dirname(os.path.abspath(__file__))
# 定义配置文件名
conf_filename = os.path.join(current_path, 'test_conf.ini')
error_conf_filename = os.path.join(current_path, 'test_conf1.ini')
# 定义 yaml 文件名
yaml_filename = os.path.join(current_path, 'test_conf.yaml')
error_yaml_filename = os.path.join(current_path, 'test_conf1.yaml')


# 2018.5.14 v1.0.11 #19027 create by David Yi, 开始进行单元测试
# 2018.5.26 v1.0.13 #19038 edit, 增加 get_uuid() 的 ut
class TestFishCommon(object):

    # 测试 if_json_contain()  tc
    def test_json_contain_01(self):
        
        json01 = {"id": "0001"}
        json02 = {"id": "0001", "value": "Desk"}
        json10 = {"id": "0001", "value": "File"}
        json11 = {"id": "0002", "value": "File"}
        json12 = {"id1": "0001", "value": "File"}
        
        assert if_json_contain(json01, json10) is True
        assert if_json_contain(json02, json10) is False
        assert if_json_contain(json01, json11) is False
        assert if_json_contain(json01, json12) is False
    
    # 测试 join_url_params()  tc
    def test_join_url_params_01(self):
        
        dic01 = {'key1': 'value1', 'key2': 'value2'}

        assert join_url_params(dic01) == '?key1=value1&key2=value2'

    # test get_uuid() tc
    def test_get_uuid_01(self):
        
        u1 = get_uuid(udTime)
        u2 = get_uuid(udTime)
        
        assert u1 != u2
        
        # 获得uuid time 方式的系统编号，检查是否一致
        u1s = uuid.UUID(u1).fields[5]
        u2s = uuid.UUID(u2).fields[5]
        
        assert u1s == u2s
        
        u1 = get_time_uuid()
        u2 = get_time_uuid()
        
        # 获得uuid time 方式的系统编号，检查是否一致
        u1s = uuid.UUID(u1).fields[5]
        u2s = uuid.UUID(u2).fields[5]
        
        assert u1s == u2s
        
        u1 = get_uuid(udRandom)
        u2 = get_uuid(udRandom)
        
        assert u1 != u2
        
        u3 = get_uuid(10000)
        assert u3 != u1
    
    # test sorted_list_from_dict() tc
    def test_sorted_list_from_dict_01(self):
        
        # 定义待处理字典
        dict1 = {'a_key': 'a_value', '1_key': '1_value', 'A_key': 'A_value', 'z_key': 'z_value'}
        # 升序结果
        list1 = sorted_list_from_dict(dict1, odASC)
        
        assert list1 == ['1_value', 'A_value', 'a_value', 'z_value']
        
        # 降序结果
        list1 = sorted_list_from_dict(dict1, odDES)
        
        assert list1 == ['z_value', 'a_value', 'A_value', '1_value']
    
    # test has_special_char() tc
    def test_has_special_char_01(self):
        non_chinese_str = 'meiyouzhongwen'
        chinese_str = u'有zhongwen'
        non_num_str = 'nonnumberstring'
        num_str = 'number123'
        
        assert has_special_char(non_chinese_str, check_style=charChinese) is False
        assert has_special_char(chinese_str, check_style=charChinese) is True
        assert has_special_char(non_num_str, check_style=charNum) is False
        assert has_special_char(num_str, check_style=charNum) is True
        assert has_special_char(non_num_str, check_style=10020) is False
        
        if sys.version > '3':
            chinese_str1 = u'有zhongwen'.encode('gbk')
            with pytest.raises(TypeError):
                has_special_char(chinese_str1, check_style=charChinese)

    # test has_space_element() tc
    def test_has_space_element_01(self):

        assert has_space_element([1, 2, 'test_str']) is False
        
        assert has_space_element([0, 2]) is False
        
        assert has_space_element([1, 2, None]) is True
        
        assert has_space_element((1, [1, 2], 3, '')) is True
        
        assert has_space_element({'a': 1, 'b': 0}) is False
        
        assert has_space_element({'a': 1, 'b': []}) is True
        
        with pytest.raises(TypeError):
            has_space_element("test_str")
    
    # test get_distinct_elements() tc
    def test_get_distinct_elements_01(self):
        list1 = [1, 5, 2, 1, 9, 1, 5, 10]
        assert list(get_distinct_elements(list1)) == [1, 5, 2, 9, 10]

        list2 = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
        
        dict_demo1 = get_distinct_elements(list2, key=lambda d: (d['x'], d['y']))
        assert (list(dict_demo1)) == [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
        
        dict_demo2 = get_distinct_elements(list2, key=lambda d: d['x'])
        assert (list(dict_demo2)) == [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
        
        dict_demo3 = get_distinct_elements(list2, key=lambda d: d['y'])
        assert (list(dict_demo3)) == [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]

    # test get_query_param_from_url() tc
    def test_get_query_param_from_url_01(self):
        url = 'http://localhost:8811/mytest?page_number=1&page_size=10' \
              '&start_time=20180515&end_time=20180712'
        query_dict = get_query_param_from_url(url)
        assert 'page_number' in query_dict
        assert '20180515' in query_dict['start_time']
    
    # test paging() tc
    def test_paging_01(self):
        all_records = list(range(100))
        result_0 = get_paging_data(all_records, page_number=7, page_size=15)
        assert result_0 == [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

    # test paging() tc
    def test_paging_02(self):
        with pytest.raises(TypeError):
            get_paging_data('test')
        
        with pytest.raises(TypeError):
            get_paging_data(list(range(10)), page_number='asdsa')
        
        with pytest.raises(ValueError):
            get_paging_data(list(range(10)), page_number=-4)
    
    # test get_sub_dict() tc
    def test_get_sub_dict_01(self):
        dict1 = {'a': 1, 'b': 2, 'list1': [1, 2, 3]}
        list1 = ['a', 'list1', 'no_key']
        
        res_dict1 = get_sub_dict(dict1, list1)
        assert 'a' in res_dict1
        assert 'no_key' in res_dict1
        assert res_dict1.get('list1') == [1, 2, 3]
        
        res_dict2 = get_sub_dict(dict1, list1, default_value='new default')
        assert res_dict2.get('no_key') == 'new default'
    
    # test get_sub_dict() tc
    def test_get_sub_dict_02(self):
        dict1 = {'a': 1, 'b': 2, 'list1': [1, 2, 3]}
        list1 = ['a', 'list1', 'no_key']
        
        with pytest.raises(TypeError):
            get_sub_dict(dict1, 'test_list')
        
        with pytest.raises(TypeError):
            get_sub_dict('test_dict', list1)
    
    # test camelcase_to_underline() tc
    def test_camelcase_to_underline(self):
        hump_param_dict = {'firstName': 'Python', 'Second_Name': 'zhangshan', 'right_name': 'name'}
        result_0 = camelcase_to_underline(hump_param_dict)

        assert 'firstName' not in result_0
        assert 'first_name' in result_0
    
    # test find_same_between_dicts() tc
    def test_find_same_between_dicts_01(self):
        dict1 = {'x': 1, 'y': 2, 'z': 3}
        dict2 = {'w': 10, 'x': 1, 'y': 4}
        
        info = find_same_between_dicts(dict1, dict2)
        assert dict(info.item) == {'x': 1}
        assert info.key == {'x', 'y'}
        assert info.value == {1}
    
    # 测试 yaml_conf_as_dict()  tc
    def test_yaml_conf_as_dict_01(self):
        # 读取配置文件
        if sys.version > '3':
            ds = yaml_conf_as_dict(yaml_filename, encoding='utf-8')
        else:
            ds = yaml_conf_as_dict(yaml_filename)
        
        # 返回结果
        assert ds[0] is True
        assert len(ds[1]) == 2
        assert ds[-1] == 'Success'
    
    # 测试 yaml_conf_as_dict()  tc
    def test_yaml_conf_as_dict_02(self):
        # 读取配置文件
        if sys.version > '3':
            ds = yaml_conf_as_dict(error_yaml_filename, encoding='utf-8')
        else:
            ds = yaml_conf_as_dict(error_yaml_filename)
        
        # 返回结果
        assert ds[0] is False
        assert ds[-1] == 'File not exist'
    
    # 测试 fish_isalpha() tc
    def test_is_alpha(self):
        letter_str = 'test'
        mix_str = 'mix123'
        
        assert is_alpha(letter_str)
        assert not is_alpha(mix_str)

    # 测试 an2cn()  tc
    def test_an2cn_01(self):
        arabic_amount = '123456.78'
        assert RMBConversion.an2cn(arabic_amount) == '壹拾贰万叁仟肆佰伍拾陆圆柒角捌分'
        
        arabic_amount1 = 1234567.89
        assert RMBConversion.an2cn(arabic_amount1) == '壹佰贰拾叁万肆仟伍佰陆拾柒圆捌角玖分'

        arabic_amount2 = '123456.0'
        assert RMBConversion.an2cn(arabic_amount2) == '壹拾贰万叁仟肆佰伍拾陆圆整'
        
        arabic_amount3 = '123456'
        assert RMBConversion.an2cn(arabic_amount3) == '壹拾贰万叁仟肆佰伍拾陆圆整'
        
        arabic_amount4 = '1000000.54'
        assert RMBConversion.an2cn(arabic_amount4) == '壹佰万圆伍角肆分'

        arabic_amount5 = '1600.06'
        assert RMBConversion.an2cn(arabic_amount5) == '壹仟陆佰圆零陆分'

    # 测试 an2cn()  tc
    def test_an2cn_02(self):
        long_arabic_amount = '12'*10
        
        with pytest.raises(ValueError):
            RMBConversion.an2cn(long_arabic_amount)
        
        error_arabic_amount1 = '12.123'
        with pytest.raises(ValueError):
            RMBConversion.an2cn(error_arabic_amount1)

        error_arabic_amount2 = '12c.12'
        with pytest.raises(ValueError):
            RMBConversion.an2cn(error_arabic_amount2)

    # 测试 an2cn()  tc
    def test_an2cn_03(self):
        arabic_amount = '10310000001.54'
        assert RMBConversion.an2cn(arabic_amount) == '壹佰零叁亿壹仟万零壹圆伍角肆分'

        arabic_amount2 = '10010000001.54'
        assert RMBConversion.an2cn(arabic_amount2) == '壹佰亿壹仟万零壹圆伍角肆分'

        arabic_amount3 = '10310050001.54'
        assert RMBConversion.an2cn(arabic_amount3) == '壹佰零叁亿壹仟零伍万零壹圆伍角肆分'
        
        arabic_amount4 = '10300000000.54'
        assert RMBConversion.an2cn(arabic_amount4) == '壹佰零叁亿圆伍角肆分'

        arabic_amount5 = '10301000000.54'
        assert RMBConversion.an2cn(arabic_amount5) == '壹佰零叁亿零壹佰万圆伍角肆分'
        
        arabic_amount6 = '10300100000.54'
        assert RMBConversion.an2cn(arabic_amount6) == '壹佰零叁亿零壹拾万圆伍角肆分'
        
        arabic_amount7 = '10300010000.54'
        assert RMBConversion.an2cn(arabic_amount7) == '壹佰零叁亿零壹万圆伍角肆分'

    # 测试 cn2an()  tc
    def test_cn2an_01(self):
        chinese_amount = '壹拾贰万叁仟肆佰伍拾陆圆柒角捌分'
        assert RMBConversion.cn2an(chinese_amount) == float('123456.78')

        chinese_amount1 = '壹佰贰拾叁万肆仟伍佰陆拾柒圆捌角'
        assert RMBConversion.cn2an(chinese_amount1) == float('1234567.80')
        
        chinese_amount2 = '壹佰贰拾叁万肆仟伍佰陆拾柒圆整'
        assert RMBConversion.cn2an(chinese_amount2) == float('1234567.00')
        
        chinese_amount3 = '壹佰零叁亿零壹万圆伍角肆分'
        assert RMBConversion.cn2an(chinese_amount3) == float('10300010000.54')

        chinese_amount4 = '壹仟陆佰圆陆分'
        assert RMBConversion.cn2an(chinese_amount4) == float('1600.06')

    # 测试 cn2an()  tc
    def test_cn2an_02(self):
        error_chinese_amount = '二拾贰万叁仟肆佰伍拾陆圆柒角捌分'
        with pytest.raises(ValueError):
            RMBConversion.cn2an(error_chinese_amount)
            
        error_chinese_amount1 = '壹拾贰万叁千肆佰伍拾陆圆柒角捌分'
        with pytest.raises(ValueError):
            RMBConversion.cn2an(error_chinese_amount1)

        error_chinese_amount2 = '壹拾贰万叁千肆佰伍拾陆圆柒角八分'
        with pytest.raises(ValueError):
            RMBConversion.cn2an(error_chinese_amount2)

        error_chinese_amount2 = '壹拾贰万叁千肆佰伍拾陆圆柒角八分'
        with pytest.raises(ValueError):
            RMBConversion.cn2an(error_chinese_amount2)
            
    # 测试 split_str_by_length() tc
    def test_split_str_by_length_01(self):
        text = 'abcd'*5 + '123'
        str_list = split_str_by_length(text, 4)
        assert len(str_list) == 6
        assert ''.join(str_list) == text
        assert str_list[0] == 'abcd'
        assert str_list[-1] == '123'
    
    # 测试 split_str_by_length() tc
    def test_split_str_by_length_02(self):
        with pytest.raises(ValueError):
            text = 'abcd'*5 + '123'
            split_str_by_length(text, '12')
