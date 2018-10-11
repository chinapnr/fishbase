# coding=utf-8
"""

``fish_common`` 包含的是最常用用的一些函数和类。

"""

# 2016.4.1 create fish_common.py by david.yi
# 2016.4.3 edit FishCache class, and edit get_cf_cache
# 2016.4.7 v1.0.6, v1.0.7  add get_long_filename_with_sub_dir()
# 2016.10.4 v1.0.9 add #19001 check_sub_path_create()
# 2017.1.8 v1.0.9 #19003, remove file related functions to fish_file.py
import sys
import uuid
import copy
import re
import hashlib
import hmac
import os
import base64
import string
import random
from collections import OrderedDict
from operator import attrgetter
import functools

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


# 读入配置文件，返回根据配置文件内容生成的字典类型变量，减少文件读取次数
# 2017.2.23 #19008 create by David Yi
# 2018.2.12 #11014 edit by David Yi, 增加返回内容，字典长度,
# 2018.4.18 #19015 加入 docstring，完善文档说明
# 2018.5.14 v1.0.11 #19028 逻辑修改，更加严密
# v1.0.15 edit by Hu Jun, #83
# v1.0.16 edit by Hu Jun, #94
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
    if not(os.path.isfile(conf_filename)):
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


# 对象序列化
# 2015.6.14  edit by david.yi
def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d


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


# 2017.2.22 edit by David.Yi, #19007
# 2018.6.29 v1.0.14 edit by Hu Jun，#62
def if_any_elements_is_space(source):
    """
    判断对象中的元素，如果存在None或空字符串或空格字符串，则返回True, 否则返回False, 支持字典、列表和元组

    :param:
        * source: (list, set, dict) 需要检查的对象

    :return:
        * result: (bool) 存在None或空字符串或空格字符串返回True， 否则返回False

    举例如下::

        print('--- if_any_elements_is_space demo---')
        print(if_any_elements_is_space([1, 2, 'test_str']))
        print(if_any_elements_is_space([0, 2]))
        print(if_any_elements_is_space([1, 2, None]))
        print(if_any_elements_is_space((1, [1, 2], 3, '')))
        print(if_any_elements_is_space({'a': 1, 'b': 0}))
        print(if_any_elements_is_space({'a': 1, 'b': []}))
        print('---')

    执行结果::

        --- if_any_elements_is_space demo---
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
# 2018.6.12 edit by Hu Jun, edit from Jia Chunying，#37
class GetMD5(object):
    """
    计算普通字符串和一般的文件，对于大文件采取逐步读入的方式，也可以快速计算；基于 Python 的 hashlib.md5() 进行封装和扩展；

    举例如下::

        print('--- md5 demo ---')
        print('string md5:', GetMD5.string('hello world!'))
        print('file md5:', GetMD5.file(get_abs_filename_with_sub_path('test_conf', 'test_conf.ini')[1]))
        print('big file md5:', GetMD5.big_file(get_abs_filename_with_sub_path('test_conf', 'test_conf.ini')[1]))
        print('---')

    执行结果::
        
        --- md5 demo ---
        string md5: fc3ff98e8c6a0d3087d515c0473f8677
        file md5: fb7528c9778b2377e30b0f7e4c26fef0
        big file md5: fb7528c9778b2377e30b0f7e4c26fef0
        ---

    """

    @staticmethod
    def string(s, salt=None):
        """
        获取一个字符串的MD5值

        :param:
            * (string) str 需要进行 hash 的字符串
            * (string) salt 随机字符串，默认为None
        :return:
            * (string) result 32位小写 MD5 值
        """
        m = hashlib.md5()
        s = s.encode('utf-8') + salt.encode('utf-8') if salt is not None else s.encode('utf-8')
        m.update(s)
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


# 2018.3.8 edit by Xiang qinqin
# 2018.5.15 edit by David Yi, #19030
# v1.0.15 edit by Hu Jun, #67
def splice_url_params(dic):
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


# v1.0.13 edit by David Yi, edit by Hu Jun，#36
# v1.0.14 edit by Hu Jun #38
def is_contain_special_char(p_str, check_style=charChinese):
    """
    检查字符串是否含有指定类型字符
    
    :param:
        * p_str: (string) 需要判断的字符串
        * check_style: (string) 需要判断的字符类型，默认为 charChinese(编码仅支持utf-8),支持 charNum，该参数向后兼容

    :return:
        * True 含有指定类型字符
        * False 不含有指定类型字符

    举例如下::
        
        print('--- is_contain_special_char demo ---')
        p_str1 = 'meiyouzhongwen'
        non_chinese_result = check_str(p_str1, check_style=charChinese)
        print(non_chinese_result)
        
        p_str2 = u'有zhongwen'
        chinese_result = check_str(p_str2, check_style=charChinese)
        print(chinese_result)
        
        p_str3 = 'nonnumberstring'
        non_number_result = check_str(p_str3, check_style=charNum)
        print(non_number_result)
        
        p_str4 = 'number123'
        number_result = check_str(p_str4, check_style=charNum)
        print(number_result)
        print('---')

    执行结果::
        
        --- is_contain_special_char demo ---
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
        ['/root/fishbase_issue/test.png', '/root/fishbase_issue/head.jpg', '/root/fishbase_issue/py/man.png', '/root/fishbase_issue/py/issue.py']
        ['/root/fishbase_issue/test.png', '/root/fishbase_issue/py/man.png', '/root/fishbase_issue/py/issue.py']
        ---

        """
    files_list = []
    for root, dirs, files in os.walk(path):
        for name in files:
            files_list.append(os.path.join(root, name))
    
    if exts is not None:
        return [file for file in files_list if os.path.splitext(file)[-1] in exts]
        
    return files_list


# v1.0.14 original by Jia Chunying, edit by Hu Jun, #27
def hmac_sha256(secret, message):
    """
    hmac_sha256，通过秘钥获取消息的hash值

    :param:
        * secret: (string) 密钥
        * message: (string) 消息输入

    :return:
        * hashed_str: (string) 长度为64的小写hex string 类型的hash值

    举例如下::

        print('--- hmac_sha256 demo---')
        # 定义待hash的消息
        message = 'Hello HMAC'
        # 定义HMAC的秘钥
        secret = '12345678'
        hashed_str = hmac_sha256(secret, message)
        print(hashed_str)
        print('---')

    执行结果::

        --- hmac_sha256 demo---
        5eb8bdabdaa43f61fb220473028e49d40728444b4322f3093decd9a356afd18f
        ---

    """
    hashed_str = hmac.new(secret.encode('utf-8'),
                          message.encode('utf-8'),
                          digestmod=hashlib.sha256).hexdigest()
    return hashed_str


# v1.0.14 edit by Hu Jun, #59
class Base64:
    """
    计算返回文件和字符串的base64编码字符串

    举例如下::

        print('--- Base64 demo ---')
        print('string base64:', Base64.string('hello world!'))
        print('file base64:', Base64.file(get_abs_filename_with_sub_path('test_conf', 'test_conf.ini')[1]))
        print('decode base64:', Base64.decode(b'aGVsbG8gd29ybGQ='))
        print('---')

    执行结果::

        --- Base64 demo ---
        string base64: b'aGVsbG8gd29ybGQ='
        file base64: b'IyEvYmluL2Jhc2gKCmNkIC9yb290L3d3dy9zaW5nbGVfcWEKCm5vaHVwIC9yb290L2FwcC9weXRob24zNjIvYmluL2d1bmljb3JuIC1jIGd1bmljb3JuLmNvbmYgc2luZ2xlX3NlcnZlcjphcHAK'
        decode base64: b'hello world'
        ---

    """
    
    @staticmethod
    def string(s):
        """
        获取一个字符串的base64值

        :param:
            * (string) s 需要进行 base64编码 的字符串
        :return:
            * (bytes) base64 编码结果
        """
        return base64.b64encode(s.encode('utf-8'))
    
    @staticmethod
    def file(filename):
        """
        获取一个文件的base64值

        :param:
            * (string) filename 需要进行 base64编码 文件路径
        :return:
            * (bytes) base64 编码结果
        """
        with open(filename, 'rb') as f:
            return base64.b64encode(f.read())
    
    @staticmethod
    def decode(s):
        """
        获取base64 解码结果

        :param:
            * (string) filename 需要进行 base64编码 文件路径
        :return:
            * (bytes) base64 解码结果
        """
        return base64.b64decode(s)


# v1.0.14 edit by Hu Jun, #51
# v1.1.1 edit by Hu Jun, #115
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
    random_source = ''
    random_source += string.ascii_letters if letters else ''
    random_source += string.digits if digits else ''
    random_source += string.punctuation if punctuation else ''

    # 避免出现 ValueError: Sample larger than population or is negative
    if length > len(random_source):
        random_source *= (length//len(random_source) + 1)

    random_str = ''.join(random.sample(random_source, length))
    return random_str


# v1.0.15 edit by Hu Jun, #77 #63
def remove_duplicate_elements(items, key=None):
    """
    去除序列中的重复元素，使得剩下的元素仍然保持顺序不变，对于不可哈希的对象，需要指定key，说明去重元素

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


# v1.0.15 edit by Hu Jun, #64
def sorted_objs_by_attr(objs, key, reverse=False):
    """
    对原生不支持比较操作的对象根据属性排序

    :param:
        * objs: (list) 需要排序的对象列表
        * key: (string) 需要进行排序的对象属性
        * reverse: (bool) 排序结果是否进行反转，默认为False，不进行反转

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
    从url中获取query参数字典

    :param:
        * url: (string) 需要获取参数字典的url

    :return:
        * query_dict: (dict) query参数的有序字典，字典的值为query值组成的列表

    举例如下::

        print('--- get_query_param_from_url demo---')
        url = 'http://localhost:8811/mytest?page_number=1&page_size=10&start_time=20180515&end_time=20180712'
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


# v1.1.0 edit by Hu Jun, #74
def get_group_list_data(data_list, group_number=1, group_size=10):
    """
    获取分组列表数据

    :param:
        * data_list: (list) 需要获取分组的数据列表
        * group_number: (int) 分组信息，默认为1
        * group_size: (int) 分组大小，默认为10

    :return:
        * group_data: (list) 分组数据

    举例如下::

        print('--- get_group_list_data demo---')
        all_records = [1, 2, 3, 4, 5]
        print(get_group_list_data(all_records))
        
        all_records1 = list(range(100))
        print(get_group_list_data(all_records1, group_number=5, group_size=15))
        print(get_group_list_data(all_records1, group_number=7, group_size=15))
        print('---')

    执行结果::

        --- get_group_list_data demo---
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


# v1.1.1 edit by Hu Jun, #114
def transform_hump_to_underline(param_dict):
    """
    将驼峰命名的参数字典键转换为下划线参数

    :param:
        * param_dict(dict): 请求参数字典

    :return:
        * temp_dict(dict): 转换后的参数字典

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
