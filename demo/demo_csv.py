from fish_base.fish_file import *
from fish_base.fish_csv import *


# csv 相关 demo
# 2018.2.1 create by David Yi
def test_csv():
    csv_filename = get_abs_filename_with_sub_path('csv', 'test_csv.csv')[1]
    print(csv_filename)
    csv_list = csv_file_to_list(csv_filename)
    print(csv_list)


if __name__ == '__main__':
    test_csv()
