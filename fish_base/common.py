# 2016.4.1 create fish_common.py by david.yi
# 2016.4.3 edit FishCache class, and edit get_cf_cache
# 2016.4.7 v1.0.6, v1.0.7  add get_long_filename_with_sub_dir()
# 2016.10.4 v1.0.9 add #19001 check_sub_path_create()
# 2017.1.8 v1.0.9 #19003, remove file related functions to fish_file.py
import sys
import uuid
import configparser
import re


# 单例基础类
# 2018.2.13 create by David Yi, #11015
class SingleTon(object):
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


# md5 函数
# 输入: s: str 字符串
# 输出: 经过md5计算的值
# 2015.5.27 create by david.yi
# 2015.6.6 edit, 转移到这里，作为基本工具函数
def get_md5(s):
    import hashlib

    m = hashlib.md5()
    m.update(s.encode('utf-8'))
    return m.hexdigest()


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


# 读入配置文件，返回根据配置文件内容生成的字典类型变量，减少文件读取次数
# 输入： conf 文件长文件名
# 输出： 字典变量, flag: 是否操作成功 d: config 文件内容 count: 字典 key 的数量
# 2017.2.23 create by David.Yi, #19008
# 2018.2.12 edit by David Yi, 增加返回内容，字典长度, #11014
def conf_as_dict(conf_filename):

    flag = True

    cf = configparser.ConfigParser()

    # 读入 config 文件
    try:
        cf.read(conf_filename)
    except:
        flag = False
        return flag

    d = dict(cf._sections)
    for k in d:
        d[k] = dict(cf._defaults, **d[k])
        d[k].pop('__name__', None)

    # 计算有多少 key
    count = len(d.keys())

    return flag, d, count


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
