# demo fish_file
# 2017.3.11 create by Leo
# 2018.5 edit by David Yi

from fishbase.fish_file import *


# 2018.1.31 测试 get_abs_filename_with_sub_path()
# 2018.5.26 edit, #19040
def demo_get_abs_filename_with_sub_path():

    print('demo get_abs_filename_with_sub_path')
    # define sub dir
    path_name = 'sub_dir'
    # define not exists file
    filename = 'test_file.txt'

    abs_filename = get_abs_filename_with_sub_path(path_name, filename)
    # return False and abs filename
    print(abs_filename)

    # define exists file
    filename = 'demo.txt'
    abs_filename = get_abs_filename_with_sub_path(path_name, filename)
    # return True and abs filename
    print(abs_filename)

    print('---')


if __name__ == '__main__':

    demo_get_abs_filename_with_sub_path()

    print('demo check_sub_path_create() ')
    # 定义子路径名称
    sub_path = 'demo_sub_dir'
    # 检查当前路径下的一个子路径是否存在，不存在则创建
    print('check sub path:', sub_path)
    result = check_sub_path_create(sub_path)
    print(result)
    print('---')

    print('demo check_ext_add()')

