# 2016.4.1 create fish_common.py by david.yi


import os


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


# 判断文件名是否没有输入后缀，加上后缀
# create 2015.8.1. by david.yi
def auto_add_file_ext(short_filename, ext):

    temp_filename = short_filename
    if os.path.splitext(temp_filename)[1] == '':
        temp_filename += ext

    return temp_filename


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
