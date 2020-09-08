# coding=utf-8
# fish_system.py 单元测试
# 2018.5.26 create by David Yi
# 2020.3.27 edit by David Yi; #257

import platform
import os
import pytest

from fishbase.fish_system import *

# 定义当前路径
current_path = os.path.dirname(os.path.abspath(__file__))
# 定义配置文件名
conf_filename = os.path.join(current_path, 'test_conf.ini')
conf_filename_not_exist = os.path.join(current_path, 'test_conf_not_exist.ini')
conf_filename_empty = os.path.join(current_path, 'test_conf_empty.ini')
conf_filename_bad_data = os.path.join(current_path, 'test_conf_bad_data.ini')

# 2018.5.26 v1.0.13 create by David Yi, fish_system unittest
class TestFishSystem(object):

    # 测试 get_platform() 的 tc
    def test_get_platform_01(self):

        os_name = get_platform()

        result = platform.system()

        os_name_test = ''

        if result == 'Linux':
            os_name_test = 'linux'
        elif result == 'Darwin':
            os_name_test = 'osx'
        elif result == 'Windows':
            os_name_test = 'win'

        # 返回结果
        assert os_name == os_name_test


# 2020.3.27 v1.2, 建立新的测试类，调整单元类别后，移动原来的单元测试文件
class TestFishConfigDict(object):

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
        ds = conf_as_dict(conf_filename_not_exist)

        # 返回结果
        assert ds[0] is False
        assert ds[1] == {}
        # # 应该读不到返回的 dict 内容
        # with pytest.raises(IndexError):
        #     d = ds[1]

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

        # 断言正常读取中文
        assert d['get_extra_rules']['zh_item'] == '中文'

    def test_config_dict_05(self):
        # 读取配置文件, 大小写敏感
        ds = conf_as_dict(conf_filename, encoding='utf-8', case_sensitive=True)
        d = ds[1]

        for item in ['Short_Opt', 'Long_Opt']:
            assert item in d.get('show_opt')

    # 测试 conf_as_dict()  tc
    def test_config_dict_06(self):
        # 读取空配置文件
        ds = conf_as_dict(conf_filename_empty)

        # 返回结果
        assert ds[0] is True
        assert isinstance(ds[1], OrderedDict)
        assert ds[2] == 0

    # 测试 conf_as_dict()  tc
    def test_config_dict_07(self):
        # 读取坏的配置文件
        ds = conf_as_dict(conf_filename_bad_data)

        # 返回结果
        assert ds[0] is False
        assert 'errors' in ds[2]

