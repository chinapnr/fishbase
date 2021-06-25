# coding=utf-8
"""

``fish_logger`` 包含的是日志处理相关的函数。

通过 ``set_log_file()`` 可以方便的进行分卷的日志文件记录。

"""

# 2017.3.5 edit by David.Yi , reference by Ucloud sdk
# 2017.3.15 edit by David.Yi
# 2017.6.20 edit by aoran.xue #14109
# 2017.8.14 move to fish_base

import sys
import logging
from logging import FileHandler
import codecs
import time
import os

logger = logging.getLogger()


# 2018.5.27 v1.0.13 #13039, edit by David Yi
# edit from https://www.jianshu.com/p/d615bf01e37b
class SafeFileHandler(FileHandler):

    def __init__(self, filename, mode='a', encoding=None, delay=0,
                 file_name_format='%project_name-%log-%date'):
        """
        Use the specified filename for streamed logging
        """
        if codecs is None:
            encoding = None
        FileHandler.__init__(self, filename, mode, encoding, delay)

        # 日志文件路径
        self.file_path = os.path.split(filename)[0]
        # 日志文件名称
        file_name = os.path.split(filename)[1]

        temp_file_name = file_name.split('.')
        if len(temp_file_name) == 1:
            self.project_name = temp_file_name[0]
            self.log_suffix = 'log'
        else:
            self.project_name, self.log_suffix = temp_file_name[0], temp_file_name[1]

        self.mode = mode
        self.encoding = encoding
        self.suffix = "%Y-%m-%d"
        self.suffix_time = ""
        self.file_name_format = file_name_format

    def emit(self, record):
        """
        Emit a record.

        Always check time
        """
        try:
            if self.check_base_filename(record):
                self.build_base_filename()
            FileHandler.emit(self, record)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

    def check_base_filename(self, record):
        """
        Determine if builder should occur.

        record is not used, as we are just comparing times,
        but it is needed so the method signatures are the same
        """
        time_tuple = time.localtime()

        if self.file_name_format:
            pass

        if self.suffix_time != time.strftime(self.suffix, time_tuple) or not os.path.exists(
                self._get_format_filename()):
            return 1
        else:
            return 0

    def build_base_filename(self):
        """
        do builder; in this case,
        old time stamp is removed from filename and
        a new time stamp is append to the filename
        """
        if self.stream:
            self.stream.close()
            self.stream = None

        # remove old suffix
        # if self.suffix_time != "":
        #     index = self.baseFilename.find("." + self.suffix_time)
        #     if index == -1:
        #         index = self.baseFilename.rfind(".")
        #     self.baseFilename = self.baseFilename[:index]

        # add new suffix
        current_time_tuple = time.localtime()
        self.suffix_time = time.strftime(self.suffix, current_time_tuple)
        self.baseFilename = self._get_format_filename()

        self.mode = 'a'
        if not self.delay:
            self.stream = self._open()

    def _get_format_filename(self):
        split_list = self.file_name_format.split('-')
        name_mapping = {'%log': self.log_suffix,
                        '%project_name': self.project_name,
                        '%date': self.suffix_time}
        new_file_name = '.'.join([name_mapping.get(i) for i in split_list])
        return os.path.join(self.file_path, new_file_name)


# 设置日志记录，按照每天一个文件，记录包括 info 以及以上级别的内容
# 输入: local_file 日志文件名
# 2018.2.6 edit by David Yi
# 2018.2.11 edit, log 相关代码优化简化; #11010
# 2018.2.13 edit, remove thread watch
# 2018.4.23 edit，#19023 增加 docstring
# 2019.7.16 v1.1.15 #240 edit by Hu Jun
def set_log_file(local_file=None, file_name_format='%project_name-%log-%date'):

    """
    设置日志记录，按照每天一个文件，记录包括 info 以及以上级别的内容；
    日志格式采取日志文件名直接加上日期，比如 fish_test.log.2018-05-27

    :param:
        * local_fie: (string) 日志文件名
        * file_name_format: (string) 日志文件名格式
    :return: 无

    举例如下::

        from fishbase.fish_logger import *
        from fishbase.fish_file import *

        log_abs_filename = get_abs_filename_with_sub_path('log', 'fish_test.log')[1]

        set_log_file(log_abs_filename)

        logger.info('test fish base log')
        logger.warn('test fish base log')
        logger.error('test fish base log')

        print('log ok')

    """

    default_log_file = 'default.log'
    if local_file is not None:
        default_log_file = local_file

    # 创建日志目录
    parent_dir = os.path.dirname(default_log_file)
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)

    support_split = ['%project_name', '%log', '%date']

    file_format_split = file_name_format.split('-')
    if set(file_format_split) != set(support_split):
        raise ValueError('file_name_format error, please check and try again!')
    
    # time rotating file handler
    # _tfh = TimedRotatingFileHandler(default_log_file, when="midnight")
    _tfh = SafeFileHandler(filename=default_log_file, file_name_format=file_name_format)
    _tfh.setLevel(logging.INFO)

    _formatter = logging.Formatter(
        '%(asctime)s %(levelname)s %(filename)s[ln:%(lineno)d] %(message)s')
    _tfh.setFormatter(_formatter)

    logger.setLevel(logging.INFO)

    logger.addHandler(_tfh)


# 2019.4.16 edit by jun.hu #221
def set_log_stdout():
    """
    设置输出到标准输出中

    :param: 无
    :return: 无

    举例如下::

        from fishbase.fish_logger import *

        set_log_stdout()

        logger.info('test fish base log')
        logger.warn('test fish base log')
        logger.error('test fish base log')

        print('log ok')
    """
    _formatter = logging.Formatter(
        '%(asctime)s %(levelname)s %(filename)s[ln:%(lineno)d] %(message)s')

    logger.setLevel(logging.INFO)
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(_formatter)

    logger.addHandler(stdout_handler)
