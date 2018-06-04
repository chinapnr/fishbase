##fish_common 特性列表

last update: 2018.5.26

#### v1.0.13

* 19037, common and system, function check_platform() move to fish_system，rename to get_platform(); ok
* 19038, common, add function get_uuid(), edit get_time_uuid(), add doc and unittest; ok
* 19039, logger, edit function set_log_file() by class SafeFileHandler(), prevent the multi process delete log file; ok
* 19040, file, edit function get_abs_filename_with_sub_path(), suggested by Wu Yanan; ok
* 19041, file, delete function check_kind_path_file(), it's feature include in get_abs_filename_with_sub_path(); ok
* 19042, file, edit function check_sub_path_create(), edit docstring, add unittest; ok
* 19043, common, edit function sorted_list_from_dict(), optimize, doc and unittest; ok
* 19044, common, edit function sorted_list_from_dict(), update doc; ok
* 19045, common, edit function hmac_sha256(), optimize, doc and unittest; ok
* 19046, common, edit function if_element_is_timestamp(), optimize, doc and unittest; ok
* 19047, common, edit function check_number_len(), optimize, doc and unittest; ok
* 19048, common, edit function check_str(), optimize, doc and unittest; ok
* 19049, date, edit function previous_months_date(), optimize, doc and unittest; ok
---

#### v1.0.12

* 19036, edit fish_base to fishbase

---

#### v1.0.11

* 19011，从19011开始编号，ok
* 19015，common conf_as_dict() 增加 docstring 说明， ok
* 19016，开始测试使用 sphinx 来组织 api 说明文档，ok
* 19017，将 conf_as_dict() 说明加入到 doc 中，ok
* 19018，`__init__.py 中的 get_ver() 返回版本号功能简化，ok
* 19019，common class SingleTon() 增加 docstring 说明，ok
* 19020，csv csv_file_to_list() 增加 docstring 说明，ok
* 19021，common 重新声明为 fish_common, csv 重新生命为 fish_csv, 所有包带 fish 前缀，ok
* 19022，sphinx doc 的 theme 修改为 rtd theme，https://sphinx-rtd-theme.readthedocs.io/en/latest/ , ok
* 19023，logger set_log_file() 增加 docstring 说明，ok
* 19024，fish_file 函数加入 docstring 说明，ok
* 19025, common, 去除 get_md5()函数，ok
* 19026, common, 增加 class GetMD5，ok  
https://stackoverflow.com/questions/1131220/get-md5-hash-of-big-files-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
* 19027, test，修改原来的 unittest 部分，先完善对于 common 函数的单元测试，完成 conf_as_dict() 和 GetMD5()等，ok
* 19028, common conf_as_dict 逻辑修改，更加严密, ok

在 PyCharm 中支持 pytest 框架：I think you need to use the Run/Debug Configuration item on the toolbar. 
Click it and 'Edit Configurations' (or alternatively use the menu item Run->Edit Configurations). 
In the 'Defaults' section in the left pane there is a 'py.test' item which I think is what you want.
配置一个专门的测试配置项，运行即可

fish_common 目前测试覆盖率 65%

* 19029, common, 增加 ag bot 所需要的 json_contained() 函数，判断两个 json 是否有包含关系；ok
* 19030, common, 增加 splice_url_params() 函数；ok
* 19031, 项目，增加 requirements.txt; ok
* 19032, 项目，增加 .travis.yml, 准备持续集成测试; ok
* 19033, 项目，增加对于 coveralls.io 的支持，监视覆盖率; 本地 python 2.7.15 测试通过; ok
* 19034, 项目，修改 `__init__.py` 和 setup.py 中对于 `__version__` 的用法; ok
* 19035, common, Add SingleTon() demo and unittest; 

---

#### v1.0.10

* 19006，增加，get_time_uuid(), 获得带时间戳的流水号；ok
* 19007，增加，if_any_elements_is_space(),判断参数列表是否存在不合法的参数，如果存在 None 或空字符串或空格字符串，
    则返回True, 否则返回False；ok
* 19008，common，增加 conf_as_dict(),读入配置文件，返回根据配置文件内容生成的字典类型变量; ok
* 11001，整体结构和开发方法调整；
* 11002, 增加 csv 功能模块，增加函数 csv_file_to_list(); ok
* 11003, fish_file 模块修改为 file，目前向下兼容保留 fish_file; ok
* 11004, file 模块的 get_abs_filename_with_sub_path() 修改；ok
* 11005, fish_date 模块修改为 date, demo/demo_date.py 演示用法；ok
* 11006, 安装包的安装程序 setup.py 中 setup.py 引入源的修改；ok
* 11007, pip 安装时候支持自动安装 python-dateutil 包; ok
* 11008, check_platform() 归入到 system 包
* 11009, csv, csv_file_to_list() 函数增加过滤空行功能；ok
* 11010, logger, log 相关代码优化简化; ok 
* 11011, demo, 将原来 test 下的 test log 程序移动到 demo 路径下; ok
* 11012, common, 原来 fish_common 保存为 common. demo 程序也修改为 demo_common; ok
* 11013, demo, common.conf_as_dict() 的 demo 例子完善；ok
* 11014, common.conf_as_dict() 增加返回内容，字典长度；ok
* 11015, common 增加 class SingleTon，单例的基础类；ok

---

####v1.0.9

* 19001, 增加，check_sub_path_create() 检查当前路径下的某个子路径是否存在, 不存在则创建；ok
* 19002, 修改，get_long_filename_with_sub_dir() 修改为 get_abs_filename_with_sub_path()；ok
* 19003, 修改，所有文件相关操作，转移到独立 py 文件; ok
* 19004, 修改，get_long_filename_with_sub_dir_module() 修改为 get_abs_filename_with_sub_path_module(); ok
* 19005, 修改，long_filename 都修改为 abd_filename; ok

---

补充

* 文档主题需要安装 pip install sphinx_rtd_theme