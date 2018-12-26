# coding=utf-8
"""

``fish_random`` 包含的是一些生成随机值的函数。

"""

# 2018.12.26 v1.1.5 created
import random
from fishbase.fish_common import get_random_str


# v1.0.15 edit by Hu Jun #163
def gen_string_by_range(min_length, max_length, prefix=None, suffix=None):
    """
    指定一个前后缀以及字符串长度，返回随机生成带有前后缀及指定长度的字符串

    :param:
        * min_length: (int) 字符串最小长度
        * max_length: (int) 字符串最小长度
        * prefix: (string) 字符串前缀
        * suffix: (string) 字符串后缀

    :return:
        * random_str: (string) 指定长度、前后缀的随机字符串
    
    举例如下::

        print('--- gen_string_by_range demo ---')
        print(gen_string_by_range(5, 7))
        print(gen_string_by_range(5, 7, prefix='FISHBASE_'))
        print(gen_string_by_range(5, 7, prefix='FISHBASE_', suffix='.py'))
        print('---')

    执行结果::

        --- gen_string_by_range demo ---
        q4uo6E8
        FISHBASE_8uCBEUH
        FISHBASE_D4wRX2.py
        ---
    """
    if not all([isinstance(min_length, int), isinstance(max_length, int)]):
        raise ValueError('min_length and max_length should be int, but we got {} and {}'.
                         format(type(min_length), type(max_length)))

    if min_length > max_length:
        raise ValueError('min_length should less than or equal to max_length')

    random_str_len = random.randint(min_length, max_length)
    init_rand_str = get_random_str(random_str_len, digits=True)
    prefix = prefix if prefix else ''
    suffix = suffix if suffix else ''

    random_str = ''.join([prefix, init_rand_str, suffix])

    return random_str
