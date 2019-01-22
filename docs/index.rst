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
.. image:: https://ci.appveyor.com/api/projects/status/ecskod12wy8fvkxu?svg=true
    :target: https://ci.appveyor.com/project/itaa/fishbase


fishbase 是什么？
=================

fishbase 是由我们自主开发、整理的一套 Python 基础函数库。

从多年的 Python 开发经验中，我们抽象出了很多通用的方法，为日常的开发工作带来极大的便利。

fishbase 设计的初衷，并不是用来解决复杂问题，而是对系统函数进一步封装，从而减少程序开发工作量、降低引用复杂度。

目前，我们正在加速 fishbase 的完善，涵盖单元测试、示例代码、文档等内容优化。希望借此帮助到更多 Python 爱好者和应用开发人员。


模块
========

目前主要分为以下模块：

-  fish_common 基本函数包

-  fish_csv csv 处理增强函数包

-  fish_data 数据信息处理函数包，含银行卡、身份证等

-  fish_date 日期处理函数包

-  fish_file 文件处理增强函数包

-  fish_logger 日志记录增强函数包

-  fish_project project 目录结构生成函数包

-  fish_random 随机数据生成函数包

-  fish_system 系统增强函数包

-  fish_crypt 加密数据函数包


怎么用？
========

.. code:: shell

   # 通过 pip 进行安装或者更新
   pip install -U fishbase


fishbase 能干什么？
===================


伪造数据
----------

.. code:: python

   >>> from fishbase.fish_random import gen_random_id_card
   >>> # 随机生成一个身份证号
   >>> print(gen_random_id_card())
   ['310109198610243547']
   >>> from fishbase.fish_random import gen_random_bank_card
   >>> # 随机生成一个中国银行的信用卡卡号
   >>> print(gen_random_bank_card('中国银行', 'CC'))
   625907379******1
   >>> from fishbase.fish_random import gen_random_mobile
   >>> # 随机生成一个手机号
   >>> print(gen_random_mobile())
   188****3925


找文件
------

.. code:: python

   >>> from fishbase.fish_common import find_files
   >>> # 获取当前路径下的 mp4 文件
   >>> print(find_files(".", [".mp4"]))


创建项目结构
------------

.. code:: python

   >>> import os
   >>> from fishbase.fish_project import init_project_by_yml
   >>> package_yml = '''
   ... project: hellopackage
   ... tree:
   ...     - README.md
   ...     - requirements.txt
   ...     - setup.py
   ... '''
   >>> # 通过 yml 文件创建一个项目结构
   >>> init_project_by_yml(package_yml, '.')
   >>> print(os.listdir('./hellopackage'))
   ['requirements.txt', 'README.md', 'setup.py']


获取文件的 MD5 值
----------------

.. code:: python

   >>> from fishbase.fish_crypt import FishMD5
   >>> # 获取文件的 MD5 值
   >>> print(FishMD5.file('./test_md5.txt'))
   fb7528c9778b2377e30b0f7e4c26fef0


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
   fish_random
   fish_crypt
