# coding=utf-8
"""

``fish_system`` 包含的是一些系统相关的函数和类。

"""
import sys


# 通过调用os.platform来获得当前操作系统名称
# 2017.2.13 create by David Yi, #19006
# 2018.5.23 edit by David Yi, #19037
def get_platform():
    """
    返回当前程序运行的操作系统名称, 基于 sys.platform() 进行封装;

    :param:
        * 无
    :return:
        * platform: (string) 返回 linux, osx, win 或者其他

    举例如下::

        print('current os:', get_platform())


    执行结果::

        current os: osx

    """

    platform = sys.platform

    if platform == 'win32':
        return 'win'
    elif platform == 'darwin':
        return 'osx'
    elif platform == 'linux' or platform == 'linux2':
        return 'linux'
    else:
        return platform
