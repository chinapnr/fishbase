## fish_base 简介

这是我们在学习 python 过程中积累的一个函数库，主要用于自己学习，希望对 python 的初学者等有所帮助。

---

## 类和函数列表:

### file 模块，路径文件处理增强

#### get_abs_filename_with_sub_dir(sub_path, filename)

功能：生成当前路径下一级路径某文件的完整文件名<br>

输入：sub_path 子路径名称， filename: 子路径下的文件名称<br>
输出：元组，第一个值，如果文件存在，返回 True，文件不存在，返回 False；第二个值为完整的长文件名

    类似下面的结构:

    \aaa.py
    \bbb\ccc.conf

在 aaa.py 中使用 `get_abs_filename_with_sub_dir('bbb'， 'ccc.conf')` 可以得到 ccc.conf 这个文件完整的带路径的文件名： C:....\bbb\ccc.conf

代码举例：

    print('get_abs_filename_with_sub_path')
    # 定义子路径名称
    path_name = 'test_sub_dir'
    # 定义文件名称
    filename = 'test_file.txt'
    # 生成当前路径下一级文件的完整路径名
    abs_filename = get_abs_filename_with_sub_path(path_name, filename)
    print(abs_filename)

### csv 模块，csv 文件处理增强

#### csv_file_to_list(csv_filename, deli=',')

功能：将 指定的 csv 文件转换为 list 返回

输入：csv_filename: csv 文件的长文件名  deli: csv 文件分隔符
输出：转换后的 list

代码举例：

    from fish_base.file import *
    from fish_base.csv import *
    
    
    # csv 相关 demo
    # 2018.2.1 create by David Yi
    def test_csv():
        csv_filename = get_abs_filename_with_sub_path('csv', 'test_csv.csv')[1]
        print(csv_filename)
        csv_list = csv_file_to_list(csv_filename)
        print(csv_list)
    
    
    if __name__ == '__main__':
        test_csv()


