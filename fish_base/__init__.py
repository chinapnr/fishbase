# 2015.6.6 create by david.yi
# add function get_md5()
# 2015.6.7 add def input_field(info, field_default) 提示用户输入指定解释信息的字段名称
# 2015.6.14 r2 项目开始使用 fpytools
#   增加 对象序列化函数 serialize_instance
# 2015.8.1 加入 auto_add_file_ext() ablist_minus() format_list_on_head()
# 2016.2.22 修改名称为 fish_base.py, 继续作为 e2at 项目的底层支持

import os


fish_base_ver = '1.0.3'


# 返回fish_base 版本号,
# 2016.2.22 create by david.yi, e2at v1.0.0 #10006
def get_fish_base_ver():
    return fish_base_ver


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


# 提示用户输入指定解释信息的字段名称
# 2015.6.7  create by david.yi
# 输入: info: 要显示的字段解释，field_default：默认的字段名称
# 输出: 字段名称
def input_field(info, field_default):
    field = input('Please input the ' + info +
                  ' field name (return for use default ' +
                  field_default + '): ')

    if len(field) <= 0:
        field = field_default

    print('The ' + info + ' field: ' + field + '\n')

    return field


# 对象序列化
# 2015.6.14  edit by david.yi
# 输入: info: 要显示的字段解释，field_default：默认的字段名称
# 输出: 字段名称
def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d


# 判断文件名是否没有输入后缀，加上后缀
# create 2015.8.1. by david.yi
def auto_add_file_ext(short_filename, ext):

    temp_filename = short_filename
    if os.path.splitext(temp_filename)[1] == '':
        temp_filename += ext

    return temp_filename


# 列表A-B计算， A: 1 2 3 4 5 B: 1 2 7 结果为 1 2
# create 2015.8.1 by david.yi
def ablist_minus(list_a, list_b):
    list_temp = []
    for i in range(len(list_a)):
        for j in range(len(list_b)):
            if list_a[i] == list_b[j]:
                list_temp.append(list_a[i])

    return list_temp


# 将列表按照列标头进行筛选
# create 2015.8.1. by david.yi
def format_list_on_head(list_source, list_head):
    # 整理 list 数据
    l1 = []  # 单行数据
    l2 = []  # 整体数据

    # 整理要输出的具体list内容
    for i in range(len(list_source)):
        for j in range(len(list_head)):
            l1.append(list_source[i][list_head[j]])
        l2.append(l1)
        l1 = []

    return l2


# r2c1 v1.0.1 #12089
# 通过conf文件。eg ini，读取值，通过字典缓存来提高读取速度
class FpyCache:
    __cache = {}

    def get_cache(self, cf, section, key):
        # 生成 key，用于 dict
        temp_key = section + '_' + key

        if not (temp_key in self.__cache):
            self.__cache[temp_key] = cf[section][key]

        return self.__cache[temp_key]


# 检查指定类型的文件名是否在指定的路径下, 主要用户检查 conf 路径下的配置文件等
# 2016.2.22 create by david.yi , e2at v1.0.0 #10005
def check_kind_path_file(kind_name, file_name):

    # 文件路径
    kind_path = os.path.join(os.path.abspath(''), kind_name)

    # 完整文件名，包含路径
    long_filename = os.path.join(kind_path, file_name)

    # 文件如果不存在，返回错误信息
    if not os.path.isfile(long_filename):
        return False
    else:
        return True, long_filename
