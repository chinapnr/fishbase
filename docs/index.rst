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


fishbase 简介
=================

fishbase 是由我们开发和整理的一套 Python基础函数库，将我们平时在开发 Python项目时候的各类工具函数汇聚到一起，方便集中管理和使用。希望对你也有所帮助，也适合初学 Python 的朋友通过代码来学习。

fishbase 最新版本为 v1.6，支持 Python 3.5-3.10，绝大部分函数也能工作在 Python 2.7下，但是我们不推荐使用 Python 2.7。

fishbase 主要有以下功能模块：

+-------------------------------------------------------------------------------+--------------------------------------+
|                                     模块                                      |               功能函数               |
+===============================================================================+======================================+
| `fish_common <https://fishbase.readthedocs.io/en/latest/fish_common.html>`_   | 基本函数包                           |
+-------------------------------------------------------------------------------+--------------------------------------+
| `fish_crypt <https://fishbase.readthedocs.io/en/latest/fish_crypt.html>`_     | 加密数据函数包                       |
+-------------------------------------------------------------------------------+--------------------------------------+
| `fish_csv <https://fishbase.readthedocs.io/en/latest/fish_csv.html>`_         | csv处理增强函数包                    |
+-------------------------------------------------------------------------------+--------------------------------------+
| `fish_data <https://fishbase.readthedocs.io/en/latest/fish_data.html>`_       | 数据处理函数包，包括银行卡、身份证等 |
+-------------------------------------------------------------------------------+--------------------------------------+
| `fish_date <https://fishbase.readthedocs.io/en/latest/fish_date.html>`_       | 日期处理增强函数包                   |
+-------------------------------------------------------------------------------+--------------------------------------+
| `fish_file <https://fishbase.readthedocs.io/en/latest/fish_file.html>`_       | 文件处理增强函数包                   |
+-------------------------------------------------------------------------------+--------------------------------------+
| `fish_logger <https://fishbase.readthedocs.io/en/latest/fish_logger.html>`_   | 日志记录增强函数包                   |
+-------------------------------------------------------------------------------+--------------------------------------+
| `fish_project <https://fishbase.readthedocs.io/en/latest/fish_project.html>`_ | 项目目录结构生成函数包               |
+-------------------------------------------------------------------------------+--------------------------------------+
| `fish_random <https://fishbase.readthedocs.io/en/latest/fish_random.html>`_   | 随机数据生成增强函数包               |
+-------------------------------------------------------------------------------+--------------------------------------+
| `fish_system <https://fishbase.readthedocs.io/en/latest/fish_system.html>`_   | 系统增强函数包                       |
+-------------------------------------------------------------------------------+--------------------------------------+


安装
=====

.. code:: shell

   # 通过 pip 进行安装或者更新
   pip install -U fishbase


fishbase 功能举例
===================

获取文件的绝对路径
------------------------------

.. code:: python

   >>> from fishbase.fish_files import get_abs_filename_with_sub_path
   >>> print(get_abs_filename_with_sub_path('/etc', 'hosts'))
   (True, '/etc/hosts')


根据时间戳获取时间间隔
------------------------------

.. code:: python

   >>> from fishbase.fish_date import get_time_interval
   >>> print(get_time_interval(1548575829,1548476921))
   {'days': 1, 'hours': 3, 'minutes': 28, 'seconds': 28}


生成随机符合校验规则的身份证和银行卡数据
--------------------------------------------------

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


更新记录
==========

2022.9.13 v1.6
------------------
- `#303 <https://github.com/chinapnr/fishbase/issues/303>`_ , update setup.py, add install_requires `chardet`
- `#302 <https://github.com/chinapnr/fishbase/pull/302>`_ , update fish_common.py, modify yaml load method.

2021.7.20 v1.5
------------------
- `#300 <https://github.com/chinapnr/fishbase/issues/300>`_ , fish_logger 中的 log 文件默认后缀修改为 .log，日期移到文件名开头;
- 修改文档描述


2021.6.23 v1.4
------------------
- `#288 <https://github.com/chinapnr/fishbase/issues/288>`_ , fish_date 中的 GetRandomTime 修改为 RandomTime，其中函数名称修改为 get_random_datetime_this_month() get_random_datetime_this_year() get_random_date_by_year() get_random_date_by_range();
- `#292 <https://github.com/chinapnr/fishbase/issues/292>`_ , fish_data 增加敏感数据掩码显示类 SensitiveMask，增加函数 get_idcard_number() get_bankcard_number() get_mobile_number() get_email() ;
- 修改小错误
- 修改文档描述

2020.4.25 v1.3
------------------
- `#273 <https://github.com/chinapnr/fishbase/issues/273>`_ , 随机数包的文档举例中的函数名称错误修正;
- `#275 <https://github.com/chinapnr/fishbase/issues/275>`_ , 随机数，gen_random_id_card() 函数优化;

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
- 为 flask应用添加 swagger模块 `#249 <https://github.com/chinapnr/fishbase/issues/249>`_

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


详细帮助
==========

更多详细文档，请参见：http://fishbase.readthedocs.io/

如有好的建议，欢迎提 issue ：https://github.com/chinapnr/fishbase/issues


感谢
====

自2016年3月初次发布以来，先后发布了20余个版本，非常感谢所有在 fishbase函数包发展过程中做出贡献的朋友们！

fishbase函数包的作者名单，按照时间先后列出如下：

Yi Jun

Leo

Zhang Muqing

Hu Jun

Jia Chunying

Yan Runsha

Miao Tianshi

Jin Xiongwei

Wang Xiaolong

