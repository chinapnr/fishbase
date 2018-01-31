import csv


# 读取csv 文件，返回列表
def csv_reader(file_path, delimiter=','):

    with open(file_path) as csv_file:
        csv_list = csv.reader(csv_file, delimiter=delimiter)
        row = []
        for line in csv_list:
            if line:
                try:
                    if line[0][0] != '#':
                        row.append(line)
                except IndexError:
                    row.append(line)
            else:
                break  
    return row


def csv_reader2(file_path, delimiter=','):

    with open(file_path) as csv_file:
        csv_list = list(csv.reader(csv_file, delimiter=delimiter))

    return csv_list
