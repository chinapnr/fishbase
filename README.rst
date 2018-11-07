
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

    from fishbase.fish_common import GetMD5

    # 获取字符换的MD5值
    md5_string = GetMD5.string('hello world!')
    print('md5_string : ', md5_string)
    # 获取文件的MD5值
    file_path = './test_conf.ini'
    md5_file = GetMD5.file(file_path)
    print('md5_file : ', md5_file)
    # 获取hmac算法MD5值
    hmac_md5_string = GetMD5.hmac_md5('hello world!', 'salt')
    print('hmac_md5_string : ', hmac_md5_string)

.. code-block:: text

    md5_string : fc3ff98e8c6a0d3087d515c0473f8677
    md5_file : fb7528c9778b2377e30b0f7e4c26fef0
    hmac_md5_string: 191f82804523bfdafe0188bbbddd6587

Links
=====

详细帮助文档：http://fishbase.readthedocs.io/

测试覆盖率：https://coveralls.io/github/chinapnr/fishbase?branch=master


.. _pip: https://pip.pypa.io/en/stable/quickstart/