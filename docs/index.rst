.. fish_base documentation master file, created by
   sphinx-quickstart on Wed Apr 18 15:20:36 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. image:: https://travis-ci.org/chinapnr/fishbase.svg?branch=master
    :target: https://travis-ci.org/chinapnr/fishbase
.. image:: https://coveralls.io/repos/github/chinapnr/fishbase/badge.svg?branch=master
    :target: https://coveralls.io/github/chinapnr/fishbase?branch=master
.. image:: https://readthedocs.org/projects/fishbase/badge/?version=latest
    :target: https://fishbase.readthedocs.io/en/latest/?badge=latest

简介
====

fishbase 是由我们自主开发、整理的一套 Python 基础函数库。

从多年的 Python 开发经验中，我们抽象出了很多通用的方法，为日常的开发工作带来极大的便利。

fishbase 设计的初衷，并不是用来解决复杂问题，而是对系统函数进一步封装，从而减少程序开发工作量、降低引用复杂度。

目前，我们正在加速 fishbase 的完善，涵盖单元测试、示例代码、文档等内容优化。希望借此帮助到更多 Python 爱好者和应用开发人员。

安装
====

Install and update using `pip`_:

.. code-block:: text

    pip install -U fishbase

模块
====

目前主要分为以下模块：

-  fish_common 基本函数包

-  fish_system 系统增强函数包

-  fish_file 文件处理增强函数包

-  fish_csv csv 处理增强函数包

-  fish_logger 日志记录增强函数包

-  fish_project project 目录结构生成函数包

使用示例
========

.. code-block:: python

    from fishbase.fish_common import *

    # 获取当前路径下的 py 文件
    print(find_files(".", [".py"]))

    # 获取字符串 "hello world" 的 MD5 值
    print(GetMD5.string('hello world'))

    # 获取长度为 10 的随机字符串
    print(get_random_str(10))


.. code-block:: python

    from fishbase.fish_data import *

    # 验证身份证号是否合法
    print(is_valid_id_number("320124198701010012"))


.. toctree::
   :maxdepth: 1

   change_log


API 函数列表
-----------------------------

可以到以下单元中查找具体的函数列表和使用说明。

.. toctree::
   :maxdepth: 2

   fish_common
   fish_csv
   fish_data
   fish_date
   fish_file
   fish_logger
   fish_project
   fish_system




.. _pip: https://pip.pypa.io/en/stable/quickstart/