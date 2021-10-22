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
import functools
import pathlib

from urllib.parse import parse_qs, urlsplit, urlencode


# uuid kind const
udTime = 10001
udRandom = 10002

# order const
odASC = 10011
odDES = 10012

# character kind const
charChinese = 10021
charNum = 10022


# v1.1.6 edit by Hu Jun
def show_deprecation_warn(old_fun, suggest_fun):
    warnings.simplefilter('always')
    warnings.warn('{} is deprecated, and in 2.x it will stop working. '
                  'Use {} instead.'.format(old_fun, suggest_fun),
                  DeprecationWarning, stacklevel=2)


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
# 2019.1.5 v1.1.6 edit by Hu Jun, #152
# 2020.3.25, #256, edit by David Yi;
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
        if i == 0:
            continue
        if not (i and str(i).strip()):
            return True
    return False


# 功能：监测list或者元组是否含有特殊字符
# 输入：source 是参数列表或元组
# 输出：True：不包含特殊字符；False：包含特殊字符
# 2017.3.30 create by Leo #11001
def if_any_elements_is_special(source):
    if not re.match('^[a-zA-Z0-9_,-.|]+$', "".join(source)):
        return False
    return True


# 功能：监测list或者元组是否只包含数字
# 输入：source 是参数列表或元组
# 输出：True：只包含数字；False：不只包含数字
# 2017.3.30 create by Leo #11003
def if_any_elements_is_number(source):
    for i in source:
        if not i.isdigit():
            return False
    return True


# 功能：检查 list 或者元素是否只包含英文
# 输入：source 是参数列表或元组
# 输出：True：只包含英文；False：不只包含英文
# 2017.3.30 create by Leo #11004
# 2020.3.28 edit by David Yi, #263
def is_alpha(source):
    for i in source:
        
        if not i.isalpha():
            return False
    
    return True


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


# v1.1.0 edit by Hu Jun, #74
# v1.2, edit by David Yi; #261, 参数名称修改，帮助内容修改；
def get_paging_data(data_list, page_number=1, page_size=10):
    """
    获取分页数据，用于快速计算获得类似 web 显示多页时的下面的页码

    :param:
        * data_list: (list) 需要获取分页的数据列表
        * page_number: (int) 第几页，默认为 1
        * page_size: (int) 每页显示多少页码，默认为 10

    :return:
        * paging_data: (list)

    举例如下::

        print('--- paging demo---')
        all_records = [1, 2, 3, 4, 5]
        print(get_paging_data(all_records))

        all_records1 = list(range(100))
        print(get_paging_data(all_records1, group_number=5, group_size=15))
        print(get_paging_data(all_records1, group_number=7, group_size=15))
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
    
    if not isinstance(page_number, int) or not isinstance(page_size, int):
        raise TypeError('group_number and group_size should be int, but we got group_number: {0}, '
                        'group_size: {1}'.format(type(page_number), type(page_size)))
    if page_number < 0 or page_size < 0:
        raise ValueError('group_number and group_size should be positive int, but we got '
                         'group_number: {0}, group_size: {1}'.format(page_number, page_size))
    
    start = (page_number - 1) * page_size
    end = page_number * page_size
    
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
                d = OrderedDict(yaml.safe_load(f.read()))
                return True, d, 'Success'
        else:
            with open(file_path, 'r') as f:
                d = OrderedDict(yaml.safe_load(f.read()))
                return True, d, 'Success'
    except Exception:
        return False, {}, 'Unknown error'


# 2019.06.11 edit by Hu Jun, #235
# 2019.06.15 edit by Hu Jun, #238
class RMBConversion(object):
    """
    人民币表示格式转换，阿拉伯数字表示的人民币和中文大写相互转换；

    举例如下::

        print('--- RMBConversion demo ---')
        chinese_amount = RMBConversion.an2cn('12345.67')
        print('RMBConversion an2cn:', chinese_amount)
        print('RMBConversion cn2an:', RMBConversion.cn2an(chinese_amount))
        print('---')

    执行结果::

        --- RMBConversion demo ---
        RMBConversion an2cn: 壹万贰仟叁佰肆拾伍圆陆角柒分
        RMBConversion cn2an: 12345.67
        ---

    """
    arab_number_max_len = 19
    upper_chinese_number = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
    unit_dict = {'1': '拾',
                 '2': '佰',
                 '3': '仟'}
    # 需要倒序拼接，所以是 '亿万'
    unit_list = ['万', '亿', '亿万']

    an_2_cn_dict = {str(k): v for k, v in zip(range(10), upper_chinese_number)}
    cn_2_an_dict = dict(zip(an_2_cn_dict.values(), an_2_cn_dict.keys()))

    @staticmethod
    def an2cn(arabic_amount):
        """
        将阿拉伯数字金额转换为中文大写金额表示
        
        :param:
           * arabic_amount: (string) 阿拉伯数字金额
        :return:
           * chinese_amount: (string) 中文大写数字金额
        """
        try:
            float(arabic_amount)
            arabic_amount = str(arabic_amount)
        except ValueError as _:
            raise ValueError('error arabic_amount : {}'.format(arabic_amount))
        if len(arabic_amount) > RMBConversion.arab_number_max_len:
            raise ValueError('len of arabic_amount should less than {}'.
                             format(RMBConversion.arab_number_max_len))
        if '.' not in arabic_amount:
            arabic_amount += '.'
        integer, decimals = arabic_amount.split('.')

        if len(decimals) > 2:
            raise ValueError('decimals error')

        reverse_integer_str = ''
        # 按照长度为 4 进行划分
        divide_part = split_str_by_length(integer[::-1], 4)
        for index, unit_part in enumerate(divide_part):
            temp_part, temp_unit = '', ''
            if unit_part == '0000':
                continue
            # 添加 万、亿单位
            if index > 0:
                temp_unit = RMBConversion.unit_list[index - 1]
                temp_part += temp_unit
            for unit_index, an_char in enumerate(unit_part):
                if an_char != '0':
                    temp_part += RMBConversion.unit_dict.get(str(unit_index % 4), '')
                temp_part += RMBConversion.an_2_cn_dict.get(an_char)
    
            while temp_part.find('零零') > 0:
                temp_part = temp_part.replace('零零', '零')
            # 替换掉万、亿、亿万后面的零
            if temp_unit and temp_unit + '零' in temp_part:
                temp_part = temp_part.replace(temp_unit + '零', temp_unit)
            reverse_integer_str += temp_part

        while reverse_integer_str[0] == '零':
            reverse_integer_str = reverse_integer_str[1:]

        chinese_amount = reverse_integer_str[::-1]
        # 整数最后部分加 圆
        chinese_amount += '圆'

        if len(decimals) == 0 or decimals in ['0', '00']:
            chinese_amount += '整'
        else:
            chinese_amount += RMBConversion.an_2_cn_dict.get(decimals[0])
            if decimals[0] != '0':
                chinese_amount += '角'
            if len(decimals) > 1 and decimals[1] != '0':
                chinese_amount += RMBConversion.an_2_cn_dict.get(decimals[1])
                chinese_amount += '分'
        return chinese_amount
    
    @staticmethod
    def cn2an(chinese_amount):
        """
        将中文大写金额转换为阿拉伯数字金额表示

        :param:
           * chinese_amount: (string) 中文大写数字金额
        :return:
           * arabic_amount: (string) 阿拉伯数字金额
        """
        cn_unit = {
            '拾': 10,
            '佰': 100,
            '仟': 1000,
            '万': 10000,
            '亿': 100000000
        }
        # 先处理小数部分
        # 有三种情况：x 分，零 x 分，x 角 y 分，x 角
        if chinese_amount.endswith('分'):
            if '角' in chinese_amount:
                dime_index = chinese_amount.index('角')
                integer_amount = chinese_amount[:dime_index - 1]
                float_str = chinese_amount[dime_index - 1:]
                float_str = float_str.replace('角', '').replace('分', '')
            else:
                if chinese_amount[-3] == '零':
                    integer_amount = chinese_amount[:-3]
                    float_str = chinese_amount[-3:]
                    float_str = float_str.replace('分', '')
                else:
                    # 需要补全零  壹仟陆佰圆陆分 ==> 壹仟陆佰圆零陆分
                    integer_amount = chinese_amount[:-2]
                    float_str = chinese_amount[-2:]
                    float_str = '零' + float_str
                    float_str = float_str.replace('分', '')
        elif chinese_amount.endswith('角'):
            integer_amount = chinese_amount[:-2]
            float_str = chinese_amount[-2:]
            float_str = float_str.replace('角', '')
            float_str += '零'
        else:
            integer_amount = chinese_amount
            float_str = ''

        float_res = '.'
        for float_char in float_str:
            try:
                float_res += RMBConversion.cn_2_an_dict[float_char]
            except KeyError as _:
                raise ValueError('error chinese_amount {}'.format(chinese_amount))

        while len(float_res) != 3:
            float_res += '0'

        float_amount = float(float_res)
        integer_amount = integer_amount.replace('圆', '')
        integer_amount = integer_amount.replace('整', '')

        # 处理整数部分
        unit = 0  # current
        an_list = []  # digest
        for cn_char in reversed(integer_amount):
            if cn_char in cn_unit:
                unit = cn_unit.get(cn_char)
                # 万 和 亿需要单独处理
                if unit in [10000, 100000000]:
                    an_list.append(unit)
                    unit = 1
            else:
                try:
                    an_num = int(RMBConversion.cn_2_an_dict[cn_char])
                except KeyError as _:
                    raise ValueError('error chinese_amount {}'.format(chinese_amount))
                if unit:
                    an_num *= unit
                    unit = 0
                an_list.append(an_num)

        # 将数组组装成数字
        arabic_amount, tmp = 0, 0
        for an_item in reversed(an_list):
            if an_item in [10000, 100000000]:
                arabic_amount += tmp * an_item
                tmp = 0
            else:
                tmp += an_item
        arabic_amount += tmp
        arabic_amount += float_amount
        return arabic_amount


# 2019.06.17 edit by Hu Jun, #239
def split_str_by_length(text, length):
    """
    将字符串切分成特定长度的数组

    :param:
        * text: (string) 需要切分的字符串
        * length: (int) 切分子串长度

    :return:
        * str_list: (list) 按照长度切分的数组

    举例如下::

        print('--- split_str_by_length demo---')
        text = '1231'*4 + '12'
        str_list = split_str_by_length(text, 4)
        print(str_list)
        print('---')

    执行结果::

        --- split_str_by_length demo---
        ['1231', '1231', '1231', '1231', '12']
        ---

    """
    if not isinstance(length, int):
        raise ValueError('{} must be int'.format(length))

    str_list = re.findall('.{' + str(length) + '}', text)
    str_list.append(text[(len(str_list) * length):])
    str_list = [item for item in str_list if item]
    return str_list

# r2c1 v1.0.1 #12089
# 2016.4.3 edit class and function name
# 通过conf文件。eg ini，读取值，通过字典缓存来提高读取速度
# class FishCache:
#    __cache = {}
#
#    def get_cf_cache(self, cf, section, key):
#        # 生成 key，用于 dict
#        temp_key = section + '_' + key
#
#        if temp_key not in self.__cache:
#            self.__cache[temp_key] = cf[section][key]
#        return self.__cache[temp_key]
