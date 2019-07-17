# coding=utf-8
# fish_logging.py 单元测试
# 2018.7.17 create by Hu Jun

import os
import time
import shutil
import pytest
from fishbase.fish_logger import set_log_file, logger as log
# 定义当前路径
current_path = os.path.dirname(os.path.abspath(__file__))


class TestFishLogging(object):
    log_filename = ''
    suffix = "%Y-%m-%d"
    suffix_time = ''
    log_path = ''

    def setup_class(self):
        # 定义配置文件名
        self.log_path = os.path.join(current_path, 'log_path')
        if not os.path.exists(self.log_path):
            os.mkdir(self.log_path)
        
        self.log_filename = os.path.join(self.log_path, 'unittest.log')
        
        current_time_tuple = time.localtime()
        self.suffix_time = time.strftime(self.suffix, current_time_tuple)

    def teardown_class(self):
        try:
            # 关闭日志文件句柄
            for h in log.handlers:
                h.close()
            shutil.rmtree(self.log_path)
        except Exception as _:
            pass
        
    def test_format1(self):
        set_log_file(self.log_filename)
        log.info('test_format1')
        assert 'unittest.log.{}'.format(self.suffix_time) in os.listdir(self.log_path)

    def test_format2(self):
        set_log_file(self.log_filename, file_name_format='%project_name-%date-%log')
        log.info('test_format2')
        assert 'unittest.{}.log'.format(self.suffix_time) in os.listdir(self.log_path)

    def test_format3(self):
        set_log_file(self.log_filename, file_name_format='%date-%project_name-%log')
        log.info('test_format3')
        assert 'unittest.log.{}'.format(self.suffix_time) in os.listdir(self.log_path)

    def test_format4(self):
        with pytest.raises(ValueError):
            set_log_file(self.log_filename, file_name_format='%date-%project_name-%log1')
