# coding=utf-8
# fish_common.py 单元测试
# 2018.5.15 create by David Yi

import pytest
import sys
sys.path.append('../fishbase')
from fishbase.fish_common import *


# 2018.5.14 v1.0.11 #19027 create by David Yi, 开始进行单元测试
# 2018.5.26 v1.0.13 #19038 edit, 增加 get_uuid() 的 ut
class TestFishCommon(object):

    # 测试 conf_as_dict()  tc
    def test_config_dict_01(self):
        # 定义配置文件名
        conf_filename = './test/test_conf.ini'

        # 读取配置文件
        ds = conf_as_dict(conf_filename)
        d = ds[1]

        # 返回结果
        assert ds[0] is True
        # 返回长度
        assert ds[2] == 7
        # 某个 section 下面某个 key 的 value
        assert d['show_opt']['short_opt'] == 'b:d:v:p:f:'

    # 测试 conf_as_dict()  tc
    def test_config_dict_02(self):
        # 定义配置文件名
        conf_filename = './test/test_conf1.ini'

        # 读取配置文件
        ds = conf_as_dict(conf_filename)

        # 返回结果
        assert ds[0] is False

        # 应该读不到返回的 dict 内容
        with pytest.raises(IndexError):
            d = ds[1]

    # 测试 GetMD5()  tc
    def test_md5_01(self):

        assert GetMD5.string('hello world!') == 'fc3ff98e8c6a0d3087d515c0473f8677'
        assert GetMD5.file('./test/test_conf.ini') == 'fb7528c9778b2377e30b0f7e4c26fef0'
        assert GetMD5.big_file('./test/test_conf.ini') == 'fb7528c9778b2377e30b0f7e4c26fef0'

    # 测试 GetMD5()  tc
    def test_md5_02(self):

        assert GetMD5.string('hello world') != 'fc3ff98e8c6a0d3087d515c0473f8677'

        if sys.version > '3':
            with pytest.raises(FileNotFoundError):
                GetMD5.file('./test/test_conf1.ini')
        else:
            with pytest.raises(IOError):
                GetMD5.file('./test/test_conf1.ini')

        assert GetMD5.file('./test/test_conf.ini') != 'bb7528c9778b2377e30b0f7e4c26fef0'

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

    # 测试 splice_url_params()  tc
    def test_splice_url_params_01(self):

        dic01 = {'key1': 'value1', 'key2': 'value2'}
        dic02 = {'key1': '1111', 'key2': 'value2'}

        assert splice_url_params(dic01) == '?key1=value1&key2=value2'
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

    # test hmac_sha256() tc
    def test_hmac_sha256_01(self):

        # 定义待hash的消息
        message = 'Hello HMAC'
        # 定义HMAC的秘钥
        secret = '12345678'

        assert hmac_sha256(secret, message) == '5eb8bdabdaa43f61fb220473028e49d40728444b4322f3093decd9a356afd18f'

    # test if_element_is_timestamp() tc
    def test_if_element_is_timestamp_01(self):

        source1 = 1234567890
        assert if_element_is_timestamp(source1) is True

        source2 = '1234567890'
        assert if_element_is_timestamp(source2) is True

        source3 = [1234567890]
        assert if_element_is_timestamp(source3) is False

    # test check_number_len() tc
    def test_check_number_len_01(self):

        check_param = '1234567890'
        # 定义最小长度
        min_length = 0
        # 定义最大长度
        max_length = 64

        assert check_number_len(check_param, min_length, max_length) is True

        # 定义待检查类型为整型
        check_param_int = 1234567890
        assert check_number_len(check_param_int, min_length, max_length) is True

        # 定义最大长度为8
        max_length_8 = 8
        assert check_number_len(check_param, min_length, max_length_8) is False

        # 定义最小长度为20
        min_length_20 = 20
        assert check_number_len(check_param, min_length_20, max_length) is False

    # test check_str() tc
    def test_check_str_01(self):

        assert check_str('meiyouzhongwen') is False

        assert check_str('有zhongwen') is True