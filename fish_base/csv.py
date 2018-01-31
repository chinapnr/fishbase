import csv


# 读取配置文件
def csv_reader(file_path, delimiter=','):

    with open(file_path) as csv_file:
        read = csv.reader(csv_file, delimiter=delimiter)
        row = []
        for line in read:
            if line:
                try:
                    if line[0][0] != '#':
                        row.append(line)
                except IndexError:
                    row.append(line)
            else:
                break  
    return row
