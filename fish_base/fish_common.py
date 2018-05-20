# coding=utf-8
"""

``fish_common`` 包含的是最通用的一些函数和类。

"""

# 2016.4.1 create fish_common.py by david.yi
# 2016.4.3 edit FishCache class, and edit get_cf_cache
# 2016.4.7 v1.0.6, v1.0.7  add get_long_filename_with_sub_dir()
# 2016.10.4 v1.0.9 add #19001 check_sub_path_create()
# 2017.1.8 v1.0.9 #19003, remove file related functions to fish_file.py
import sys

if sys.version > '3':
    import configparser
else:
    import ConfigParser as configparser

import uuid
import re
import hashlib
import os
from collections import OrderedDict


# 读入配置文件，返回根据配置文件内容生成的字典类型变量，减少文件读取次数
# 2017.2.23 #19008 create by David Yi
# 2018.2.12 #11014 edit by David Yi, 增加返回内容，字典长度,
# 2018.4.18 #19015 加入 docstring，完善文档说明
# 2018.5.14 v1.0.11 $19028 逻辑修改，更加严密
def conf_as_dict(conf_filename):

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
    flag = False

    # 检查文件是否存在
    if not(os.path.isfile(conf_filename)):
        return flag,

    cf = configparser.ConfigParser()

    # 读入 config 文件
    try:
        cf.read(conf_filename)
    except:
        flag = False
        return flag,

    d = dict(cf._sections)
    for k in d:
        d[k] = dict(cf._defaults, **d[k])
        d[k].pop('__name__', None)

    flag = True

    # 计算有多少 key
    count = len(d.keys())

    return flag, d, count


# 申明一个单例类
# 2018.2.13 create by David Yi, #11015
# 2018.4.20 5.19 edit, #19019，增加 docstring
class SingleTon(object):

    """
    申明一个单例类，可以作为需要单例类时候申明用的父类

    :param:
        无
    :returns:
        无

    举例如下::

        print('--- class singleton demo ---')
        t1 = SingleTon()
        t1.x = 2
        print('t1.x:', t1.x)

        t2 = SingleTon()

        t1.x += 1

        print('t1.x:', t1.x)
        print('t2.x:', t2.x)
        print('---')

    执行结果::

        --- class singleton demo ---
        t1.x: 2
        t1.x: 3
        t2.x: 3
        ---

    """

    _state = {}

    def __new__(cls, *args, **kwargs):
        ob = super(SingleTon, cls).__new__(cls)
        # 类维护所有实例的共享属性
        ob.__dict__ = cls._state
        return ob


# 通过调用os.platform来获得当前操作系统名称
# 2017.2.13 create by David Yi, #19006
def check_platform():
    if sys.platform == 'win32':
        return 'win32'
    elif sys.platform == 'darwin':
        return 'macos'
    elif sys.platform == 'linux':
        return 'linux'
    else:
        return sys.platform


# 对象序列化
# 输入: info: 要显示的字段解释，field_default：默认的字段名称
# 输出: 字段名称
# 2015.6.14  edit by david.yi
def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d


# 功能：获取带时间戳的流水号
# 输入参数：无
# 输出参数：流水号（string)
# 2017.2.22, create by David.Yi, #19006
def get_time_uuid():
    # Generate a UUID from a host ID, sequence number, and the current time.
    # If node is not given, getnode() is used to obtain the hardware address.
    # If clock_seq is given, it is used as the sequence number; otherwise a random 14-bit sequence number is chosen.
    return str(uuid.uuid1())


# 功能：判断参数列表是否存在不合法的参数，如果存在None或空字符串或空格字符串，则返回True, 否则返回False
# 输入参数：source 是参数列表或元组
# 输出参数：True : 有元素为 None，或空； False：没有元素为 None 或空
# 2017.2.22 edit by David.Yi, #19007
def if_any_elements_is_space(source):
    for i in source:
        if not (i and str(i).strip()):
            return True
    return False


# 2017.3.30 create by Leo #11001
# 功能：监测list或者元素是否含有特殊字符
# 输入：source 是参数列表或元组
# 输出：True：不包含特殊字符；False：包含特殊字符
def if_any_elements_is_special(source):

    if not re.match('^[a-zA-Z0-9_,-.|]+$', "".join(source)):
            return False

    return True


# 2017.3.30 create by Leo #11003
# 功能：监测list或者元素是否只包含数字
# 输入：source 是参数列表或元组
# 输出：True：只包含数字；False：不只包含数字
def if_any_elements_is_number(source):

    for i in source:

        if not i.isdigit():
            return False

    return True


# 2017.3.30 create by Leo #11004
# 功能：监测list或者元素是否只包含英文
# 输入：source 是参数列表或元组
# 输出：True：只包含英文；False：不只包含英文
def if_any_elements_is_letter(source):

    for i in source:

        if not i.isalpha():
            return False

    return True


# r2c1 v1.0.1 #12089
# 2016.4.3 edit class and function name
# 通过conf文件。eg ini，读取值，通过字典缓存来提高读取速度
class FishCache:
    __cache = {}

    def get_cf_cache(self, cf, section, key):
        # 生成 key，用于 dict
        temp_key = section + '_' + key

        if not (temp_key in self.__cache):
            self.__cache[temp_key] = cf[section][key]

        return self.__cache[temp_key]


# 2018.5.8 edit by David Yi, edit from Jia Chunying，#19026
class GetMD5(object):
    """
    封装了 MD5 计算的类，可以计算普通字符串和一般的文件，对于大文件采取逐步读入的方式，也可以快速计算

    举例如下::

        print('--- md5 demo ---')
        print('string md5:', GetMD5.string('hello world!'))
        print('file md5:', GetMD5.file(get_abs_filename_with_sub_path('test_conf', 'test_conf.ini')[1]))
        print('big file md5:', GetMD5.big_file(get_abs_filename_with_sub_path('test_conf', 'test_conf.ini')[1]))
        print('---')

    执行结果::

        string md5: fc3ff98e8c6a0d3087d515c0473f8677
        file md5: fb7528c9778b2377e30b0f7e4c26fef0
        big file md5: fb7528c9778b2377e30b0f7e4c26fef0

    """

    @staticmethod
    def string(s):
        """
        获取一个字符串的MD5值

        :param:
            * (string) str 需要进行 hash 的字符串
        :return:
            * (string) result 32位小写 MD5 值
        """
        m = hashlib.md5()
        m.update(s.encode('utf-8'))
        result = m.hexdigest()
        return result

    @staticmethod
    def file(filename):
        """
        获取一个文件的 MD5 值

        :param:
            * (string) filename 需要进行 hash 的文件名
        :return:
            * (string) result 32位小写 MD5 值
        """
        m = hashlib.md5()
        with open(filename, 'rb') as f:
            m.update(f.read())
            result = m.hexdigest()
            return result

    @staticmethod
    def big_file(filename):
        """
        获取一个大文件的 MD5 值

        :param:
            * (string) filename 需要进行 hash 的大文件路径
        :return:
            * (string) result 32位小写 MD5 值
        """

        md5 = hashlib.md5()
        with open(filename, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                md5.update(chunk)

        result = md5.hexdigest()
        return result


# 2018.5.15 v1.0.11 original by Lu Jie, edit by David Yi, #19029
def if_json_contain(left_json, right_json, op='strict'):
    """
    判断一个 json 是否包含另外一个 json 的 key，并且 value 相等；

    :param:
        * left_json: (dict) 需要判断的 json，我们称之为 left
        * right_json: (dict) 需要判断的 json，我们称之为 right，目前是判断 left 是否包含在 right 中
        * op: (string) 判断操作符，目前只有一种，默认为 strict，向后兼容
    :returns:
        * result: (bool) right json 包含 left json 的 key，并且 value 一样，返回 True，否则都返回 False

    举例如下::

        print('--- json contain demo ---')
        json1 = {"id": "0001"}
        json2 = {"id": "0001", "value": "File"}
        print(if_json_contain(json1, json2))
        print('---')

    执行结果::

        True

    """

    key_list = left_json.keys()

    if op == 'strict':
        for key in key_list:
            if not right_json.get(key) == left_json.get(key):
                return False
        return True


# 2018.3.8 edit by Xiang qinqin
# 2018.5.15 edit by David Yi, #19030
def splice_url_params(dic):
    """
    根据传入的键值对，拼接 url 后面 ? 的参数，比如 ?key1=value1&key2=value2

    :param:
        * dic: (dict) 参数键值对
    :returns:
        * result: (string) 拼接好的参数

    举例如下::

        dic1 = {'key1': 'value1', 'key2': 'value2'}
        print(splice_url_params(dic1))

    执行结果::

        ?key1=value1&key2=value2

    """

    od = OrderedDict(sorted(dic.items()))

    url = '?'
    for key, value in od.items():
        temp_str = key + '=' + value
        url = url + temp_str + '&'
    # 去掉最后一个&字符
    url = url[:len(url) - 1]
    return url
