# coding=utf-8
# fish_system.py 单元测试
# 2018.5.26 create by David Yi

import platform

from fishbase.fish_system import *


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
