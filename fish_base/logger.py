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
def set_log_file(local_file=None):

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
