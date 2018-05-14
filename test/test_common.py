# fish_common.py 单元测试
# 2017.5.23 create by Leo

import sys
sys.path.append('../fish_base')
from fish_base.fish_common import *


# 2018.5.14 v1.0.11 #19027 create by David Yi, 开始进行单元测试
class TestFishCommon(object):

    def test_config_dict(self):
        # 定义配置文件名
        # conf_filename = os.path.join(os.getcwd(), 'test', 'test_conf.ini')
        conf_filename = './test/test_conf.ini'

        # 读取配置文件
        ds = conf_as_dict(conf_filename)

        # 返回结果
        assert ds[0] is True
        # 返回长度
        assert ds[2] == 7
