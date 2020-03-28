# fish_base.common demo
# 2017.3.15 create by Leo
# 2018.2.11 edit by David Yi

from fishbase.fish_common import *
from fishbase.fish_file import get_abs_filename_with_sub_path


# 2018.5.10
def demo_common_md5():
    print('--- md5 demo ---')
    print('string md5:', GetMD5.string('hello world!'))
    print('file md5:', GetMD5.file(get_abs_filename_with_sub_path('conf', 'test_conf.ini')[1]))
    print('big file md5:', GetMD5.big_file(get_abs_filename_with_sub_path('conf', 'test_conf.ini')[1]))
    print('---')


# 2018.5.15
def demo_json_contain():
    print('--- json contain demo ---')
    json1 = {"id": "0001"}
    json2 = {"id": "0001", "value": "File"}
    print(if_json_contain(json1, json2))
    print('---')


# 2018.5.26
def demo_uuid():
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


# 2018.5.30
def demo_dict():
    print('--- sorted_list_from_dict() demo ---')
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


if __name__ == '__main__':

    # 定义需要判断的列表
    # 合法列表
    test_legitimate_list = ['Hello World', 1]
    # 非法列表
    test_illegal_list = ['Hello World', None]

    # 判断列表是否有非法参数
    result = if_any_elements_is_space(test_legitimate_list)
    print(result)
    result = if_any_elements_is_space(test_illegal_list)
    print(result)

    demo_common_md5()

    demo_json_contain()

    dic1 = {'key1': 'value1', 'key2': 'value2'}
    print(splice_url_params(dic1))

    demo_uuid()

    demo_dict()
