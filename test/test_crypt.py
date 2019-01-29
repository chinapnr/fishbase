# coding=utf-8
import os
import sys
import pytest
from fishbase.fish_crypt import *


# 定义当前路径
current_path = os.path.dirname(os.path.abspath(__file__))
# 定义配置文件名
conf_filename = os.path.join(current_path, 'test_conf.ini')
error_conf_filename = os.path.join(current_path, 'test_conf1.ini')


# 2019.01.21 v1.1.6 create by Hu Jun
class TestCrypt(object):
    # 测试 FishMD5()  tc
    def test_md5_01(self):
        assert FishMD5.string('hello world!') == 'fc3ff98e8c6a0d3087d515c0473f8677'
        # different line separator will get different md5 value
        assert FishMD5.file(conf_filename) in ['c73ec5050bbff26ade9330bbe0bd7a25',
                                               '8d4f03dc6b223bd199be6aa53d5d4f5c']
        assert FishMD5.big_file(conf_filename) in ['c73ec5050bbff26ade9330bbe0bd7a25',
                                                   '8d4f03dc6b223bd199be6aa53d5d4f5c']

    # 测试 FishMD5()  tc
    def test_md5_02(self):

        assert FishMD5.string('hello world') != 'fc3ff98e8c6a0d3087d515c0473f8677'

        if sys.version > '3':
            with pytest.raises(FileNotFoundError):
                FishMD5.file(error_conf_filename)
        else:
            with pytest.raises(IOError):
                FishMD5.file(error_conf_filename)

        assert FishMD5.file(conf_filename) != 'bb7528c9778b2377e30b0f7e4c26fef0'

    # 测试 FishMD5()  tc
    def test_md5_03(self):
        salt = 'm4xV2yGFSn'
        assert FishMD5.string('hello world!', salt) == '984d47991401fad7d920a30f715cfd22'

    # 测试 FishMD5()  tc
    def test_md5_04(self):
        salt = 'salt'
        assert FishMD5.hmac_md5('hello world!', salt) == '191f82804523bfdafe0188bbbddd6587'

    # test Base64() tc
    def test_base64_01(self):
        assert FishBase64.string('hello world') == b'aGVsbG8gd29ybGQ='
    
        assert len(FishBase64.file(conf_filename)) != 0
    
        assert FishBase64.decode(b'aGVsbG8gd29ybGQ=') == b'hello world'
    
        assert FishBase64.decode(b'aGVsbG8gd29ybGQ=') != b'hello'
    
    # test FishSha256.hmac_sha256() tc
    def test_hmac_sha256_02(self):
        message = 'Hello HMAC'
        secret = '12345678'
        assert (FishSha256.hmac_sha256(secret, message) ==
                '5eb8bdabdaa43f61fb220473028e49d40728444b4322f3093decd9a356afd18f')

    # test FishSha256.hashlib_sha256() tc
    def test_hashlib_sha256_01(self):
        message = 'Hello HMAC'
        assert (FishSha256.hashlib_sha256(message) ==
                '4a1601381dfb85d6e713853a414f6b43daa76a82956911108512202f5a1c0ce4')
