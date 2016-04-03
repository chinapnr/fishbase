# 2015.6.6 create by david.yi
# add function get_md5()
# 2015.6.7 add def input_field(info, field_default) 提示用户输入指定解释信息的字段名称
# 2015.6.14 r2 项目开始使用 fpytools
#   增加 对象序列化函数 serialize_instance
# 2015.8.1 加入 auto_add_file_ext() ablist_minus() format_list_on_head()
# 2016.2.22 修改名称为 fish_base.py, 继续作为 e2at 项目的底层支持
# 2016.4.1 edit fish_base directory to common
# 2016.4.3 edit begin update to version v1.0.5


from .fish_common import *

fish_base_ver = '1.0.5'


# 返回fish_base 版本号,
# 2016.2.22 create by david.yi, e2at v1.0.0 #10006
def get_fish_base_ver():
    return fish_base_ver


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

# for test on local machine
# 1 setup sdist
# 2 pip install fish_base-1.0.4.tar.gz
# 3 run /tests/code
# for upload to pypi: python setup.py sdist upload
