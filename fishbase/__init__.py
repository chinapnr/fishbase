# coding=utf-8
# 2015.6.6 create by david.yi
# add function get_md5()
# 2015.6.7 add def input_field(info, field_default) 提示用户输入指定解释信息的字段名称
# 2015.6.14 r2 项目开始使用 fpytools
#   增加 对象序列化函数 serialize_instance
# 2015.8.1 加入 auto_add_file_ext() ablist_minus() format_list_on_head()
# 2016.2.22 修改名称为 fish_base.py, 继续作为 e2at 项目的底层支持
# 2016.4.1 edit fish_base directory to common
# 2016.4.3 edit begin update to version v1.0.5
# 2016.4.26 start v1.0.8 add date functions
# 2016.10.4 start v1.0.9
# 2017.1.8 v1.0.9, add fish_file.py
# 2018.1.1 v1.0.10, delete old functions
# 2018.4.8 v1.0.11, delete old import
# 2018.5.18 v1.0.11, user __version__


from .fish_common import *
from .fish_crypt import *
from .fish_csv import *
from .fish_data import *
from .fish_date import *
from .fish_file import *
from .fish_logger import *
from .fish_system import *
from .fish_project import *
from .fish_random import *

__version__ = '1.1.7'  # type: str
