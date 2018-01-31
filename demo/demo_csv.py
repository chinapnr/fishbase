from fish_base.file import *
from fish_base.csv import *


def test_csv():
    csv_filename = get_abs_filename_with_sub_path('csv', 'test_csv.csv')[1]
    print(csv_filename)
    csv_list = csv_reader(csv_filename)
    print(csv_list)
    csv_list = csv_reader2(csv_filename)
    print(csv_list)

if __name__ == '__main__':
    test_csv()
