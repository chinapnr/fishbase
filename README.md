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

### common 模块

#### def conf_as_dict(conf_filename)

功能：读入配置文件，返回根据配置文件内容生成的字典类型变量，减少文件读取次数

输入： conf 文件长文件名
输出： 字典变量, flag: 是否操作成功 d: config 文件内容 count: 字典 key 的数量

代码举例：

    def demo_common_config():
        print('--- conf_as_dict demo---')
        # 定义配置文件名
        conf_filename = 'test_conf.ini'
        # 读取配置文件
    
        ds = conf_as_dict(conf_filename)
        # 显示是否成功，所有 dict 的内容，dict 的 key 数量
        print('flag:', ds[0])
        print('dict:', ds[1])
        print('length:', ds[2])
    
        d = ds[1]
    
        # 显示一个 section 下的所有内容
        print('section show_opt:', d['show_opt'])
        # 显示一个 section 下面的 key 的 value 内容
        print('section show_opt, key short_opt:', d['show_opt']['short_opt'])
    
        # 读取一个复杂的section，先读出 key 中的 count 内容，再遍历每个 key 的 value
        i = int(d['get_extra_rules']['erule_count'])
        print('section get_extra_rules, key erule_count:', i)
        for j in range(i):
            print('section get_extra_rules, key erule_type:', d['get_extra_rules']['erule_'+str(j)])
        print('---')

### logger 模块

#### def set_log_file(local_file=None)

功能：设置日志记录，按照每天一个文件，记录包括 info 以及以上级别的内容

输入： local_file 日志文件名

代码举例：

    from fish_base.logger import *
    from fish_base.file import *
    
    log_abs_filename = get_abs_filename_with_sub_path('log', 'fish_test.log')[1]
    
    set_log_file(log_abs_filename)
    
    logger.info('test fish base log')
    logger.warn('test fish base log')
    logger.error('test fish base log')
    
    print('log ok')