# coding=utf-8
"""

``fish_common`` 包含的是最常用用的一些函数和类。

"""

# 2016.4.1 create fish_common.py by david.yi
# 2016.4.3 edit FishCache class, and edit get_cf_cache
# 2016.4.7 v1.0.6, v1.0.7  add get_long_filename_with_sub_dir()
# 2016.10.4 v1.0.9 add #19001 check_sub_path_create()
# 2017.1.8 v1.0.9 #19003, remove file related functions to fish_file.py
# 2019.1.18 v1.1.6 #200, remove function get_random_str to fish_random.py
import sys
import uuid
import copy
import re
import os
import warnings

import yaml
from collections import OrderedDict, namedtuple
from operator import attrgetter
import functools
import pathlib

if sys.version > '3':
    import configparser
    from urllib.parse import parse_qs, urlsplit, urlencode
else:
    import ConfigParser as configparser
    from urllib import urlencode
    from urlparse import parse_qs, urlsplit

# uuid kind const
udTime = 10001
udRandom = 10002

# order const
odASC = 10011
odDES = 10012

# character kind const
charChinese = 10021
charNum = 10022

# common data type
commonDataType = tuple([int, float, bool, complex, str, set, list, tuple, dict])


# v1.1.6 edit by Hu Jun
def show_deprecation_warn(old_fun, suggest_fun):
    warnings.simplefilter('always')
    warnings.warn('{} is deprecated, and in 2.x it will stop working. '
                  'Use {} instead.'.format(old_fun, suggest_fun),
                  DeprecationWarning, stacklevel=2)


# 读入配置文件，返回根据配置文件内容生成的字典类型变量，减少文件读取次数
# 2017.2.23 #19008 create by David Yi
# 2018.2.12 #11014 edit by David Yi, 增加返回内容，字典长度,
# 2018.4.18 #19015 加入 docstring，完善文档说明
# 2018.5.14 v1.0.11 #19028 逻辑修改，更加严密
# v1.0.15 edit by Hu Jun, #83
# v1.0.16 edit by Hu Jun, #94
# v1.0.17 edit by Hu Jun, #212
def conf_as_dict(conf_filename, encoding=None):
    """
    读入 ini 配置文件，返回根据配置文件内容生成的字典类型变量；

    :param:
        * conf_filename: (string) 需要读入的 ini 配置文件长文件名
        * encoding: (string) 文件编码
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
    if not pathlib.Path(conf_filename).is_file():
        return flag,

    cf = configparser.ConfigParser()

    # 读入 config 文件
    try:
        if sys.version > '3':
            cf.read(conf_filename, encoding=encoding)
        else:
            cf.read(conf_filename)
    except:
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


# 2015.6.14  edit by david.yi
# 2019.03.19 v1.1.7 edit by Hu Jun, edit from Jia Chunying，#215
def serialize_instance(obj):
    """
    对象序列化

    :param:
        * obj: (object) 对象实例

    :return:
        * obj_dict: (dict) 对象序列化字典

    举例如下::

        print('--- serialize_instance demo ---')
        # 定义两个对象
        class Obj(object):
            def __init__(self, a, b):
                self.a = a
                self.b = b

        class ObjB(object):
            def __init__(self, x, y):
                self.x = x
                self.y = y

        # 对象序列化
        b = ObjB('string', [item for item in range(10)])
        obj_ = Obj(1, b)
        print(serialize_instance(obj_))
        print('---')

    执行结果::

        --- serialize_instance demo ---
        {'__classname__': 'Obj', 'a': 1,
        'b': {'__classname__': 'ObjB', 'x': 'string', 'y': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}}
        ---

    """
    obj_dict = {'__classname__': type(obj).__name__}
    obj_dict.update(obj.__dict__)
    for key, value in obj_dict.items():
        if not isinstance(value, commonDataType):
            sub_dict = serialize_instance(value)
            obj_dict.update({key: sub_dict})
        else:
            continue
    return obj_dict


# 2018.5.26 v1.0.13 edit by David Yi，#19038
def get_uuid(kind):
    """
    获得不重复的 uuid，可以是包含时间戳的 uuid，也可以是完全随机的；基于 Python 的 uuid 类进行封装和扩展；

    支持 get_time_uuid() 这样的写法，不需要参数，也可以表示生成包含时间戳的 uuid，兼容 v1.0.12 以及之前版本；

    :param:
        * kind: (int) uuid 类型，整形常量 udTime 表示基于时间戳， udRandom 表示完全随机
    :return:
        * result: (string) 返回类似 66b438e3-200d-4fe3-8c9e-2bc431bb3000 的 uuid

    举例如下::

        print('--- uuid demo ---')
        # 获得带时间戳的uuid
        for i in range(2):
            print(get_uuid(udTime))

        print('---')

        # 时间戳 uuid 的简单写法，兼容之前版本
        for i in range(2):
            print(get_time_uuid())

        print('---')

        # 获得随机的uuid
        for i in range(2):
            print(get_uuid(udRandom))

        print('---')

    执行结果::

        --- uuid demo ---
        c8aa92cc-60ef-11e8-aa87-acbf52d15413
        c8ab7194-60ef-11e8-b7bd-acbf52d15413
        ---
        c8ab7368-60ef-11e8-996c-acbf52d15413
        c8ab741e-60ef-11e8-959d-acbf52d15413
        ---
        8e108777-26a1-42d6-9c4c-a0c029423eb0
        8175a81a-f346-46af-9659-077ad52e3e8f
        ---

    """

    if kind == udTime:
        return str(uuid.uuid1())
    elif kind == udRandom:
        return str(uuid.uuid4())
    else:
        return str(uuid.uuid4())


# 2018.5.26 v1.0.13 edit by David Yi，#19038
get_time_uuid = functools.partial(get_uuid, udTime)


# 2019.01.05 v1.1.6 edit by Hu Jun, #152
def if_any_elements_is_space(dic):
    show_deprecation_warn('if_any_elements_is_space', 'has_space_element')
    return has_space_element(dic)


# 2017.2.22 edit by David.Yi, #19007
# 2018.6.29 v1.0.14 edit by Hu Jun，#62
# 2019.01.05 v1.1.6 edit by Hu Jun, #152
def has_space_element(source):
    """
    判断对象中的元素，如果存在 None 或空字符串，则返回 True, 否则返回 False, 支持字典、列表和元组

    :param:
        * source: (list, set, dict) 需要检查的对象

    :return:
        * result: (bool) 存在 None 或空字符串或空格字符串返回 True， 否则返回 False

    举例如下::

        print('--- has_space_element demo---')
        print(has_space_element([1, 2, 'test_str']))
        print(has_space_element([0, 2]))
        print(has_space_element([1, 2, None]))
        print(has_space_element((1, [1, 2], 3, '')))
        print(has_space_element({'a': 1, 'b': 0}))
        print(has_space_element({'a': 1, 'b': []}))
        print('---')

    执行结果::

        --- has_space_element demo---
        False
        False
        True
        True
        False
        True
        ---

    """
    if isinstance(source, dict):
        check_list = list(source.values())
    elif isinstance(source, list) or isinstance(source, tuple):
        check_list = list(source)
    else:
        raise TypeError('source except list, tuple or dict, but got {}'.format(type(source)))
    for i in check_list:
        if i is 0:
            continue
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


# 2019.01.05 v1.1.6 edit by Hu Jun, #152
def if_any_elements_is_letter(source):
    show_deprecation_warn('if_any_elements_is_letter', 'fish_isalpha')
    return fish_isalpha(source)


# 2017.3.30 create by Leo #11004
# 功能：监测list或者元素是否只包含英文
# 输入：source 是参数列表或元组
# 输出：True：只包含英文；False：不只包含英文
def fish_isalpha(source):

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

        if temp_key not in self.__cache:
            self.__cache[temp_key] = cf[section][key]
        return self.__cache[temp_key]


# 2019.01.06 edit by Hu Jun, #152
# 2019.01.21 edit by Hu Jun, #200
class GetMD5(object):
    @staticmethod
    def string(s, salt=None):
        from fishbase.fish_crypt import FishMD5
        show_deprecation_warn('GetMD5.sting', 'fish_crypt.FishMD5.string')
        return FishMD5.string(s, salt=salt)

    @staticmethod
    def file(filename):
        from fishbase.fish_crypt import FishMD5
        show_deprecation_warn('GetMD5.file', 'fish_crypt.FishMD5.file')
        return FishMD5.file(filename)

    @staticmethod
    def big_file(filename):
        from fishbase.fish_crypt import FishMD5
        show_deprecation_warn('GetMD5.big_file', 'fish_crypt.FishMD5.big_file')
        return FishMD5.big_file(filename)

    @staticmethod
    def hmac_md5(s, salt):
        from fishbase.fish_crypt import FishMD5
        show_deprecation_warn('GetMD5.hmac_md5', 'fish_crypt.FishMD5.hmac_md5')
        return FishMD5.hmac_md5(s, salt)


# 2018.5.15 v1.0.11 original by Lu Jie, edit by David Yi, #19029
def if_json_contain(left_json, right_json, op='strict'):
    """
    判断一个 json 是否包含另外一个 json 的 key，并且 value 相等；

    :param:
        * left_json: (dict) 需要判断的 json，我们称之为 left
        * right_json: (dict) 需要判断的 json，我们称之为 right，目前是判断 left 是否包含在 right 中
        * op: (string) 判断操作符，目前只有一种，默认为 strict，向后兼容
    :return:
        * result: (bool) right json 包含 left json 的 key，并且 value 一样，返回 True，否则都返回 False

    举例如下::

        print('--- json contain demo ---')
        json1 = {"id": "0001"}
        json2 = {"id": "0001", "value": "File"}
        print(if_json_contain(json1, json2))
        print('---')

    执行结果::
        
        --- json contain demo ---
        True
        ---

    """

    key_list = left_json.keys()

    if op == 'strict':
        for key in key_list:
            if not right_json.get(key) == left_json.get(key):
                return False
        return True


# 2019.01.05 v1.1.6 edit by Hu Jun, #152
def splice_url_params(dic):
    show_deprecation_warn('splice_url_params', 'join_url_params')
    return join_url_params(dic)


# 2018.3.8 edit by Xiang qinqin
# 2018.5.15 edit by David Yi, #19030
# v1.0.15 edit by Hu Jun, #67
# 2019.01.05 v1.1.6 edit by Hu Jun, #152
def join_url_params(dic):
    """
    根据传入的键值对，拼接 url 后面 ? 的参数，比如 ?key1=value1&key2=value2

    :param:
        * dic: (dict) 参数键值对
    :return:
        * result: (string) 拼接好的参数

    举例如下::
        
        print('--- splice_url_params demo ---')
        dic1 = {'key1': 'value1', 'key2': 'value2'}
        print(splice_url_params(dic1))
        print('---')

    执行结果::
        
        --- splice_url_params demo ---
        ?key1=value1&key2=value2
        ---

    """

    od = OrderedDict(sorted(dic.items()))

    url = '?'
    temp_str = urlencode(od)
    
    url = url + temp_str
    
    return url


# v1.0.13 edit by Hu Jun, edit by David Yi，#19043
def sorted_list_from_dict(p_dict, order=odASC):
    """
    根据字典的 value 进行排序，并以列表形式返回

    :param:
        * p_dict: (dict) 需要排序的字典
        * order: (int) 排序规则，odASC 升序，odDES 降序，默认为升序
    :return:
        * o_list: (list) 排序后的 list

    举例如下::
        
        print('--- sorted_list_from_dict demo ---')
        # 定义待处理字典
        dict1 = {'a_key': 'a_value', '1_key': '1_value', 'A_key': 'A_value', 'z_key': 'z_value'}
        print(dict1)
        # 升序结果
        list1 = sorted_list_from_dict(dict1, odASC)
        print('ascending order result is:', list1)
        # 降序结果
        list1 = sorted_list_from_dict(dict1, odDES)
        print('descending order result is:', list1)
        print('---')

    执行结果::
        
        --- sorted_list_from_dict demo ---
        {'a_key': 'a_value', 'A_key': 'A_value', '1_key': '1_value', 'z_key': 'z_value'}
        ascending order result is: ['1_value', 'A_value', 'a_value', 'z_value']
        descending order result is: ['z_value', 'a_value', 'A_value', '1_value']
        ---
        
    """
    o_list = sorted(value for (key, value) in p_dict.items())

    if order == odASC:
        return o_list
    elif order == odDES:
        return o_list[::-1]


# 2019.01.05 v1.1.6 edit by Hu Jun, #152
def is_contain_special_char(p_str, check_style=charChinese):
    show_deprecation_warn('is_contain_special_char', 'has_special_char')
    return has_special_char(p_str, check_style=check_style)


# v1.0.13 edit by David Yi, edit by Hu Jun，#36
# v1.0.14 edit by Hu Jun #38
# 2019.01.05 v1.1.6 edit by Hu Jun, #152
def has_special_char(p_str, check_style=charChinese):
    """
    检查字符串是否含有指定类型字符
    
    :param:
        * p_str: (string) 需要判断的字符串
        * check_style: (string) 需要判断的字符类型，默认为 charChinese (编码仅支持utf-8), 支持 charNum，该参数向后兼容

    :return:
        * True 含有指定类型字符
        * False 不含有指定类型字符

    举例如下::
        
        print('--- has_special_char demo ---')
        p_str1 = 'meiyouzhongwen'
        non_chinese_result = has_special_char(p_str1, check_style=charChinese)
        print(non_chinese_result)
        
        p_str2 = u'有zhongwen'
        chinese_result = has_special_char(p_str2, check_style=charChinese)
        print(chinese_result)
        
        p_str3 = 'nonnumberstring'
        non_number_result = has_special_char(p_str3, check_style=charNum)
        print(non_number_result)
        
        p_str4 = 'number123'
        number_result = has_special_char(p_str4, check_style=charNum)
        print(number_result)
        print('---')

    执行结果::
        
        --- has_special_char demo ---
        False
        True
        False
        True
        ---

    """
    if check_style == charChinese:
        check_pattern = re.compile(u'[\u4e00-\u9fa5]+')
    elif check_style == charNum:
        check_pattern = re.compile(u'[0-9]+')
    else:
        return False
    
    try:
        if check_pattern.search(p_str):
            return True
        else:
            return False
    except TypeError as ex:
        raise TypeError(str(ex))


# v1.0.14 edit by Hu Jun, edit from Jia Chunying，#38
# v1.0.17 edit by Hu Jun, #212
def find_files(path, exts=None):
    """
    查找路径下的文件，返回指定类型的文件列表

    :param:
        * path: (string) 查找路径
        * exts: (list) 文件类型列表，默认为空

    :return:
        * files_list: (list) 文件列表

    举例如下::
        
        print('--- find_files demo ---')
        path1 = '/root/fishbase_issue'
        all_files = find_files(path1)
        print(all_files)
        exts_files = find_files(path1, exts=['.png', '.py'])
        print(exts_files)
        print('---')

    执行结果::

        --- find_files demo ---
        ['/root/fishbase_issue/test.png', '/root/fishbase_issue/head.jpg','/root/fishbase_issue/py/man.png'
        ['/root/fishbase_issue/test.png', '/root/fishbase_issue/py/man.png']
        ---

        """
    files_list = []
    for root, dirs, files in os.walk(path):
        for name in files:
            files_list.append(os.path.join(root, name))
    
    if exts is not None:
        return [file for file in files_list if pathlib.Path(file).suffix in exts]
        
    return files_list


# v1.1.6 edit by Hu Jun, #200
# v1.1.1 edit by Hu Jun, #115
# v1.0.14 edit by Hu Jun, #51
def get_random_str(length, letters=True, digits=False, punctuation=False):
    """
    获得指定长度，不同规则的随机字符串，可以包含数字，字母和标点符号
    
    :param:
        * length: (int) 随机字符串的长度
        * letters: (bool) 随机字符串是否包含字母，默认包含
        * digits: (bool) 随机字符串是否包含数字，默认不包含
        * punctuation: (bool) 随机字符串是否包含特殊标点符号，默认不包含

    :return:
        * random_str: (string) 指定规则的随机字符串

    举例如下::

        print('--- get_random_str demo---')
        print(get_random_str(6))
        print(get_random_str(6, digits=True))
        print(get_random_str(12, punctuation=True))
        print(get_random_str(6, letters=False, digits=True))
        print(get_random_str(12, letters=False, digits=True, punctuation=True))
        print('---')

    执行结果::

        --- get_random_str demo---
        nRBDHf
        jXG5wR
        )I;rz{ob&Clg
        427681
        *"4$0^`2}%9{
        ---

    """
    show_deprecation_warn('get_random_str', 'fish_random.gen_random_str')
    from fishbase.fish_random import gen_random_str
    return gen_random_str(length, length, has_letter=letters, has_digit=digits,
                          has_punctuation=punctuation)


# 2019.01.05 v1.1.6 edit by Hu Jun, #152
def remove_duplicate_elements(items, key=None):
    show_deprecation_warn('remove_duplicate_elements', 'get_distinct_elements')
    return get_distinct_elements(items, key=key)


# v1.0.15 edit by Hu Jun, #77 #63
def get_distinct_elements(items, key=None):
    """
    去除序列中的重复元素，使得剩下的元素仍然保持顺序不变，对于不可哈希的对象，需要指定 key ，说明去重元素

    :param:
        * items: (list) 需要去重的列表
        * key: (hook函数) 指定一个函数，用来将序列中的元素转换成可哈希类型

    :return:
        * result: (generator) 去重后的结果的生成器

    举例如下::

        print('--- remove_duplicate_elements demo---')
        list_demo = remove_duplicate_elements([1, 5, 2, 1, 9, 1, 5, 10])
        print(list(list_demo))
        list2 = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
        dict_demo1 = remove_duplicate_elements(list2, key=lambda d: (d['x'], d['y']))
        print(list(dict_demo1))
        dict_demo2 = remove_duplicate_elements(list2, key=lambda d: d['x'])
        print(list(dict_demo2))
        dict_demo3 = remove_duplicate_elements(list2, key=lambda d: d['y'])
        print(list(dict_demo3))
        print('---')

    执行结果::

        --- remove_duplicate_elements demo---
        [1, 5, 2, 9, 10]
        [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
        [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
        [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
        ---

    """
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


# 2019.01.05 v1.1.6 edit by Hu Jun, #152
def sorted_objs_by_attr(objs, key, reverse=False):
    show_deprecation_warn('sorted_objs_by_attr', 'sort_objs_by_attr')
    return sort_objs_by_attr(objs, key, reverse=reverse)


# v1.0.15 edit by Hu Jun, #64
def sort_objs_by_attr(objs, key, reverse=False):
    """
    对原生不支持比较操作的对象根据属性排序

    :param:
        * objs: (list) 需要排序的对象列表
        * key: (string) 需要进行排序的对象属性
        * reverse: (bool) 排序结果是否进行反转，默认为 False，不进行反转

    :return:
        * result: (list) 排序后的对象列表

    举例如下::

        print('--- sorted_objs_by_attr demo---')


        class User(object):
            def __init__(self, user_id):
                self.user_id = user_id
                
        
        users = [User(23), User(3), User(99)]
        result = sorted_objs_by_attr(users, key='user_id')
        reverse_result = sorted_objs_by_attr(users, key='user_id', reverse=True)
        print([item.user_id for item in result])
        print([item.user_id for item in reverse_result])
        print('---')

    执行结果::

        --- sorted_objs_by_attr demo---
        [3, 23, 99]
        [99, 23, 3]
        ---

    """
    if len(objs) == 0:
        return []
    if not hasattr(objs[0], key):
        raise AttributeError('{0} object has no attribute {1}'.format(type(objs[0]), key))
    result = sorted(objs, key=attrgetter(key), reverse=reverse)
    return result


# v1.0.15 edit by Hu Jun, #79
def get_query_param_from_url(url):
    """
    从 url 中获取 query 参数字典

    :param:
        * url: (string) 需要获取参数字典的 url

    :return:
        * query_dict: (dict) query 参数的有序字典，字典的值为 query 值组成的列表

    举例如下::

        print('--- get_query_param_from_url demo---')
        url = 'http://localhost:8811/mytest?page_number=1&page_size=10'
        query_dict = get_query_param_from_url(url)
        print(query_dict['page_size'])
        print('---')

    执行结果::

        --- get_query_param_from_url demo---
        ['10']
        ---

    """
    url_obj = urlsplit(url)
    query_dict = parse_qs(url_obj.query)

    return OrderedDict(query_dict)


# 2019.01.05 v1.1.6 edit by Hu Jun, #152
def get_group_list_data(data_list, group_number=1, group_size=10):
    show_deprecation_warn('get_group_list_data', 'paging')
    return paging(data_list, group_number=group_number, group_size=group_size)


# v1.1.0 edit by Hu Jun, #74
def paging(data_list, group_number=1, group_size=10):
    """
    获取分组列表数据

    :param:
        * data_list: (list) 需要获取分组的数据列表
        * group_number: (int) 分组信息，默认为 1
        * group_size: (int) 分组大小，默认为 10

    :return:
        * group_data: (list) 分组数据

    举例如下::

        print('--- paging demo---')
        all_records = [1, 2, 3, 4, 5]
        print(get_group_list_data(all_records))
        
        all_records1 = list(range(100))
        print(get_group_list_data(all_records1, group_number=5, group_size=15))
        print(get_group_list_data(all_records1, group_number=7, group_size=15))
        print('---')

    执行结果::

        --- paging demo---
        [1, 2, 3, 4, 5]
        [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74]
        [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
        ---

    """
    if not isinstance(data_list, list):
        raise TypeError('data_list should be a list, but we got {}'.format(type(data_list)))
        
    if not isinstance(group_number, int) or not isinstance(group_size, int):
        raise TypeError('group_number and group_size should be int, but we got group_number: {0}, '
                        'group_size: {1}'.format(type(group_number), type(group_size)))
    if group_number < 0 or group_size < 0:
        raise ValueError('group_number and group_size should be positive int, but we got '
                         'group_number: {0}, group_size: {1}'.format(group_number, group_size))

    start = (group_number - 1) * group_size
    end = group_number * group_size

    return data_list[start:end]


# v1.1.0 edit by Hu Jun, #89
def get_sub_dict(data_dict, key_list, default_value='default_value'):
    """
    从字典中提取子集

    :param:
        * data_dict: (dict) 需要提取子集的字典
        * key_list: (list) 需要获取子集的键列表
        * default_value: (string) 当键不存在时的默认值，默认为 default_value

    :return:
        * sub_dict: (dict) 子集字典

    举例如下::

        print('--- get_sub_dict demo---')
        dict1 = {'a': 1, 'b': 2, 'list1': [1,2,3]}
        list1 = ['a', 'list1', 'no_key']
        print(get_sub_dict(dict1, list1))
        print(get_sub_dict(dict1, list1, default_value='new default'))
        print('---')

    执行结果::

        --- get_sub_dict demo---
        {'a': 1, 'list1': [1, 2, 3], 'no_key': 'default_value'}
        {'a': 1, 'list1': [1, 2, 3], 'no_key': 'new default'}
        ---

    """
    if not isinstance(data_dict, dict):
        raise TypeError('data_dict should be dict, but we got {}'.format(type(data_dict)))

    if not isinstance(key_list, list):
        raise TypeError('key_list should be list, but we got {}'.format(type(key_list)))

    sub_dict = dict()
    for item in key_list:
        sub_dict.update({item: data_dict.get(item, default_value)})
    return sub_dict


# 2019.01.05 v1.1.6 edit by Hu Jun, #152
def transform_hump_to_underline(param_dict):
    show_deprecation_warn('transform_hump_to_underline', 'camelcase_to_underline')
    return camelcase_to_underline(param_dict)


# v1.1.1 edit by Hu Jun, #114
def camelcase_to_underline(param_dict):
    """
    将驼峰命名的参数字典键转换为下划线参数

    :param:
        * param_dict: (dict) 请求参数字典

    :return:
        * temp_dict: (dict) 转换后的参数字典

    举例如下::

        print('--- transform_hump_to_underline demo---')
        hump_param_dict = {'firstName': 'Python', 'Second_Name': 'san', 'right_name': 'name'}
        underline_param_dict = transform_hump_to_underline(hump_param_dict )
        print(underline_param_dict )
        print('---')

    执行结果::

        --- transform_hump_to_underline demo---
        {'first_name': 'Python', 'second_name': 'san', 'right_name': 'name'}
        ---

    """
    temp_dict = copy.deepcopy(param_dict)

    # 正则
    hump_to_underline = re.compile(r'([a-z]|\d)([A-Z])')
    for key in list(param_dict.keys()):
        # 将驼峰值替换为下划线
        underline_sub = re.sub(hump_to_underline, r'\1_\2', key).lower()
        temp_dict[underline_sub] = temp_dict.pop(key)
    return temp_dict


# v1.1.2 edit by Hu Jun, #80
def find_same_between_dicts(dict1, dict2):
    """
    查找两个字典中的相同点，包括键、值、项，仅支持 hashable 对象

    :param:
        * dict1: (dict) 比较的字典 1
        * dict2: (dict) 比较的字典 2

    :return:
        * dup_info: (namedtuple) 返回两个字典中相同的信息组成的具名元组
    
    举例如下::

        print('--- find_same_between_dicts demo---')
        dict1 = {'x':1, 'y':2, 'z':3}
        dict2 = {'w':10, 'x':1, 'y':2}
        res = find_same_between_dicts(dict1, dict2)
        print(res.item)
        print(res.key)
        print(res.value)
        print('---')

    执行结果::

        --- find_same_between_dicts demo---
        set([('x', 1)])
        {'x', 'y'}
        {1}
        ---

    """
    Same_info = namedtuple('Same_info', ['item', 'key', 'value'])
    same_info = Same_info(set(dict1.items()) & set(dict2.items()),
                          set(dict1.keys()) & set(dict2.keys()),
                          set(dict1.values()) & set(dict2.values()))
    return same_info


# v1.1.3 edit by Hu Jun, #94
# v1.0.17 edit by Hu Jun, #212
def yaml_conf_as_dict(file_path, encoding=None):
    """
    读入 yaml 配置文件，返回根据配置文件内容生成的字典类型变量

    :param:
        * file_path: (string) 需要读入的 yaml 配置文件长文件名
        * encoding: (string) 文件编码
        * msg: (string) 读取配置信息

    :return:
        * flag: (bool) 读取配置文件是否正确，正确返回 True，错误返回 False
        * d: (dict) 如果读取配置文件正确返回的包含配置文件内容的字典，字典内容顺序与配置文件顺序保持一致

    举例如下::

        print('--- yaml_conf_as_dict demo---')
        # 定义配置文件名
        conf_filename = 'test_conf.yaml'
        # 读取配置文件
        ds = yaml_conf_as_dict(conf_filename, encoding='utf-8')
        # 显示是否成功，所有 dict 的内容，dict 的 key 数量
        print('flag:', ds[0])
        print('dict length:', len(ds[1]))
        print('msg:', len(ds[1]))
        print('conf info: ', ds[1].get('tree'))
        print('---')

    执行结果::

        --- yaml_conf_as_dict demo---
        flag: True
        dict length: 2
        msg: Success
        conf info:  ['README.md', 'requirements.txt', {'hellopackage': ['__init__.py']},
        {'test': ['__init__.py']}, {'doc': ['doc.rst']}]
        ---

    """
    if not pathlib.Path(file_path).is_file():
        return False, {}, 'File not exist'

    try:
        if sys.version > '3':
            with open(file_path, 'r', encoding=encoding) as f:
                d = OrderedDict(yaml.load(f.read()))
                return True, d, 'Success'
        else:
            with open(file_path, 'r') as f:
                d = OrderedDict(yaml.load(f.read()))
                return True, d, 'Success'
    except:
        return False, {}, 'Unknow error'


# 2019.01.06 edit by Hu Jun, #152
class GetSha256(object):
    @staticmethod
    def hmac_sha256(secret, message):
        from fishbase.fish_crypt import FishSha256
        show_deprecation_warn('GetSha256.hmac_sha256', 'FishSha256.hmac_sha256')
        return FishSha256.hmac_sha256(secret, message)

    @staticmethod
    def hashlib_sha256(message):
        from fishbase.fish_crypt import FishSha256
        show_deprecation_warn('GetSha256.hashlib_sha256', 'FishSha256.hashlib_sha256')
        return FishSha256.hashlib_sha256(message)


# v1.0.14 original by Jia Chunying, edit by Hu Jun, #27
# v1.1.3 edit by Hu Jun, #100 move hmac_sha256 to GetSha256
hmac_sha256 = GetSha256.hmac_sha256
