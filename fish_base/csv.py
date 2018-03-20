import csv


# 将 指定的 csv 文件转换为 list 返回
# 输入：
# csv_filename: csv 文件的长文件名
# deli: csv 文件分隔符，默认为逗号
# del_blank_row: 是否要删除空行，默认为删除
# 输出：转换后的 list
# ---
# 2018.2.1 edit by David Yi, #11002
# 2018.2.6 edit by David Yi, #11009， 增加过滤空行功能
def csv_file_to_list(csv_filename, deli=',', del_blank_row=True):

    with open(csv_filename) as csv_file:
        csv_list = list(csv.reader(csv_file, delimiter=deli))

    # 如果设置为要删除空行
    if del_blank_row:
        csv_list = [s for s in csv_list if len(s) != 0]

    return csv_list
