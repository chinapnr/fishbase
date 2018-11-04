
.. image:: https://travis-ci.org/chinapnr/fishbase.svg?branch=master
    :target: https://travis-ci.org/chinapnr/fishbase
.. image:: https://coveralls.io/repos/github/chinapnr/fishbase/badge.svg?branch=master
    :target: https://coveralls.io/github/chinapnr/fishbase?branch=master
.. image:: https://readthedocs.org/projects/fishbase/badge/?version=latest
    :target: https://fishbase.readthedocs.io/en/latest/?badge=latest

fishbase
========

fishbase 是我们自己开发和整理的一套 Python 基础函数库。 从这几年的
Python
开发中抽象了很多常见的通用的业务逻辑，以希望减少日常开发中的一些重复的工作量。

我们从2016年左右逐渐开始用 Python
开发一些项目，还不能算很有经验，但是也经常碰到一些问题， fishbase
库并不是用来解决很复杂的问题，并且有些是对系统函数的进一步封装，以简化应用程序开发中的工作量和引用的复杂度。

目前，我们正在加快 fishbase
库的建设，包括完善文档和加入单元测试、示例代码、文档等。希望能够帮助到所有的
Python 爱好者和应用开发人员。

Installing
==========

Install and update using `pip`_:

.. code-block:: text

    pip install -U fishbase

Modules
=======

目前主要分为以下模块：

-  fish_common 基本函数包

-  fish_system 系统增强函数包

-  fish_file 文件处理增强函数包

-  fish_csv csv 处理增强函数包

-  fish_logger 日志记录增强函数包

-  fish_project project 目录结构生成函数包

A Simple Example
================

.. code-block:: python

    from fishbase.fish_common import conf_as_dict

    # 定义配置文件名
    conf_filename = 'test_conf.ini'
    ds = conf_as_dict(conf_filename)
    # 显示是否成功，所有 dict 的内容，dict 的 key 数量
    print('flag:', ds[0])
    print('dict:', ds[1])
    print('length:', ds[2])

    d = ds[1]

    # 显示一个 section 下的所有内容
    print('section show_opt:', d['show_opt'])

.. code-block:: text

    flag: True
    dict: (omit)
    length: 7
    section show_opt: {'short_opt': 'b:d:v:p:f:', 'long_opt': 'region=,prov=,mer_id=,mer_short_name=,web_status='}

Links
=====

详细帮助文档：http://fishbase.readthedocs.io/

测试覆盖率：https://coveralls.io/github/chinapnr/fishbase?branch=master
