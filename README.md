# fish_base

It's my first python package, and mostly for test. 

pre-alpha version v1.0.x

Thanks!

这是我在学习 python 过程中积累的一个函数库, 希望对 python 的初学者等有所帮助. 代码写得很一般, 我会继续努力.
 python 是一门很棒的编程语言, 还有很多东西要学习.

类和函数列表, functions list:

## class FishCache

### get_cf_cache(self, cf, section, key)

读取 conf 文件类型(ini 文件类型)的缓存功能,不需要每次从文件中读取,第二次访问从内存字典中读取,以提高速度

举例1:

```python

def cf_cache_demo():

    # 申明配置文件
    cf = configparser.ConfigParser()
    
    # 读入测试用的 conf 文件
    cf.read('test_conf.ini')
    
    # 申明 conf 文件使用的 cache
    test_cache = FishCache()
    
    # 从 conf 获得参数 args 的设置
    temp_s = test_cache.get_cf_cache(cf, 'get_args', 'args')
    print(temp_s)
``` 

举例2:

我们通过循环 10 万次, 来比较一下读取速度, 第一种是通过 fish_cf_cache 缓存模式, 第二种是通过标准的方式, 
我们可以看到速度相差了 15 倍左右, 因此适用于对于配置文件有大量读取的场景.

```bash
 cost time: 0.05010986328125 use fish_cf_cache 
 cost time: 0.8643078804016113 use common conf way
```

```python
 # way 1, use fish_cf_cache
 start_time = time.time()

 for i in range(100000):
     temp_s = test_cache.get_cf_cache(cf, 'get_args', 'args')

 end_time = time.time()

 print('cost time:', end_time - start_time, 'use fish_cf_cache ')

 # way 2, use common conf way
 start_time = time.time()

 for i in range(100000):
     temp_s = cf['get_args']['args']

 end_time = time.time()

 print('cost time:', end_time - start_time, 'use common conf way')

 print(temp_s)
```

### get_long_filename_with_sub_dir(sub_dir, filename)

输入: 子路径名称, 子路径下的文件名称
输出: 标志(目前总是为 True), 完整的长文件名

生成当前路径下一级路径某文件的完整文件名

类似下面的结构:

\aaa.py
\bbb\ccc.conf

在 aaa.py 中使用

get_long_filename_with_sub_dir('bbb', 'ccc.conf')

会得到 C:....\bbb\ccc.conf


get_md5(s)

serialize_instance(obj)

auto_add_file_ext(short_filename, ext)

check_kind_path_file(kind_name, file_name)

I will add more notes and optimized the code in the future.

