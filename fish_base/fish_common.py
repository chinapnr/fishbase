# 2016.4.1 create fish_common.py by david.yi
# 2016.4.3 edit FishCache class, and edit get_cf_cache
# 2016.4.7 v1.0.6, v1.0.7  add get_long_filename_with_sub_dir()
# 2016.10.4 v1.0.9 add #19001 check_sub_path_create()
# 2017.1.8 v1.0.9 #19003, remove file related functions to fish_file.py
import sys


# 2017.2.13 #19006
# 通过调用os.platform来获得当前操作系统名称
def check_platform():
    if sys.platform == 'win32':
        return 'win32'
    elif sys.platform == 'darwin':
        return 'macos'
    elif sys.platform == 'linux':
        return 'linux'
    else:
        return sys.platform


# md5 函数
# 2015.5.27 create by david.yi
# 2015.6.6 edit, 转移到这里，作为基本工具函数
# 输入: s: str 字符串
# 输出: 经过md5计算的值
def get_md5(s):
    import hashlib

    m = hashlib.md5()
    m.update(s.encode('utf-8'))
    return m.hexdigest()


# 对象序列化
# 2015.6.14  edit by david.yi
# 输入: info: 要显示的字段解释，field_default：默认的字段名称
# 输出: 字段名称
def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d

#!/usr/bin/env python
# encoding: utf-8

import time
import random


# 功能：获取整个请求的响应流水号，由10位时间戳和4位随机数拼接而成
# 输入参数：无
# 输出参数：resp_id 响应流水号（string)
def get_resp_id():
    random_var = str(random.randint(1000, 9999))
    time_stamp_var = str(int(time.time()))
    resp_id = ''.join([time_stamp_var, random_var])
    return resp_id


# 功能：判断参数列表是否存在不合法的参数，如果存在None或空字符串或空格字符串，则返回True；否则返回False
# 输入参数：param是参数列表或元组
# 输出参数：True or False
def exist_param_illegal(param):
    for i in param:
        if not (i and str(i).strip()):
            return True
    return False



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
