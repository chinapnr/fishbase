# coding=utf-8
"""

``fish_ system`` 包含的是一些系统相关的函数和类。

"""
import sys


# 通过调用os.platform来获得当前操作系统名称
# 2017.2.13 create by David Yi, #19006
# 2018.5.23 edit by David Yi, #19037
def get_platform():
    """
    读入 ini 配置文件，返回根据配置文件内容生成的字典类型变量；

    :param:
        * conf_filename: (string) 需要读入的 ini 配置文件长文件名
    :returns:
        * flag: (bool) 读取配置文件是否正确，正确返回 True，错误返回 False
        * d: (dict) 如果读取配置文件正确返回的包含配置文件内容的字典
        * count: (int) 读取到的配置文件有多少个 key 的数量

    举例如下::

        print('--- conf_as_dict demo---')
        # 定义配置文件名
        conf_filename = 'test_conf.ini'
        # 读取配置文件
        ds = conf_as_dict(conf_filename)
        # 显示是否成功，所有 dict 的内容，dict 的 key 数量
        print('flag:', ds[0])
        print('dict:', ds[1])
        print('length:', ds[2])

        d = ds[1]

        # 显示一个 section 下的所有内容
        print('section show_opt:', d['show_opt'])
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
        section show_opt, key short_opt: b:d:v:p:f:
        section get_extra_rules, key erule_count: 2
        section get_extra_rules, key erule_type: extra_rule_1
        section get_extra_rules, key erule_type: extra_rule_2
        ---

    """

    if sys.platform == 'win32':
        return 'win32'
    elif sys.platform == 'darwin':
        return 'osx'
    elif sys.platform == 'linux':
        return 'linux'
    else:
        return sys.platform