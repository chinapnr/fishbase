# coding=utf-8
# fish_common.py 单元测试
# 2018.5.15 create by David Yi

import pytest
import sys
sys.path.append('../fishbase')
from fishbase.fish_common import *


# 2018.5.14 v1.0.11 #19027 create by David Yi, 开始进行单元测试
class TestFishCommon(object):

    # 测试 conf_as_dict() 通过的 tc
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

    # 测试 conf_as_dict() 通不过的 tc
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

    # 测试 GetMD5() 通过的 tc
    def test_md5_01(self):

        assert GetMD5.string('hello world!') == 'fc3ff98e8c6a0d3087d515c0473f8677'
        assert GetMD5.file('./test/test_conf.ini') == 'fb7528c9778b2377e30b0f7e4c26fef0'
        assert GetMD5.big_file('./test/test_conf.ini') == 'fb7528c9778b2377e30b0f7e4c26fef0'

    # 测试 GetMD5() 通不过的 tc
    def test_md5_02(self):

        assert GetMD5.string('hello world') != 'fc3ff98e8c6a0d3087d515c0473f8677'

        if sys.version > '3':
            with pytest.raises(FileNotFoundError):
                GetMD5.file('./test/test_conf1.ini')
        else:
            with pytest.raises(IOError):
                GetMD5.file('./test/test_conf1.ini')

        assert GetMD5.file('./test/test_conf.ini') != 'bb7528c9778b2377e30b0f7e4c26fef0'

    # 测试 if_json_contain() 通过和不通过 tc
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

    # 测试 splice_url_params() 通过和不通过 tc
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
