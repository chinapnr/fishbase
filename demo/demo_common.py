# fish_base.common demo
# 2017.3.15 create by Leo
# 2018.2.11 edit by David Yi

from fishbase.fish_common import *
from fishbase.fish_file import get_abs_filename_with_sub_path


# 2018.2.12 common 中 config 文件处理相关，#11013
def demo_common_config():
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


# 2018.5.19
def demo_singleton():
    print('--- class singleton demo ---')
    t1 = SingleTon()
    t1.x = 2
    print('t1.x:', t1.x)

    t2 = SingleTon()

    t1.x += 1

    print('t1.x:', t1.x)
    print('t2.x:', t2.x)
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

    # 定义需要序列化的对象
    class Foo(object):
        a = 1
        b = [1, 2, 3]
        c = {'a': 1, 'b': 2}

        def test(self):
            print('hello')

    # 序列化对象
    result = serialize_instance(Foo)
    print(result)

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

    demo_common_config()

    demo_common_md5()

    demo_json_contain()

    dic1 = {'key1': 'value1', 'key2': 'value2'}
    print(splice_url_params(dic1))

    demo_singleton()

    demo_uuid()

    demo_dict()
