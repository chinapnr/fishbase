# coding=utf-8
"""

``fish_file`` 包含的是文件、路径处理相关的函数。

各类相对绝对文件的路径处理等都是开发时候经常需要处理的问题，fish_file 中的函数试图简化这些操作。

"""

# 2017.1.8 v1.0.9 created

import os


# 生成当前路径下一级路径某文件的完整文件名
# ---
# 2016.4.7 v1.0.6, v1.0.7, create by David Yi
# 2017.1.8 v1.0.9 edit the function name, #19002
# 2018.1.30 1.31 v1.0.10 代码优化, #11004
# 2018.4.24 v1.0.11 加入 docstring
# 2018.5.28 v1.0.13 edit, #19040
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
            
            print('--- get_abs_filename_with_sub_path demo ---')
            # define sub dir
            path_name = 'sub_dir'
            # define not exists file
            filename = 'test_file.txt'

            abs_filename = get_abs_filename_with_sub_path(path_name, filename)
            # return False and abs filename
            print(abs_filename)

            # define exists file
            filename = 'demo.txt'
            abs_filename = get_abs_filename_with_sub_path(path_name, filename)
            # return True and abs filename
            print(abs_filename)
            print('---')

        输出结果::
            
            --- get_abs_filename_with_sub_path demo ---
            (False, '/Users/****/Documents/dev_python/fishbase/demo/sub_dir/test_file.txt')
            (True, '/Users/****/Documents/dev_python/fishbase/demo/sub_dir/demo.txt')
            ---
            
    """

    try:
        cur_path = os.getcwd()
        abs_filename = os.path.join(cur_path, sub_path, filename)

        flag = os.path.isfile(abs_filename)

        return flag, abs_filename

    except:

        flag = False
        return flag, None


# 判断文件名是否没有输入后缀，没有的话则加上后缀
# create 2015.8.1 by David Yi
# edit 2018.6.3 v1.0.13, #19044
# def check_ext_add(filename, ext):
#
#     temp_filename = filename
#     if os.path.splitext(temp_filename)[1] == '':
#         temp_filename += ext
#
#     return temp_filename


# 检查当前路径下的某个子路径是否存在, 不存在则创建
# 2016.10.4 v1.0.9 #19001, edit by David Yi
# 2018.5.28 v1.0.13 #19042, edit by David Yi
def check_sub_path_create(sub_path):

    """
    检查当前路径下的某个子路径是否存在, 不存在则创建；

    :param:
        * sub_path: (string) 下一级的某路径名称
    :return:
        * 返回类型 (tuple)，有两个值
        * True: 路径存在，False: 不需要创建
        * False: 路径不存在，True: 创建成功

    举例如下::
        
        print('--- check_sub_path_create demo ---')
        # 定义子路径名称
        sub_path = 'demo_sub_dir'
        # 检查当前路径下的一个子路径是否存在，不存在则创建
        print('check sub path:', sub_path)
        result = check_sub_path_create(sub_path)
        print(result)
        print('---')

    输出结果::
        
        --- check_sub_path_create demo ---
        check sub path: demo_sub_dir
        (True, False)
        ---
        
    """

    # 获得当前路径
    cur_path = os.path.abspath('')

    # 生成 带有 sub_path_name 的路径
    path = os.path.join(cur_path, sub_path)

    # 判断是否存在带有 sub_path 路径
    if os.path.exists(path):
        # 返回 True: 路径存在, False: 不需要创建
        return True, False
    else:
        os.makedirs(path)
        # 返回 False: 路径不存在  True: 路径已经创建
        return False, True


# 生成使用模块时的下一级路径某文件的完整文件名
# 2016.5.18 create by David Yi
# 2017.1.8 v1.0.9 edit the function name, #19004
# 2018.4.24 v1.0.11 增加 docstring 支持
# def get_abs_filename_with_sub_path_module(sub_path, filename):
#
#     """
#     生成使用模块时的下一级路径某文件的完整文件名；
#
#     :param:
#         * sub_path: (string) 下一级的某路径名称
#         * filename: (string) 下一级路径的某个文件名
#     :return:
#         * 返回类型 (tuple)，有两个值，第一个为 flag，第二个为文件名，说明见下
#         * flag: (bool) 如果文件存在，返回 True，文件不存在，返回 False
#         * abs_filename: (string) 指定 filename 的包含路径的长文件名，注意是模块安装的路径，不是应用程序的路径
#
#     举例如下::
#
#         # 定义子路径名称
#         sub_path = 'test_sub_dir'
#         # 定义存在的文件名称
#         filename_existent = 'demo_file.txt'
#         # 定义不存在的文件名称
#         filename_non_existent = 'demo.txt'
#         # 生成下一级路径文件的完整文件名
#         result = get_abs_filename_with_sub_path_module(sub_path, filename_existent)
#         print(result)
#
#         result = get_abs_filename_with_sub_path_module(sub_path, filename_non_existent)
#         print(result)
#
#     输出结果::
#
#         (True, '/Users/*****/anaconda3/lib/python3.6/site-packages/fishbase/test_sub_dir/demo_file.txt')
#         (False, '/Users/****/anaconda3/lib/python3.6/site-packages/fishbase/test_sub_dir/demo.txt')
#     """
#
#     cur_module_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
#     abs_filename = os.path.join(cur_module_dir, sub_path, filename)
#
#     # 检查是否存在文件名
#     if os.path.exists(abs_filename):
#         return True, abs_filename
#     else:
#         return False, abs_filename
