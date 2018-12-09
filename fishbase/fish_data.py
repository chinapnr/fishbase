# coding=utf-8
"""

``fish_data`` 包含的是一些与数据信息相关的函数，比如银行卡、身份证信息的生成和校验。

在我们进行一些开发测试、功能测试、自动化测试、压力测试等场景下，都需要模拟身份证、银行卡等信息。
fish_data 中的函数就是用在这样的场景。注意，这些函数不会生成真实的身份证和银行卡号。


"""

# 2018.12.9 v1.1.3 created

import re


# 检查身份证号码是否能通过校验规则
# ---
# 2018.12.9 create by David Yi, add in v1.1.3, github issue #137
# original source: https://zhuanlan.zhihu.com/p/24449773
def is_valid_id_number(id_number):
    """
        生成当前路径下一级路径某文件的完整文件名；

        :param:
            * id_number: (string) 身份证号，比如 32012419870101001
        :returns:
            * 返回类型 (tuple)，当前有一个值，第一个为 flag，以后第二个值会返回具体校验不通过的详细错误
            * flag: (bool) 如果身份证号码校验通过，返回 True；如果身份证校验不通过，返回 False

        举例如下::

            from fishbase.fish_data import *

            print('--- fish_data is_valid_id_number demo ---')

            # id number false
            id1 = '320124198701010012'
            print(id1, is_valid_id_number(id1)[0])

            # id number true
            id2 = '130522198407316471'
            print(id2, is_valid_id_number(id2)[0])

            print('---')

        输出结果::

            --- fish_data is_valid_id_number demo ---
            320124198701010012 False
            130522198407316471 True
            ---

    """

    id_regex = '[1-9][0-9]{14}([0-9]{2}[0-9X])?'

    if isinstance(id_number, int):
        id_number = str(id_number)

    if not re.match(id_regex, id_number):
        return False

    items = [int(item) for item in id_number[:-1]]

    # 加权因子表
    factors = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)

    # 计算17位数字各位数字与对应的加权因子的乘积
    copulas = sum([a * b for a, b in zip(factors, items)])

    # 校验码表
    check_codes = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')

    check = check_codes[copulas % 11].upper() == id_number[-1].upper()

    return check,
