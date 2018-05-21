# coding=utf-8
"""

``fish_file`` 包含的是文件、路径处理相关的函数。

各类相对绝对文件的路径处理等都是开发时候经常需要处理的问题，fish_file 中的函数试图简化这些操作。

"""

# 2017.1.8 v1.0.9 created

import os
import sys
import inspect


# 生成当前路径下一级路径某文件的完整文件名
# ---
# 2016.4.7 v1.0.6, v1.0.7, create by david.yi
# 2017.1.8 v1.0.9 edit the function name, #19002
# 2018.1.30 1.31 v1.0.10 代码优化, #11004
# 2018.4.24 v1.0.11 加入 docstring
def get_abs_filename_with_sub_path(sub_path, filename):

    """
        生成当前路径下一级路径某文件的完整文件名；

        :param:
            * sub_path: (string) 下一级的某路径名称
            * filename: (string) 下一级路径的某个文件名
        :returns:
            * 返回类型 (tuple)，有两个值，第一个为 flag，第二个为文件名，说明见下
            * flag: (bool) 如果文件存在，返回 True，文件不存在，返回 False
            * abs_filename: (string) 指定 filename 的包含路径的长文件名

        举例如下::

            # 定义子路径名称
            path_name = 'test_sub_dir'
            # 定义文件名称
            filename = 'test_file.txt'
            # 生成当前路径下一级文件的完整路径名
            abs_filename = get_abs_filename_with_sub_path(path_name, filename)
            print(abs_filename)

        输出结果::

            (True, '/Users/yijun/Documents/dev_python/fishbase/demo/test_sub_dir/test_file.txt')

    """

    try:
        cur_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        abs_filename = os.path.join(cur_dir, sub_path, filename)

        flag = os.path.isfile(abs_filename)

        return flag, abs_filename

    except:

        flag = False
        return flag, None


# 生成使用模块时的下一级路径某文件的完整文件名
# 2016.5.18 create by David Yi
# 2017.1.8 v1.0.9 edit the function name, #19004
# 2018.4.24 v1.0.11 增加 docstring 支持
def get_abs_filename_with_sub_path_module(sub_path, filename):

    """
        生成使用模块时的下一级路径某文件的完整文件名；

        :param:
            * sub_path: (string) 下一级的某路径名称
            * filename: (string) 下一级路径的某个文件名
        :returns:
            * 返回类型 (tuple)，有两个值，第一个为 flag，第二个为文件名，说明见下
            * flag: (bool) 如果文件存在，返回 True，文件不存在，返回 False
            * abs_filename: (string) 指定 filename 的包含路径的长文件名，注意是模块安装的路径，不是应用程序的路径

        举例如下::

            # 定义子路径名称
            sub_path = 'test_sub_dir'
            # 定义存在的文件名称
            filename_existent = 'demo_file.txt'
            # 定义不存在的文件名称
            filename_non_existent = 'demo.txt'
            # 生成下一级路径文件的完整文件名
            result = get_abs_filename_with_sub_path_module(sub_path, filename_existent)
            print(result)

            result = get_abs_filename_with_sub_path_module(sub_path, filename_non_existent)
            print(result)

        输出结果::

            (True, '/Users/yijun/anaconda3/lib/python3.6/site-packages/fishbase/test_sub_dir/demo_file.txt')
            (False, '/Users/yijun/anaconda3/lib/python3.6/site-packages/fishbase/test_sub_dir/demo.txt')

    """

    cur_module_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    abs_filename = os.path.join(cur_module_dir, sub_path, filename)

    # 检查是否存在文件名
    if os.path.exists(abs_filename):
        return True, abs_filename
    else:
        return False, abs_filename


# 判断文件名是否没有输入后缀，没有的话则加上后缀
# create 2015.8.1. by david.yi
def auto_add_file_ext(short_filename, ext):

    temp_filename = short_filename
    if os.path.splitext(temp_filename)[1] == '':
        temp_filename += ext

    return temp_filename


# 检查指定类型的文件名是否在指定的路径下, 比如用来检查 conf 路径下的配置文件是否存在
# 2016.2.22 e2at v1.0.0 #10005, create by  David Yi
# 2017.1.8 v1.0.9 #19005, minor edit
def check_kind_path_file(kind_name, file_name):

    """
        检查指定类型的文件名是否在指定的路径下, 比如用来检查 conf 路径下的配置文件是否存在；

        :param:
            * kind_name: (string) 类别名称，比如 conf
            * file_name: (string)
        :returns:
            * 返回类型 (tuple)，有两个值
            * Flag: (bool) True: 文件存在，False: 文件不存在
            * abs_filename: (string) 要检查的文件的长文件名

        举例如下::

            # 定义路径（类型）
            kind_name = 'test_conf'
            # 定义文件名
            conf_filename = 'test_conf.ini'
            # 检查指定路径（类型）的文件名是否在指定的路径下
            result = check_kind_path_file(kind_name, conf_filename)
            print(result)

        输出结果::

            (True, '/Users/yijun/Documents/dev_python/fishbase/demo/test_conf/test_conf.ini')

    """

    # 文件路径
    kind_path = os.path.join(os.path.abspath(''), kind_name)

    # 完整文件名，包含路径
    abs_filename = os.path.join(kind_path, file_name)

    # 文件如果不存在
    if not os.path.isfile(abs_filename):
        return False, abs_filename
    # 文件存在
    else:
        return True, abs_filename


# 检查当前路径下的某个子路径是否存在, 不存在则创建
# 2016.10.4 by David Yi, v1.0.9 #19001
def check_sub_path_create(sub_path):

    """
        检查当前路径下的某个子路径是否存在, 不存在则创建；

        :param:
            * sub_path: (string) 下一级的某路径名称
        :returns:
            * 返回类型 (tuple)，有两个值
            * True: 路径存在，False: 不需要创建
            * False: 路径不存在，True: 创建成功

        举例如下::

            # 定义存在子路径名
            sub_path = 'test_sub_dir'
            # 检查当前路径下的一个子路径是否存在，不存在则创建
            result = check_sub_path_create(sub_path)
            print('check sub path:', sub_path)
            print(result)

        输出结果::

            check sub path: test_sub_dir
            (True, False)

    """

    # 获得当前路径
    cur_path = os.path.abspath('')
    # print('cur absolute path:', cur_path)

    # 生成 带有 sub_path_name 的路径
    path = os.path.join(cur_path, sub_path)
    # print('check path:', path)

    # 判断是否存在带有 sub_path 路径
    if os.path.exists(path):
        # print('path exists')
        # 返回 True: 路径存在, False: 不需要创建
        return True, False
    else:
        # print('log path not exists')
        os.makedirs(path)
        # 返回 False: 路径不存在  True: 路径已经创建
        # print('create sub path')
        return False, True
