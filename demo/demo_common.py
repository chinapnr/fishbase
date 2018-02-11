# fish_base.common demo
# 2017.3.15 create by Leo
# 2018.2.11 edit by David Yi

from fish_base.common import *

if __name__ == '__main__':

    # 检查当前系统名称
    result = check_platform()
    print(result)

    # 定义需要生成md5值的字符串
    s = 'Hello World!'
    # 生成md5值
    result = get_md5(s)
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

    print('--- conf_as_dict demo---')
    # 定义配置文件名
    conf_filename = 'test_conf.ini'
    # 读取配置文件
    result = conf_as_dict(conf_filename)
    print(result)
    print('---')

    # 初始化类
    FishCache_test = FishCache()
    # 从config文件读取值
    result = FishCache_test.get_cf_cache(result, 'show_opt', 'short_opt')
    print(result)
