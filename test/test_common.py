# fish_common.py 单元测试
# 2017.5.23 create by Leo

import sys
sys.path.append('../fish_base')
from fish_base.fish_common import *


class TestFishCommon(object):

    def test_config_dict(self):
        # 定义配置文件名
        conf_filename = 'test_conf.ini'
        # 读取配置文件
        ds = conf_as_dict(conf_filename)

        # 显示是否成功，所有 dict 的内容，dict 的 key 数量
        # print('flag:', ds[0])
        # print('dict:', ds[1])
        # print('length:', ds[2])

        assert ds[0] is True
