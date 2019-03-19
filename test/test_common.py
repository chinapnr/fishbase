# coding=utf-8
# fish_common.py 单元测试
# 2018.5.15 create by David Yi
import string
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

    # 测试 conf_as_dict()  tc
    def test_config_dict_01(self):
        # 读取配置文件
        ds = conf_as_dict(conf_filename, encoding='utf-8')
        d = ds[1]

        # 返回结果
        assert ds[0] is True
        # 返回长度
        assert ds[2] == 7
        # 某个 section 下面某个 key 的 value
        assert d['show_opt']['short_opt'] == 'b:d:v:p:f:'

    # 测试 conf_as_dict()  tc
    def test_config_dict_02(self):
        # 读取不存在的配置文件
        ds = conf_as_dict(error_conf_filename)

        # 返回结果
        assert ds[0] is False

        # 应该读不到返回的 dict 内容
        with pytest.raises(IndexError):
            d = ds[1]

    def test_config_dict_03(self):
        # 读取配置文件
        ds = conf_as_dict(conf_filename, encoding='utf-8')
        d = ds[1]

        list1 = ['show_opt', 'show_opt_common', 'show_opt_common2', 'get_args', 'show_rule_pattern',
                 'show_pattern', 'get_extra_rules']

        # 断言是否保序
        assert list(d.keys()) == list1

    def test_config_dict_04(self):
        # 读取配置文件, 中文编码
        ds = conf_as_dict(conf_filename, encoding='utf-8')
        d = ds[1]
    
        list1 = ['show_opt', 'show_opt_common', 'show_opt_common2', 'get_args', 'show_rule_pattern',
                 'show_pattern', 'get_extra_rules']
    
        # 断言是否保序
        assert list(d.keys()) == list1

    # 测试 FishMD5()  tc
    def test_md5_01(self):
        assert GetMD5.string('hello world!') == 'fc3ff98e8c6a0d3087d515c0473f8677'
        # different line separator will get different md5 value
        assert GetMD5.file(conf_filename) in ['c73ec5050bbff26ade9330bbe0bd7a25',
                                              '8d4f03dc6b223bd199be6aa53d5d4f5c']
        assert GetMD5.big_file(conf_filename) in ['c73ec5050bbff26ade9330bbe0bd7a25',
                                                  '8d4f03dc6b223bd199be6aa53d5d4f5c']
        salt_0 = 'salt'
        assert GetMD5.hmac_md5('hello world!', salt_0) == '191f82804523bfdafe0188bbbddd6587'
        salt_1 = 'm4xV2yGFSn'
        assert GetMD5.string('hello world!', salt_1) == '984d47991401fad7d920a30f715cfd22'

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
        dic02 = {'key1': '1111', 'key2': 'value2'}

        assert join_url_params(dic01) == '?key1=value1&key2=value2'
        assert splice_url_params(dic02) != '?key1=value1&key2=value2'

    # test singleton() test case
    def test_singleton_01(self):

        t1 = SingleTon()
        t1.x = 2
        t2 = SingleTon()
        t1.x += 1

        assert t2.x == t1.x

        t2.x = 5
        assert t1.x == 5

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

        assert is_contain_special_char(non_num_str, check_style=10020) is False

        if sys.version > '3':
            chinese_str1 = u'有zhongwen'.encode('gbk')
            with pytest.raises(TypeError):
                has_special_char(chinese_str1, check_style=charChinese)

    # test find_files() tc
    def test_find_files_01(self):
        path = './'
        exts_list = ['.ini', '.py']

        assert len(find_files(path)) >= len(find_files(path, exts=exts_list))

    # test hmac_sha256() tc
    def test_hmac_sha256_01(self):
        message = 'Hello HMAC'
        secret = '12345678'
        assert (hmac_sha256(secret, message) ==
                '5eb8bdabdaa43f61fb220473028e49d40728444b4322f3093decd9a356afd18f')

    # test FishSha256.hmac_sha256() tc
    def test_hmac_sha256_02(self):
        message = 'Hello HMAC'
        secret = '12345678'
        assert (GetSha256.hmac_sha256(secret, message) ==
                '5eb8bdabdaa43f61fb220473028e49d40728444b4322f3093decd9a356afd18f')

    # test FishSha256.hashlib_sha256() tc
    def test_hashlib_sha256_01(self):
        message = 'Hello HMAC'
        assert (GetSha256.hashlib_sha256(message) ==
                '4a1601381dfb85d6e713853a414f6b43daa76a82956911108512202f5a1c0ce4')

    # test get_random_str() tc
    def test_get_random_str_01(self):
        assert len(get_random_str(6)) == 6
    
        import re

        digits_pattern = re.compile('[0-9]+')
        letters_pattern = re.compile('[a-zA-Z]+')
        letters_digits_pattern = re.compile('[0-9a-zA-Z]+')
        punctuation_ord_list = [ord(item) for item in string.punctuation]
    
        letter_str = get_random_str(6)
        assert letters_pattern.match(letter_str)

        letter_digits_str = get_random_str(80, digits=True)
        assert letters_digits_pattern.match(letter_digits_str)
    
        digits_str = get_random_str(6, letters=False, digits=True)
        assert digits_pattern.match(digits_str)
    
        punctuation_str = get_random_str(6, letters=False, punctuation=True)
        for item in punctuation_str:
            assert ord(item) in punctuation_ord_list
    
        assert len(get_random_str(12, letters=False, digits=True, punctuation=True)) == 12

    # test has_space_element() tc
    def test_has_space_element_01(self):
        assert if_any_elements_is_space([1, 2, 'test_str']) is False

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
        assert list(remove_duplicate_elements(list1)) == [1, 5, 2, 9, 10]

        list2 = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    
        dict_demo1 = get_distinct_elements(list2, key=lambda d: (d['x'], d['y']))
        assert (list(dict_demo1)) == [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
    
        dict_demo2 = get_distinct_elements(list2, key=lambda d: d['x'])
        assert (list(dict_demo2)) == [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    
        dict_demo3 = get_distinct_elements(list2, key=lambda d: d['y'])
        assert (list(dict_demo3)) == [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]

    # test sort_objs_by_attr() tc
    def test_sort_objs_by_attr_01(self):
        class User(object):
            def __init__(self, user_id):
                self.user_id = user_id
    
        users = [User(23), User(3), User(99)]
        result_0 = sort_objs_by_attr(users, key='user_id')
        assert result_0[0].user_id == 3

        result_1 = sorted_objs_by_attr(users, key='user_id')
        assert result_1[0].user_id == 3
        
        reverse_result = sort_objs_by_attr(users, key='user_id', reverse=True)
        assert reverse_result[0].user_id == 99

    # test sort_objs_by_attr() tc
    def test_sort_objs_by_attr_02(self):
        class User(object):
            def __init__(self, user_id):
                self.user_id = user_id
    
        users = [User(23), User(3), User(99)]
    
        with pytest.raises(AttributeError):
            sort_objs_by_attr(users, key='user_id1')
    
        assert len(sort_objs_by_attr([], key='user_id')) == 0

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
        result_0 = paging(all_records, group_number=7, group_size=15)
        assert result_0 == [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

        result_1 = get_group_list_data(all_records, group_number=7, group_size=15)
        assert result_1 == [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

    # test paging() tc
    def test_paging_02(self):
        with pytest.raises(TypeError):
            paging('test')

        with pytest.raises(TypeError):
            paging(list(range(10)), group_number='asdsa')
    
        with pytest.raises(ValueError):
            paging(list(range(10)), group_number=-4)

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
        result_1 = transform_hump_to_underline(hump_param_dict)

        assert 'firstName' not in result_0
        assert 'first_name' in result_0
        assert 'first_name' in result_1

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
    def test_fish_isalpha(self):
        letter_str = 'test'
        mix_str = 'mix123'

        assert fish_isalpha(letter_str)
        assert not fish_isalpha(mix_str)
        assert not if_any_elements_is_letter(mix_str)

    # 测试 serialize_instance() tc
    def test_serialize_instance(self):
        # 定义两个对象
        class ObjA(object):
            def __init__(self, a, b):
                self.a = a
                self.b = b
    
        class ObjB(object):
            def __init__(self, x, y):
                self.x = x
                self.y = y

        obj_b = ObjB('string', [item for item in range(10)])
        obj_a = ObjA(1, obj_b)
        obj_attr_dict = serialize_instance(obj_a)

        assert '__classname__' in obj_attr_dict
        assert obj_attr_dict.get('__classname__') == 'ObjA'
        assert isinstance(obj_attr_dict.get('b'), dict)
