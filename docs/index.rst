.. fish_base documentation master file, created by
   sphinx-quickstart on Wed Apr 18 15:20:36 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

fish_base 函数库使用说明
=====================================

**fish_base** 是我们自己开发、收集和整理的一套 Python 基础函数库。
抽象了很多常见的通用的业务逻辑，以希望减少日常开发中的一些重复的工作量。

.. toctree::
   :maxdepth: 1

   update


API 函数列表
-----------------------------

可以到以下单元中查找具体的函数列表和使用说明。

.. toctree::
   :maxdepth: 2

   fish_common
   fish_file
   fish_csv
   fish_logger

从 ``v1.0.11`` 开始，所有 fish_base 的引用需要用如下格式::

    from fish_base.fish_aaaa import *

也就是所有的 fish_base 模块都使用 ``fish_`` 开头。


