
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

fishbase 是由我们自主开发、整理的一套 Python 基础函数库，每月更新 1 到 2 个版本。

自 2016/3 初次发布以来，我们坚持不断更新，先后发布了 20 余个版本，抽象出了很多通用的方法，目前主要分为以下模块：

-  fish_common 基本函数包

-  fish_csv csv 处理增强函数包

-  fish_crypt 加密/编码增强函数包

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


获取当前系统类型
-------------

.. code:: python

   >>> from fishbase.fish_system import get_platform
   >>> print('current os:', get_platform())
   current os: osx


获取文件的绝对路径
------

.. code:: python

   >>> from fishbase.fish_common import find_files
   >>> print(get_abs_filename_with_sub_path('/etc', 'hosts'))
   (True, '/etc/hosts')


根据时间戳获取时间间隔
------------------------

.. code:: python

   >>> from fishbase.fish_date import get_time_interval
   >>> print(get_time_interval(1548575829,1548476921))
   {'days': 1, 'hours': 3, 'minutes': 28, 'seconds': 28}


生成随机数据
-----------

.. code:: python

   >>> from fishbase.fish_random import gen_random_id_card
   >>> # 随机生成一个身份证号
   >>> print(gen_random_id_card())
   ['3101091986******47']
   >>> from fishbase.fish_random import gen_random_bank_card
   >>> # 随机生成一个中国银行的信用卡卡号
   >>> print(gen_random_bank_card('中国银行', 'CC'))
   625907379******1


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


更多
====

想看看我们还实现了些啥？请戳这里：http://fishbase.readthedocs.io/

如果您有好点子，希望我们帮忙实现，请戳这里：https://github.com/chinapnr/fishbase/issues
