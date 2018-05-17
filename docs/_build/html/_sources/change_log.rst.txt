更新记录
===========================

v1.0.11
---------------------------

* 19011, 从19011开始编号，ok
* 19015, ``common conf_as_dict()`` 增加 docstring 说明， ok
* 19016, 开始测试使用 sphinx 来组织 api 说明文档，ok
* 19017, 将 ``conf_as_dict()`` 说明加入到 doc 中，ok
* 19018, __init__.py 中的 ``get_ver()`` 返回版本号功能简化，ok
* 19019, common ``class SingleTon()`` 增加 docstring 说明，ok
* 19020, csv ``csv_file_to_list()`` 增加 docstring 说明，ok
* 19021, common 重新声明为 fish_common, csv 重新生命为 fish_csv, 所有包带 fish 前缀，ok
* 19022, sphinx doc 的 theme 修改为 rtd theme，https://sphinx-rtd-theme.readthedocs.io/en/latest/ , ok
* 19023, logger ``set_log_file()`` 增加 docstring 说明，ok
* 19024, fish_file 函数加入 docstring 说明，ok
* 19025, common, 去除 ``get_md5()`` 函数，ok
* 19026, common, 增加 ``class GetMD5``，增加字符串、小文件、大文件三种类型的 md5计算，ok
* 19027, test, 修改原来的 unittest 部分，完善对于 common 函数的单元测试，ok
* 19028, common, ``conf_as_dict()`` 逻辑修改，更加严密，ok
* 19029, common, 增加 ``json_contained()`` 函数，判断两个 json 是否有包含关系，ok
* 19030, common, 增加 ``splice_url_params()`` 函数；ok


v1.0.10
---------------------------

* 19006, 增加，``get_time_uuid()``, 获得带时间戳的流水号；ok
* 19007, 增加，``if_any_elements_is_space()``, 判断参数列表是否存在 None 或空字符串或空格字符串；ok
* 19008, common，增加 ``conf_as_dict()``,读入配置文件，返回根据配置文件内容生成的字典类型变量; ok
* 11001, 整体结构和开发方法调整；
* 11002, 增加 csv 功能模块，增加函数 ``csv_file_to_list()``; ok
* 11003, fish_file 模块修改为 file，目前向下兼容保留 fish_file; ok
* 11004, file 模块的 ``get_abs_filename_with_sub_path()`` 修改；ok
* 11005, fish_date 模块修改为 date, demo/demo_date.py 演示用法；ok
* 11006, 安装包的安装程序 setup.py 中 setup.py 引入源的修改；ok
* 11007, pip 安装时候支持自动安装 ``python-dateutil`` 包; ok
* 11008, ``check_platform()`` 归入到 system 包
* 11009, csv, ``csv_file_to_list()`` 函数增加过滤空行功能；ok
* 11010, logger, log 相关代码优化简化; ok
* 11011, demo, 将原来 test 下的 test log 程序移动到 demo 路径下; ok
* 11013, demo, ``common.conf_as_dict()`` 的 demo 例子完善；ok
* 11014, common, ``conf_as_dict()`` 增加返回内容，字典长度；ok
* 11015, common 增加 ``class SingleTon``，单例的基础类；ok