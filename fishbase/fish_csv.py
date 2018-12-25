# coding=utf-8
import csv
from io import open


# 将指定的 csv 文件转换为 list 返回
# 输入：
# csv_filename: csv 文件的长文件名
# deli: csv 文件分隔符，默认为逗号
# del_blank_row: 是否要删除空行，默认为删除
# 输出：转换后的 list
# ---
# 2018.2.1 edit by David Yi, #11002
# 2018.2.6 edit by David Yi, #11009， 增加过滤空行功能
# v1.0.16 edit by Hu Jun #94
# v1.1.4 edit by Hu Jun #126
def csv2list(csv_filename, deli=',', del_blank_row=True, encoding=None):

    """
    将指定的 csv 文件转换为 list 返回；

    :param:
        * csv_filename: (string) csv 文件的长文件名
        * deli: (string) csv 文件分隔符，默认为逗号
        * del_blank_row: (string) 是否要删除空行，默认为删除
        * encode: (string) 文件编码
    :return:
        * csv_list: (list) 转换后的 list

    举例如下::

        from fishbase.fish_file import *
        from fishbase.fish_csv import *

        def test_csv():
            csv_filename = get_abs_filename_with_sub_path('csv', 'test_csv.csv')[1]
            print(csv_filename)
            csv_list = csv2list(csv_filename)
            print(csv_list)


        if __name__ == '__main__':
            test_csv()

    """
    with open(csv_filename, encoding=encoding) as csv_file:
        csv_list = list(csv.reader(csv_file, delimiter=deli))

    # 如果设置为要删除空行
    if del_blank_row:
        csv_list = [s for s in csv_list if len(s) != 0]

    return csv_list


# v1.1.4 edit by Hu Jun #126 rename csv_file_to_list to csv2list
csv_file_to_list = csv2list


# v1.1.4 edit by Hu Jun #126
def list2csv(data_list, csv_filename='./list2csv.csv'):

    """
    将字典写入到指定的 csv 文件，并返回文件的长文件名；

    :param:
        * data_list: (list) 需要写入 csv 的数据字典
        * csv_filename: (string) csv 文件的长文件名
    :return:
        * csv_filename: (string) csv 文件的长文件名

    举例如下::

        from fishbase.fish_csv import *

        def test_list2csv():
            data_list = ['a', 'b', 'c']
            csv_file = list2csv(data_list)
            print(csv_file)


        if __name__ == '__main__':
            test_list2csv()

    """
    with open(csv_filename, "w") as csv_file:
        csv_writer = csv.writer(csv_file)
        for data in data_list:
            csv_writer.writerow(data)
    return csv_filename


# v1.1.4 edit by Hu Jun #126
def csv2dict(csv_filename, deli=',', encoding=None, key_is_header=False):

    """
    将指定的 csv 文件转换为 list 返回；

    :param:
        * csv_filename: (string) csv 文件的长文件名
        * deli: (string) csv 文件分隔符，默认为逗号
        * del_blank_row: (string) 是否要删除空行，默认为删除
        * encode: (string) 文件编码
    :return:
        * csv_data: (dict) 读取后的数据

    举例如下::

        from fishbase.fish_file import *
        from fishbase.fish_csv import *

        def test_csv2dict():
            csv_filename = get_abs_filename_with_sub_path('csv', 'test_csv.csv')[1]
            print(csv_filename)
            csv_dict = csv2dict(csv_filename)
            print(csv_dict)


        if __name__ == '__main__':
            test_csv2dict()

    """
    with open(csv_filename, encoding=encoding) as csv_file:
        if key_is_header:
            reader = csv.reader(csv_file, delimiter=deli)
            # 读取字典 key
            fieldnames = next(reader)
            reader = csv.DictReader(csv_file, fieldnames=fieldnames, delimiter=deli)
            return [dict(row) for row in reader]
        reader = csv.reader(csv_file, delimiter=deli)
        return {row[0]: row[1] for row in reader if row}


# v1.1.4 edit by Hu Jun #126
def dict2csv(data_dict, csv_filename='./dict2csv.csv', key_is_header=False):

    """
    将字典写入到指定的 csv 文件，并返回文件的长文件名；

    :param:
        * data_dict: (dict) 需要写入 csv 的数据字典
        * csv_filename: (string) csv 文件的长文件名
        * key_is_header: (bool) csv 文件第一行是否全为字典 key
    :return:
        * csv_filename: (string) csv 文件的长文件名

    举例如下::

        from fishbase.fish_csv import *

        def test_dict2csv():
            data_dict = {'a': 1, 'b': 2}
            csv_file = dict2csv(data_dict)
            print(csv_file)


        if __name__ == '__main__':
            test_dict2csv()

    """
    with open(csv_filename, "w") as csv_file:
        csv_writer = csv.writer(csv_file)
        if key_is_header:
            if isinstance(data_dict, dict):
                csv_writer.writerow(list(data_dict.keys()))
                csv_writer.writerow(list(data_dict.values()))
            elif isinstance(data_dict, list) and all([isinstance(item, dict) for
                                                      item in data_dict]):
                for item in data_dict:
                    csv_writer.writerow(list(item.keys()))
                    csv_writer.writerow(list(item.values()))
            else:
                raise ValueError('data_dict should be a dict or list which member is dict, '
                                 'but we got {}'.format(data_dict))
        else:
            csv_writer.writerows(data_dict.items())
    return csv_filename
