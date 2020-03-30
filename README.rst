
.. image:: https://travis-ci.org/chinapnr/fishbase.svg?branch=master
    :target: https://travis-ci.org/chinapnr/fishbase
.. image:: https://coveralls.io/repos/github/chinapnr/fishbase/badge.svg?branch=master
    :target: https://coveralls.io/github/chinapnr/fishbase?branch=master
.. image:: https://readthedocs.org/projects/fishbase/badge/?version=latest
    :target: https://fishbase.readthedocs.io/en/latest/?badge=latest
.. image:: https://ci.appveyor.com/api/projects/status/ecskod12wy8fvkxu?svg=true
    :target: https://ci.appveyor.com/project/itaa/fishbase


fishbase 简介
=================

fishbase 是由我们自主开发和整理的一套 Python 基础函数库，将我们平时在开发 Python 项目时候的各类工具函数汇聚到一起，方便集中管理和使用。

fishbase 当前版本为 v1.2，支持 Python 3.5-3.8，绝大部分函数也能工作在 Python 2.7 下，但是我们不推荐使用 Python 2.7 .

自 2016/3 初次发布以来，我们坚持不断更新，先后发布了 20 余个版本。近一年来，我们逐步形成每月更新 1 到 2 个版本的频率，抽象出了很多通用的方法，主要分为以下模块：

+----------------------------------------------------------------------------------+----------------------------------------+
|       模块                                                                       | 功能函数                               |
+==================================================================================+========================================+
| `fish_common <https://fishbase.readthedocs.io/en/latest/fish_common.html>`_      | 基本函数包                             |
+----------------------------------------------------------------------------------+----------------------------------------+
| `fish_crypt <https://fishbase.readthedocs.io/en/latest/fish_crypt.html>`_        | 加密数据函数包                         |
+----------------------------------------------------------------------------------+----------------------------------------+
| `fish_csv <https://fishbase.readthedocs.io/en/latest/fish_csv.html>`_            | csv 处理增强函数包                     |
+----------------------------------------------------------------------------------+----------------------------------------+
| `fish_data <https://fishbase.readthedocs.io/en/latest/fish_data.html>`_          | 数据信息处理函数包，含银行卡、身份证等 |
+----------------------------------------------------------------------------------+----------------------------------------+
| `fish_date <https://fishbase.readthedocs.io/en/latest/fish_date.html>`_          | 日期处理增强函数包                     |
+----------------------------------------------------------------------------------+----------------------------------------+
| `fish_file <https://fishbase.readthedocs.io/en/latest/fish_file.html>`_          | 文件处理增强函数包                     |
+----------------------------------------------------------------------------------+----------------------------------------+
| `fish_logger <https://fishbase.readthedocs.io/en/latest/fish_logger.html>`_      | 日志记录增强函数包                     |
+----------------------------------------------------------------------------------+----------------------------------------+
| `fish_project <https://fishbase.readthedocs.io/en/latest/fish_project.html>`_    | project 目录结构生成函数包             |
+----------------------------------------------------------------------------------+----------------------------------------+
| `fish_random <https://fishbase.readthedocs.io/en/latest/fish_random.html>`_      | 随机数据生成函数包                     |
+----------------------------------------------------------------------------------+----------------------------------------+
| `fish_system <https://fishbase.readthedocs.io/en/latest/fish_system.html>`_      | 系统增强函数包                         |
+----------------------------------------------------------------------------------+----------------------------------------+


安装
=====

.. code:: shell

   # 通过 pip 进行安装或者更新
   pip install -U fishbase


fishbase 能干什么？
===================

举例：

获取文件的绝对路径
------------------------------

.. code:: python

   >>> from fishbase.fish_common import find_files
   >>> print(get_abs_filename_with_sub_path('/etc', 'hosts'))
   (True, '/etc/hosts')


根据时间戳获取时间间隔
------------------------------

.. code:: python

   >>> from fishbase.fish_date import get_time_interval
   >>> print(get_time_interval(1548575829,1548476921))
   {'days': 1, 'hours': 3, 'minutes': 28, 'seconds': 28}


生成随机数据
----------------------

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
--------------------

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


最近更新
==========

2020.3.28 v1.2
------------------
- `#255 <https://github.com/chinapnr/fishbase/issues/255>`_ `#266 <https://github.com/chinapnr/fishbase/issues/266>`_ , 开始使用 github 的 Actions 进行 CI 集成;
- `#257 <https://github.com/chinapnr/fishbase/issues/257>`_ , conf_as_dict() 函数移动从 common 包移动到 system 包;
- `#259 <https://github.com/chinapnr/fishbase/issues/259>`_ , 增加 fish_object 函数包，面向对象增强函数;
- `#260 <https://github.com/chinapnr/fishbase/issues/260>`_ , common 包，删除 sorted_objs_by_attr() 函数和 get_group_list_data() 函数;
- `#261 <https://github.com/chinapnr/fishbase/issues/261>`_ , common 包，paging 函数名称修改为 get_page_data();
- `#263 <https://github.com/chinapnr/fishbase/issues/263>`_ , common 包，删除一些为了向前兼容的函数;
- `#263 <https://github.com/chinapnr/fishbase/issues/263>`_ , 删除 flask swagger 支持;


2019.12.5 v1.1.16
------------------
- 为 flask 应用添加 swagger 模块 `#249 <https://github.com/chinapnr/fishbase/issues/249>`_

2019.7.17 v1.1.15
------------------

- 添加可选参数，定义日志文件格式 `#240 <https://github.com/chinapnr/fishbase/issues/240>`_
- 根据银行卡、身份证获取详细信息的方法 `#243 <https://github.com/chinapnr/fishbase/issues/243>`_

2019.6.25 v1.1.14
------------------

- 修复金额数字转中文大写时多个零的错误 `#238 <https://github.com/chinapnr/fishbase/issues/238>`_
- 按照特定长度分割长文本字符 `#239 <https://github.com/chinapnr/fishbase/issues/239>`_

2019.6.11 v1.1.13
------------------
- 数字金额和中文大写相互转换 `#235 <https://github.com/chinapnr/fishbase/issues/235>`_


更多
====

更多详细文档，请参见：http://fishbase.readthedocs.io/

如有好的建议，欢迎提 issue ：https://github.com/chinapnr/fishbase/issues


感谢
====

非常感谢所有在 fishbase 函数包发展过程中做出共享的朋友们：

Leo

Zhang Muqing

Hu Jun

Jia Chunying

Yan Runsha

Miao Tianshi

Jin Xiongwei

Yi Jun


