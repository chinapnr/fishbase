## fish_base 简介

这是我们在学习 python 过程中积累的一个函数库，主要用于自己学习，希望对 python 的初学者等有所帮助。代码写得很一般，在不断积累和学习中。

---

## 类和函数列表:

### fish_common 常用小函数

### fish_file 路径文件处理增强

#### get_long_filename_with_sub_dir(sub_dir， filename)

功能：生成当前路径下一级路径某文件的完整文件名<br>

输入：子路径名称， 子路径下的文件名称<br>
输出：标志(目前总是为 True)， 完整的长文件名

    类似下面的结构:

    \aaa.py
    \bbb\ccc.conf

在 aaa.py 中使用 `get_long_filename_with_sub_dir('bbb'， 'ccc.conf')` 可以得到 ccc.conf 这个文件完整的带路径的文件名： C:....\bbb\ccc.conf

### fish_date 常用日期函数


