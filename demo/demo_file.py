# demo_file 单元测试
# 2017.3.11 create by Leo

from fishbase.fish_file import *


# 2018.1.31 测试 get_abs_filename_with_sub_path()
def test_get_abs_filename_with_sub_path():

    print('get_abs_filename_with_sub_path')
    # 定义子路径名称
    path_name = 'test_sub_dir'
    # 定义文件名称
    filename = 'test_file.txt'
    # 生成当前路径下一级文件的完整路径名
    abs_filename = get_abs_filename_with_sub_path(path_name, filename)
    print(abs_filename)
    print('---')


if __name__ == '__main__':

    test_get_abs_filename_with_sub_path()

    print('test get_abs_filename_with_sub_path_module() ')
    # 定义子路径名称
    sub_path = 'test_sub_dir'
    # 定义存在的文件名称
    filename_existent = 'demo_file.txt'
    # 定义不存在的文件名称
    filename_non_existent = 'demo.txt'
    # 生成下一级路径文件的完整文件名
    result = get_abs_filename_with_sub_path_module(sub_path, filename_existent)
    print(result)
    result = get_abs_filename_with_sub_path_module(sub_path, filename_non_existent)
    print(result)
    print('---')

    print('test check_kind_path_file() ')
    # 定义路径（类型）
    kind_name = 'test_conf'
    # 定义文件名
    conf_filename = 'test_conf.ini'
    # 检查指定路径（类型）的文件名是否在指定的路径下
    result = check_kind_path_file(kind_name, conf_filename)
    print(result)
    print('---')

    print('test check_sub_path_create() ')
    # 定义存在子路径名
    sub_path = 'test_sub_dir'
    # 检查当前路径下的一个子路径是否存在，不存在则创建
    result = check_sub_path_create(sub_path)
    print('check sub path:', sub_path)
    print(result)
    print('---')
