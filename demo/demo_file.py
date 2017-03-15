# demo_file 单元测试
# 2017.3.11 create by Leo

from fish_base.fish_file import *

if __name__ == '__main__':

    # 生成当前路径下一级路径某文件的完整文件名，正确会返回true，并返回此文件的绝对路径如...\\demo_file\\demo_file.txt
    get_abs_filename_with_sub_path_result = get_abs_filename_with_sub_path('test_sub_dir', 'demo_file.txt')
    print(get_abs_filename_with_sub_path_result)
    
    # 生成使用模块时的下一级路径某文件的完整文件名,存在，会返回true，以及此文件的绝对路径如...\\demo_file\\demo_file.txt
    get_abs_filename_with_sub_path_module_result_existent = get_abs_filename_with_sub_path_module('test_sub_dir', 'demo_file.txt')
    print(get_abs_filename_with_sub_path_module_result_existent)
    
    # 生成使用模块时的下一级路径某文件的完整文件名,不存在，会返回false，以及此文件的绝对路径如...\\demo_file\\demo_file.txt
    get_abs_filename_with_sub_path_module_result_non_existent = get_abs_filename_with_sub_path_module('test_sub_dir', 'demo.txt')
    print(get_abs_filename_with_sub_path_module_result_non_existent)

    # 判断文件名是否没有输入后缀，加上后缀，正确输出为(demo_file\\demo.txt, demo.txt)
    auto_add_file_ext_result = auto_add_file_ext('test_sub_dir\\demo', '.txt')
    print(auto_add_file_ext_result)

    # 检查指定类型的文件名是否在指定的路径下，目前kind指的是文件的子目录，存在
    check_kind_path_file_existent_result = check_kind_path_file('test_sub_dir', 'demo_file.txt')
    print(check_kind_path_file_existent_result)

    # 检查指定类型的文件名是否在指定的路径下，目前kind指的是文件的子目录，不存在
    check_kind_path_file_non_existent_result = check_kind_path_file('test', 'demo_file.txt')
    print(check_kind_path_file_non_existent_result)
    
    #检查当前路径下的某个子路径是否存在, 不存在则创建，存在，返回true
    check_sub_path_create_existent_result = check_sub_path_create('test_sub_dir')
    print(check_sub_path_create_existent_result)
    
    #检查当前路径下的某个子路径是否存在, 不存在则创建，不存在，返回false，并且创建目录，返回true表示目录创建成功
    check_sub_path_create_non_existent_result = check_sub_path_create('test')
    print(check_sub_path_create_non_existent_result)

    

