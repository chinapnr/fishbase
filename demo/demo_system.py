# fishbase.system demo
# 2018.5.26 created by David Yi
# for Python 3.x

from fishbase.fish_system import *


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


if __name__ == '__main__':
    print('current os:', get_platform())
    demo_common_config()


