# 2016.4.3 add demo code for conf cache
# 2016.10.4 add demo code for fish_common check_sub_path_create()
# 2017.2.21 test functions need update in the days

from fish_base import *

import configparser
import time


# 2016.4.3 create cf cache demo
def cf_cache_demo():

    # 申明配置文件
    cf = configparser.ConfigParser()

    # 读入测试用的 conf 文件
    cf.read('test_conf.ini')

    # 申明 conf 文件使用的 cache
    test_cache = FishCache()

    # 从 conf 获得参数 args 的设置

    # way 1, use fish_cf_cache
    start_time = time.time()

    # 记录读取的键值
    temp_s = ''

    for i in range(100000):
        temp_s = test_cache.get_cf_cache(cf, 'get_args', 'args')

    end_time = time.time()

    print('cost time:', end_time - start_time, 'use fish_cf_cache ')

    # way 2, use common conf way
    start_time = time.time()

    for i in range(100000):
        temp_s = cf['get_args']['args']

    end_time = time.time()

    print('cost time:', end_time - start_time, 'use common conf way')

    print(temp_s)


# main
if __name__ == '__main__':

    print(get_md5('Hello World'))

    # cf_cache_demo()

    # fish_base get_abs_filename_with_sub_path() demo
    print(get_abs_filename_with_sub_path('test_sub_dir', 'test_file.txt'))

    # fish_base check_sub_path_create() demo
    print(check_sub_path_create('auto_create'))



