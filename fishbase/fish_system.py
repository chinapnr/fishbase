# coding=utf-8
"""

``fish_system`` 包含的是一些系统相关的函数和类。

"""
import sys
import pathlib
from collections import OrderedDict
import configparser


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


# v1.1.9 edit by Hu Jun, #222
# v1.2 edit by David Yi, #257
class MyConfigParser(configparser.ConfigParser):
    """
    自定义 MyConfigParser，重写 optionxform 方法，以便读取大小写敏感的配置文件
    """

    def __init__(self, defaults=None):
        configparser.ConfigParser.__init__(self, defaults=None)

    def optionxform(self, optionstr):
        return optionstr


# 读入配置文件，返回根据配置文件内容生成的字典类型变量，减少文件读取次数
# 2017.2.23 #19008 create by David Yi
# 2018.2.12 #11014 edit by David Yi, 增加返回内容，字典长度,
# 2018.4.18 #19015 加入 docstring，完善文档说明
# 2018.5.14 v1.0.11 #19028 逻辑修改，更加严密
# v1.0.15 edit by Hu Jun, #83
# v1.0.16 edit by Hu Jun, #94
# v1.0.17 edit by Hu Jun, #212
# v1.1.9 edit by Hu Jun, #222
# v1.2 edit by David Yi, #257
def conf_as_dict(conf_filename, encoding=None, case_sensitive=False):
    """
    读入 ini 配置文件，返回根据配置文件内容生成的字典类型变量；

    :param:
        * conf_filename: (string) 需要读入的 ini 配置文件长文件名
        * encoding: (string) 文件编码
        * case_sensitive: (bool) 是否大小写敏感，默认为 False
    :return:
        * flag: (bool) 读取配置文件是否正确，正确返回 True，错误返回 False
        * d: (dict) 如果读取配置文件正确返回的包含配置文件内容的字典，字典内容顺序与配置文件顺序保持一致
        * count: (int) 读取到的配置文件有多少个 key 的数量

    举例如下::

        print('--- conf_as_dict demo---')
        # 定义配置文件名
        conf_filename = 'test_conf.ini'
        # 读取配置文件
        ds = conf_as_dict(conf_filename)
        ds1 = conf_as_dict(conf_filename, case_sensitive=True)
        # 显示是否成功，所有 dict 的内容，dict 的 key 数量
        print('flag:', ds[0])
        print('dict:', ds[1])
        print('length:', ds[2])

        d = ds[1]
        d1 = ds1[1]

        # 显示一个 section 下的所有内容
        print('section show_opt:', d['show_opt'])
        # 显示一个 section 下的所有内容，大小写敏感
        print('section show_opt:', d1['show_opt'])
        # 显示一个 section 下面的 key 的 value 内容
        print('section show_opt, key short_opt:', d['show_opt']['short_opt'])

        # 读取一个复杂的section，先读出 key 中的 count 内容，再遍历每个 key 的 value
        i = int(d['get_extra_rules']['erule_count'])
        print('section get_extra_rules, key erule_count:', i)
        for j in range(i):
            print('section get_extra_rules, key erule_type:', d['get_extra_rules']['erule_'+str(j)])
        print('---')

    执行结果::

        --- conf_as_dict demo---
        flag: True
        dict: (omit)
        length: 7
        section show_opt: {'short_opt': 'b:d:v:p:f:', 'long_opt': 'region=,prov=,mer_id=,mer_short_name=,web_status='}
        section show_opt: {'Short_Opt': 'b:d:v:p:f:', 'Long_Opt': 'region=,prov=,mer_id=,mer_short_name=,web_status='}
        section show_opt, key short_opt: b:d:v:p:f:
        section get_extra_rules, key erule_count: 2
        section get_extra_rules, key erule_type: extra_rule_1
        section get_extra_rules, key erule_type: extra_rule_2
        ---

    """
    flag = False

    # 检查文件是否存在
    if not pathlib.Path(conf_filename).is_file():
        return flag,

    # 判断是否对大小写敏感
    cf = configparser.ConfigParser() if not case_sensitive else MyConfigParser()

    # 读入 config 文件
    try:
        if sys.version > '3':
            cf.read(conf_filename, encoding=encoding)
        else:
            cf.read(conf_filename)
    except Exception:
        flag = False
        return flag,

    d = OrderedDict(cf._sections)
    for k in d:
        d[k] = OrderedDict(cf._defaults, **d[k])
        d[k].pop('__name__', None)

    flag = True

    # 计算有多少 key
    count = len(d.keys())

    return flag, d, count
