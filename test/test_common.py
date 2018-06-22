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

    # 测试 GetMD5()  tc
    def test_md5_03(self):
        salt = 'm4xV2yGFSn'
        assert GetMD5.string('hello world!', salt) == '984d47991401fad7d920a30f715cfd22'
    
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

    # test check_str() tc
    def test_check_str_01(self):
        non_chinese_str = 'meiyouzhongwen'
        chinese_str = u'有zhongwen'
        non_num_str = 'nonnumberstring'
        num_str = 'number123'
        
        assert check_str(non_chinese_str, check_style=charChinese) is False
        assert check_str(chinese_str, check_style=charChinese) is True
        assert check_str(non_num_str, check_style=charNum) is False
        assert check_str(num_str, check_style=charNum) is True
        assert check_str(non_num_str, check_style=10020) is False

        if sys.version > '3':
            chinese_str1 = u'有zhongwen'.encode('gbk')
            with pytest.raises(TypeError):
                check_str(chinese_str1, check_style=charChinese)

    # test find_files() tc
    def test_find_files_01(self):
        path = './'
        exts_list = ['.ini', '.py']

        assert len(find_files(path)) >= len(find_files(path, exts=exts_list))

    # test find_files() tc
    def test_hmac_sha256_01(self):
        message = 'Hello HMAC'
        secret = '12345678'
        assert hmac_sha256(secret, message) == '5eb8bdabdaa43f61fb220473028e49d40728444b4322f3093decd9a356afd18f'

    # test Base64() tc
    def test_base64_01(self):
        assert Base64.string('hello world') == b'aGVsbG8gd29ybGQ='
    
        file_base64 = (b'aW1wb3J0IHN5cw0Kc3lzLnBhdGguYXBwZW5kKCcuLi9maXNoYmFzZScpDQoNCmZyb20gdGVzdC50'
                       b'ZXN0X2ZpbGUgaW1wb3J0ICoNCmZyb20gdGVzdC50ZXN0X2NvbW1vbiBpbXBvcnQgKg0KZnJvbSB0'
                       b'ZXN0LnRlc3RfZGF0ZSBpbXBvcnQgKg0KZnJvbSB0ZXN0LnRlc3Rfc3lzdGVtIGltcG9ydCAqDQoN'
                       b'CnB5dGVzdC5tYWluKCkNCg==')
    
        assert Base64.file('./__init__.py') == file_base64
    
        assert Base64.decode(b'aGVsbG8gd29ybGQ=') == b'hello world'

    # test Base64()  tc
    def test_base64_02(self):
    
        assert GetMD5.string('hello world') != b'aGVsbG8gd29ybGQ=='
        assert Base64.decode(b'aGVsbG8gd29ybGQ=') != b'hello'
    
        if sys.version > '3':
            with pytest.raises(FileNotFoundError):
                GetMD5.file('./__init1__.py')
        else:
            with pytest.raises(IOError):
                GetMD5.file('./__init1__.py')
    
        assert GetMD5.file('./__init__.py') != b'bb7528c9778b2377e30b0f7e4c26fef0'
