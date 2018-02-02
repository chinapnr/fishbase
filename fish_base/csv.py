import csv


# 读取csv 文件，返回列表
# 输入：
# csv_filename: csv 文件的长文件名  deli: csv 文件分隔符
# 输出：
# 转换后的 list
# ---
# 2018.2.1. edit by David Yi, #11002
def csv_file_to_list(csv_filename, deli=','):

    with open(csv_filename) as csv_file:
        csv_list = list(csv.reader(csv_file, delimiter=deli))

    return csv_list
