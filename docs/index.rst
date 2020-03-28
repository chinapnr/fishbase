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

fishbase 是由我们自主开发和整理的一套 Python 基础函数库，将我们平时在开发 Python 项目时候的各类工具函数汇聚到一起，方便集中管理和使用。

fishbase 当前版本为 v1.2，支持 Python 3.5-3.8，绝大部分函数也能工作在 Python 2.7 下，但是我们不推荐使用 Python 2.7 。

自 2016/3 初次发布以来，我们坚持不断更新，先后发布了 20 余个版本。近一年来，我们逐步形成每月更新 1 到 2 个版本的频率，抽象出了很多通用的方法，主要分为以下模块：


+----------------------------------------------------------------------------------+----------------------------------------+
| 模块                                                                             | 功能函数                               |
+==================================================================================+========================================+
| `fish_common <https://fishbase.readthedocs.io/en/latest/fish_common.html>`_      | 基本功能函数包                         |
+----------------------------------------------------------------------------------+----------------------------------------+
| `fish_object <https://fishbase.readthedocs.io/en/latest/fish_object.html>`_      | 面向对象函数包                         |
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
| `swagger <https://fishbase.readthedocs.io/en/latest/swagger.html>`_              | 集成swagger为flask应用生成接口文档信息 |
+----------------------------------------------------------------------------------+----------------------------------------+


安装
=====

.. code:: shell

   # 通过 pip 进行安装或者更新
   pip install -U fishbase


fishbase 能干什么？
===================


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


集成 swagger 为 flask 应用生成接口文档信息
-----------------------------------------------

.. code:: python

   >>> from fishbase.swagger import doc
   >>> from fishbase.swagger.swagger import flask_swagger
   >>> from flask import Flask

   >>> # 创建 Flask app
   >>> app = Flask("Demo Server")

   >>> @app.route('/v1/query', methods=['GET'])
   >>> @doc.summary("xx业务查询接口", group="xx业务")
   >>> @doc.description("测试 Swagger 使用, 参数为 URL 参数 token, 且必传")
   >>> @doc.consumes("token", required=True)
   >>> def test_query():
   >>>     pass

   >>> # 将 app 对象传递给 swagger 模块
   >>> flask_swagger(app)

   >>> if __name__ == "__main__":
   >>>     app.run("127.0.0.1", "8899", debug=False)

访问: http://127.0.0.1:8899/swagger/ 即可查看接口信息，并在线调试。更多 swagger 使用技巧，可参考 https://fishbase.readthedocs.io/en/latest/swagger.html


.. toctree::
   :maxdepth: 1

   change_log


API 函数列表
-----------------------------

可以到以下单元中查找具体的函数列表和使用说明。

.. toctree::
   :maxdepth: 2

   fish_common
   fish_object
   fish_crypt
   fish_csv
   fish_data
   fish_date
   fish_file
   fish_logger
   fish_project
   fish_system
   fish_random
   swagger


更多
====

如有好的建议，欢迎提 issue ：https://github.com/chinapnr/fishbase/issues

感谢
====

非常感谢所有在 fishbase 函数包发展过程中做出共享的朋友们：

Leo

Zhang Muqing

Hu Jun

Jia Chunyin

Yan Runsha

Miao Tianshi

Jin Xiongwei

Yi Jun