# fish_base.common demo
# 2017.3.15 create by Leo
# 2018.2.11 edit by David Yi

from fish_base.fish_common import *
from fish_base.fish_file import get_abs_filename_with_sub_path


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
    print('file md5:', GetMD5.file(get_abs_filename_with_sub_path('test_conf', 'test_conf.ini')[1]))
    print('big file md5:', GetMD5.big_file(get_abs_filename_with_sub_path('test_conf', 'test_conf.ini')[1]))
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


if __name__ == '__main__':

    # 检查当前系统名称
    result = check_platform()
    print(result)

    # 定义需要序列化的对象
    class Foo(object):
        a = 1
        
        def test(self):
            pass

    # 序列化对象
    result = serialize_instance(Foo)
    print(result)

    # 获得带时间戳的流水号
    result = get_time_uuid()
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