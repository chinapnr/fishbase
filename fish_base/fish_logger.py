# coding=utf-8
"""

``fish_logger`` 包含的是日志处理相关的函数。

通过 ``set_log_file()`` 可以方便的进行分卷的日志文件记录。

"""

# 2017.3.5 edit by David.Yi , reference by Ucloud sdk
# 2017.3.15 edit by David.Yi
# 2017.6.20 edit by aoran.xue #14109
# 2017.8.14 move to fish_base

import logging
from logging.handlers import TimedRotatingFileHandler


logger = logging.getLogger()


# 设置日志记录，按照每天一个文件，记录包括 info 以及以上级别的内容
# 输入: local_file 日志文件名
# 2018.2.6 edit by David Yi
# 2018.2.11 edit, log 相关代码优化简化; #11010
# 2018.2.13 edit, remove thread watch
# 2018.4.23 edit，#19023 增加 docstring
def set_log_file(local_file=None):

    """
    设置日志记录，按照每天一个文件，记录包括 info 以及以上级别的内容；

    :param:
        * local_fie: (string) 日志文件名
    :returns:

    举例如下::

        from fish_base.fish_logger import *
        from fish_base.fish_file import *

        log_abs_filename = get_abs_filename_with_sub_path('log', 'fish_test.log')[1]

        set_log_file(log_abs_filename)

        logger.info('test fish base log')
        logger.warn('test fish base log')
        logger.error('test fish base log')

        print('log ok')

    """

    default_log_file = 'default.log'

    _formatter = logging.Formatter(
        '%(asctime)s %(levelname)s %(filename)s[line:%(lineno)d] %(message)s')

    if local_file is not None:
        default_log_file = local_file

    # time rotating file handler
    _tfh = TimedRotatingFileHandler(default_log_file, when="midnight")
    _tfh.setLevel(logging.INFO)
    _tfh.setFormatter(_formatter)

    logger.setLevel(logging.INFO)
    logger.addHandler(_tfh)
