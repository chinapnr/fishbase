# 2017.1.8 v1.0.9 #19003, remove file related functions to fish_fils.py
# 2018.1.31 v1.0.10,  change fish_file to file, short the lib name

import os
import sys
import inspect


# 生成当前路径下一级路径某文件的完整文件名
# 输入:
# sub_path: 下一级的某路径名称
# filename: 下一级路径的某个文件名
# 输出:
# flag: 如果文件存在，返回 True，文件不存在，返回 False
# abs_filename: 指定 filename 的包含路径的长文件名
# ---
# 2016.4.7 v1.0.6, v1.0.7, create by david.yi
# 2017.1.8 v1.0.9 edit the function name, #19002
# 2018.1.30 1.31 v1.0.10 代码优化, #11004
def get_abs_filename_with_sub_path(sub_path, filename):

    try:
        cur_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        abs_filename = os.path.join(cur_dir, sub_path, filename)

        flag = os.path.isfile(abs_filename)

        return flag, abs_filename

    except:

        flag = False
        return flag, None


# 生成使用模块时的下一级路径某文件的完整文件名
# 输入: 子目录, 文件名
# 输出: 文件是否存在标志, 完整文件名
# 2016.5.18 create by David Yi
# 2017.1.8 v1.0.9 edit the function name, #19004
def get_abs_filename_with_sub_path_module(sub_path, filename):

    cur_module_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    abs_filename = os.path.join(cur_module_dir, sub_path, filename)

    # 检查是否存在文件名
    if os.path.exists(abs_filename):
        return True, abs_filename
    else:
        return False, abs_filename


# 判断文件名是否没有输入后缀，加上后缀
# create 2015.8.1. by david.yi
def auto_add_file_ext(short_filename, ext):

    temp_filename = short_filename
    if os.path.splitext(temp_filename)[1] == '':
        temp_filename += ext

    return temp_filename


# 检查指定类型的文件名是否在指定的路径下, 主要用户检查 conf 路径下的配置文件等
# 2017.1.8 v1.0.9 #19005, minor edit
# 2016.2.22 e2at v1.0.0 #10005, create by david.yi ,
def check_kind_path_file(kind_name, file_name):

    # 文件路径
    kind_path = os.path.join(os.path.abspath(''), kind_name)

    # 完整文件名，包含路径
    abs_filename = os.path.join(kind_path, file_name)

    # 文件如果不存在，返回错误信息
    if not os.path.isfile(abs_filename):
        return False
    else:
        return True, abs_filename


# v1.0.9 #19001 检查当前路径下的某个子路径是否存在, 不存在则创建
# 2016.10.4 by david.yi
def check_sub_path_create(sub_path_name):
    # 获得当前路径
    cur_path = os.path.abspath('')
    # print('cur absolute path:', cur_path)

    # 生成 带有 sub_path_name 的路径
    path = os.path.join(cur_path, sub_path_name)
    # print('check path:', path)

    # 判断是否存在带有 sub_path_name 路径
    if os.path.exists(path):
        # print('path exists')
        # 返回 True, 路径存在
        return True
    else:
        # print('log path not exists')
        os.makedirs(path)
        # 返回 False: 路径不存在  True: 路径已经创建
        # print('create sub path')
        return False, True
