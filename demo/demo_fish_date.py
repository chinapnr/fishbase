# demo_date 单元测试
# 2017.3.15 create by Leo

from fish_base.fish_date import *

if __name__ == '__main__':

    # 得到上个月的第一天和最后一天
    result = get_date_range('last month')
    print(result)

    # 得到这个月的第一天和最后一天
    result = get_date_range('this month')
    print(result)
