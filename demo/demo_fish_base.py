# 2016.4.3 add demo code for conf cache

import fish_base
from fish_base import FishCache

import configparser


# 2016.4.3 create cf cache demo
def cf_cache_demo():

    # 申明配置文件
    cf = configparser.ConfigParser()

    # 读入测试用的 conf 文件
    cf.read('test_conf.ini')

    # 申明 conf 文件使用的 cache
    test_cache = FishCache()

    # 从 conf 获得参数 args 的设置
    temp_s = test_cache.get_cf_cache(cf, 'get_args', 'args')
    print(temp_s)

# main
if __name__ == '__main__':

    print(fish_base.get_md5('Hello World'))

    cf_cache_demo()
