# coding=utf-8
# fish_file.py 单元测试
# 2018.5.28 create by David Yi

import sys

sys.path.append('../fishbase')
from fishbase.fish_file import *


# 2018.5.28 v1.0.13 #19040, create by David Yi, fish_file unittest
class TestFishFile(object):

    # tc for get_abs_filename_with_sub_path()
    def test_get_abs_filename_with_sub_path_01(self):

        # 定义子路径名称
        path_name_0 = 'test'
        path_name_1 = 'test1'
        # 定义文件名称
        filename_0 = 'readme.111'
        filename_1 = 'test_file.py'

        # tc
        result = get_abs_filename_with_sub_path(path_name_0, filename_0)
        assert result[0] is False

        result = get_abs_filename_with_sub_path(path_name_0, filename_1)
        assert result[0] is True
        # print(result[1])

        abs_file = os.path.join(os.path.abspath(''), path_name_0, filename_1)
        assert result[1] == abs_file

        result = get_abs_filename_with_sub_path(path_name_1, filename_0)
        assert result[0] is False

        result = get_abs_filename_with_sub_path(path_name_1, filename_1)
        assert result[0] is False
