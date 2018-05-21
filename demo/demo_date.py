# demo_date 单元测试
# 2017.3.15 create by Leo

from fishbase.fish_date import *


# 2016.4.26
def month_range_demo():

    temple_tuple = get_date_range('last month')
    print(temple_tuple[0])
    print(temple_tuple[1])

    temple_tuple = get_date_range('this month')
    print(temple_tuple[0])
    print(temple_tuple[1])


if __name__ == '__main__':

    # 得到上个月的第一天和最后一天
    result = get_date_range('last month')
    print(result)

    # 得到这个月的第一天和最后一天
    result = get_date_range('this month')
    print(result)
