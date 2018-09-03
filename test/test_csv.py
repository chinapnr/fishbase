# coding=utf-8
import io
import os
import sys
import shutil
from fishbase.fish_csv import csv_file_to_list


# 2018.6.27 v1.0.14 #73 create by Jia ChunYing
class TestCsv(object):
    @staticmethod
    def get_test_file(csv_content):
        # 创建csv测试文件
        csv_file_name = '.test_cache_data/test_file.csv'
        if os.path.isfile(csv_file_name):
            os.remove(csv_file_name)
        if not os.path.exists(os.path.dirname(csv_file_name)):
            os.makedirs(os.path.dirname(csv_file_name))
        with io.open(csv_file_name, 'w', encoding='utf8') as f:
            f.write(csv_content)
            f.close()
        return csv_file_name
        
    # 测试 csv_file_to_list()  tc
    def test_csv_01(self):
        csv_content = u"a,b\n1,2"
        csv_file_name = TestCsv.get_test_file(csv_content)
        result = csv_file_to_list(csv_file_name)
        shutil.rmtree(os.path.dirname(csv_file_name))
        assert len(result) == 2
        assert len(result[0]) == 2
        assert len(result[1]) == 2

    # 测试 csv_file_to_list()  tc
    def test_csv_02(self):
        if sys.version > '3':
            csv_content = u"a,b\n1,中文"
            csv_file_name = TestCsv.get_test_file(csv_content)
            with io.open(csv_file_name, 'w', encoding='utf8') as f:
                f.write(csv_content)
                f.close()
            result = csv_file_to_list(csv_file_name, encoding='utf-8')
            shutil.rmtree(os.path.dirname(csv_file_name))
            assert len(result) == 2
            assert len(result[0]) == 2
            assert len(result[1]) == 2

    # 测试 csv_file_to_list()  tc
    def test_csv_03(self):
        if sys.version > '3':
            csv_content = u"a,b\n1,中文"
            csv_file_name = TestCsv.get_test_file(csv_content)
    
            with io.open(csv_file_name, 'w', encoding='gbk') as f:
                f.write(csv_content)
                f.close()
            result = csv_file_to_list(csv_file_name, encoding='gbk')
            shutil.rmtree(os.path.dirname(csv_file_name))
            assert len(result) == 2
            assert len(result[0]) == 2
            assert len(result[1]) == 2
