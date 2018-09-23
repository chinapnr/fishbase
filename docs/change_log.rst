更新记录
===========================
2018.9.23 v1.1.1
---------------------------
* `#115 <https://github.com/chinapnr/fishbase/issues/115>`_, common,:meth:`fish_common.get_random_str`, optimize;
* `#114 <https://github.com/chinapnr/fishbase/issues/114>`_, common, add function :meth:`fish_common.transform_hump_to_underline`, doc and unittest;
* `#101 <https://github.com/chinapnr/fishbase/issues/101>`_, date, add function :meth:`fish_date.transform_datetime_to_unix`, doc and unittest;


2018.9.3 v1.1.0
---------------------------
* `#74 <https://github.com/chinapnr/fishbase/issues/74>`_, common, add function :meth:`fish_common.get_group_list_data`, doc and unittest;
* `#89 <https://github.com/chinapnr/fishbase/issues/89>`_, common, add function :meth:`fish_common.get_sub_dict`, doc and unittest;
* `#90 <https://github.com/chinapnr/fishbase/issues/90>`_, common, add function :meth:`fish_date.get_time_interval`, doc and unittest;
* `#93 <https://github.com/chinapnr/fishbase/issues/93>`_, common, add function :meth:`fish_date.transform_unix_to_datetime`, doc and unittest;
* `#82 <https://github.com/chinapnr/fishbase/issues/82>`_, project, add function :meth:`fish_project.init_project_by_yml`, doc and unittest;


2018.8.2 v1.0.16
---------------------------
* `#87 <https://github.com/chinapnr/fishbase/issues/87>`_, date, add function :meth:`fish_date.GetRandomTime`, doc and unittest;
* `#94 <https://github.com/chinapnr/fishbase/issues/94>`_, csv, edit function :meth:`fish_csv.csv_file_to_list`, doc and unittest;
* `#94 <https://github.com/chinapnr/fishbase/issues/94>`_, common, edit function :meth:`fish_common.conf_as_dict`, doc and unittest;


2018.7.11 v1.0.15
---------------------------

* `#36 <https://github.com/chinapnr/fishbase/issues/36>`_, common, edit function :meth:`fish_common.is_contain_special_char()`, change function name;
* `#62 <https://github.com/chinapnr/fishbase/issues/62>`_, common, edit function :meth:`fish_common.if_any_elements_is_space()`, optimize, doc and unittest;
* `#78 <https://github.com/chinapnr/fishbase/issues/78>`_, optimize change_log;
* `#67 <https://github.com/chinapnr/fishbase/issues/67>`_, common, edit function :meth:`fish_common.splice_url_params`, optimize;
* `#63 <https://github.com/chinapnr/fishbase/issues/67>`_ and `#77 <https://github.com/chinapnr/fishbase/issues/67>`_, common, add function :meth:`fish_common.remove_duplicate_elements`, doc and unittest;
* `#64 <https://github.com/chinapnr/fishbase/issues/64>`_ common, add function :meth:`fish_common.sorted_objs_by_attr`, doc and unittest;
* `#79 <https://github.com/chinapnr/fishbase/issues/79>`_ common, add function :meth:`fish_common.get_query_param_from_url`, doc and unittest;
* `#83 <https://github.com/chinapnr/fishbase/issues/83>`_ common, edit function :meth:`fish_common.conf_as_dict`, optimize;

2018.6.27 v1.0.14
---------------------------

* 19046, setup, edit setup.py to add long description etc., the package detail;
* issue ID use directly on github
* `#36 <https://github.com/chinapnr/fishbase/issues/36>`_, common, add function :meth:`fish_common.check_str()`, doc and unittest;
* `#38 <https://github.com/chinapnr/fishbase/issues/38>`_, common, add function :meth:`fish_common.find_files()`, doc and unittest;
* `#37 <https://github.com/chinapnr/fishbase/issues/37>`_, date, add function :meth:`fish_date.get_years()`, doc and unittest;
* `#27 <https://github.com/chinapnr/fishbase/issues/27>`_, common, add function :meth:`fish_common.hmac_sha256()`, doc and unittest;
* `#61 <https://github.com/chinapnr/fishbase/issues/61>`_, date, edit function :meth:`fish_date.get_date_range()`, optimize, doc and unittest;
* `#57 <https://github.com/chinapnr/fishbase/issues/57>`_, common, edit function :meth:`fish_common.GetMD5.string()`, optimize;
* `#59 <https://github.com/chinapnr/fishbase/issues/59>`_, common, add function :meth:`fish_common.Base64`, doc and unittest;
* `#51 <https://github.com/chinapnr/fishbase/issues/51>`_, common, add function :meth:`fish_common.get_random_str`, doc and unittest;

2018.6.6 v1.0.13
---------------------------

* 19037, common and system, function ``check_platform()`` move to fish_system 中，rename to :meth:`fish_system.get_platform`;
* 19038, common, add function :meth:`fish_common.get_uuid`, edit ``fish_common.get_time_uuid``, add doc and unittest;
* 19039, logger, edit function :meth:`fish_logger.set_log_file()` by ``class SafeFileHandler()``, prevent the multi process delete log file error;
* 19040, file, edit function :meth:`fish_file.get_abs_filename_with_sub_path`, thanks to Wu Yanan;
* 19041, file, delete function ``check_kind_path_file()``;
* 19042, file, edit function :meth:`fish_file.check_sub_path_create`, optimize, doc and unittest;
* 19043, common, edit function :meth:`fish_common.sorted_list_from_dict()`, optimize, doc and unittest;
* 19044, file, remove ``auto_add_file_ext()``;
* 19045, file, remove ``get_abs_filename_with_sub_path_module()``;

2018.5.21 v1.0.12
---------------------------

* 19035, rename package 'fish_base' to 'fishbase'

2018.5.18 v1.0.11
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
* 19031, 项目，增加 requirements.txt; ok
* 19032, 项目，增加 .travis.yml, 支持持续集成测试; ok
* 19033, 项目，增加对于 coveralls.io 的支持，监视 ut 的覆盖率; 本地 python 2.7.15 测试通过; ok
* 19034, 项目，修改 __init__.py 和 setup.py 中对于 __version__ 的用法; ok


2018.3.20 v1.0.10
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