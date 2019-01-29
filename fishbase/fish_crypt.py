# coding=utf-8
"""

``fish_crypt`` 包含的是一些加密、编码数据的函数，比如 MD5、SHA256 的计算。

原来这些方法属于 fish_common 模块, 因 fish_common 过于杂乱，故重新进行分类整理。
"""

# 2019.01.21 v1.1.6 created by Hu Jun

import hashlib
import hmac
import base64


# 2018.5.8 edit by David Yi, edit from Jia Chunying，#19026
# 2018.6.12 edit by Hu Jun, edit from Jia Chunying，#37
# 2018.10.28 edit by Hu Jun, #99
# 2019.01.06 edit by Hu Jun, #152
# 2019.01.21 v1.1.6 edit by Hu Jun, #200 move fish_common.FishMD5 to fish_crypt.FishMD5
class FishMD5(object):
    """
    计算普通字符串和一般的文件，对于大文件采取逐步读入的方式，也可以快速计算；基于 Python 的 hashlib.md5() 进行封装和扩展；

    举例如下::

        print('--- md5 demo ---')
        print('string md5:', GetMD5.string('hello world!'))
        file_path = get_abs_filename_with_sub_path('test_conf', 'test_conf.ini')[1])
        print('file md5:', GetMD5.file(file_path)
        big_file_path = get_abs_filename_with_sub_path('test_conf', 'test_conf.ini')[1])
        print('big file md5:', GetMD5.big_file(big_file_path)
        print('string hmac_md5:', GetMD5.hmac_md5('hello world!', 'salt'))
        print('---')

    执行结果::

        --- md5 demo ---
        string md5: fc3ff98e8c6a0d3087d515c0473f8677
        file md5: fb7528c9778b2377e30b0f7e4c26fef0
        big file md5: fb7528c9778b2377e30b0f7e4c26fef0
        string hmac_md5: 191f82804523bfdafe0188bbbddd6587
        ---

    """
    @staticmethod
    def string(s, salt=None):
        """
        获取一个字符串的 MD5 值

        :param:
            * s: (string) 需要进行 hash 的字符串
            * salt: (string) 随机字符串，默认为 None
        :return:
            * result: (string) 32 位小写 MD5 值
        """
        m = hashlib.md5()
        s = s.encode('utf-8') + salt.encode('utf-8') if salt is not None else s.encode('utf-8')
        m.update(s)
        result = m.hexdigest()
        return result
    
    @staticmethod
    def file(filename):
        """
        获取一个文件的 MD5 值

        :param:
            * filename: (string) 需要进行 hash 的文件名
        :return:
            * result: (string) 32位小写 MD5 值
        """
        m = hashlib.md5()
        with open(filename, 'rb') as f:
            m.update(f.read())
            result = m.hexdigest()
            return result
    
    @staticmethod
    def big_file(filename):
        """
        获取一个大文件的 MD5 值

        :param:
            * filename: (string) 需要进行 hash 的大文件路径
        :return:
            * result: (string) 32位小写 MD5 值
        """
        
        md5 = hashlib.md5()
        with open(filename, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                md5.update(chunk)
        
        result = md5.hexdigest()
        return result
    
    @staticmethod
    def hmac_md5(s, salt):
        """
        获取一个字符串的 使用 salt 加密的 hmac MD5 值

        :param:
            * s: (string) 需要进行 hash 的字符串
            * salt: (string) 随机字符串
        :return:
            * result: (string) 32位小写 MD5 值
        """
        hmac_md5 = hmac.new(salt.encode('utf-8'), s.encode('utf-8'),
                            digestmod=hashlib.md5).hexdigest()
        return hmac_md5


# v1.0.14 edit by Hu Jun, #59
# 2019.01.21 v1.1.6 edit by Hu Jun, #200 move fish_common.Base64 to fish_crypt.Base64
class FishBase64(object):
    """
    计算返回文件和字符串的 base64 编码字符串

    举例如下::

        print('--- FishBase64 demo ---')
        print('string base64:', FishBase64.string('hello world!'))
        file_path = get_abs_filename_with_sub_path('test_conf', 'test_conf.ini')[1])
        print('file base64:', FishBase64.file(file_path)
        print('decode base64:', Base64.decode(b'aGVsbG8gd29ybGQ='))
        print('---')

    执行结果::

        --- FishBase64 demo ---
        string base64: b'aGVsbG8gd29ybGQ='
        file base64: (b'IyEvYmluL2Jhc2gKCmNkIC9yb290L3d3dy9zaW5nbGVfcWEKCm5vaHVwIC9yb2
        90L2FwcC9weXRob24zNjIvYmluL2d1bmljb3JuIC1jIGd1bmljb3JuLmNvbmYgc2luZ2xlX3NlcnZlcjphcHAK')
        decode base64: b'hello world'
        ---

    """
    @staticmethod
    def string(s):
        """
        获取一个字符串的 base64 值

        :param:
            * s: (string) 需要进行 base64 编码 的字符串
        :return:
            * (bytes) base64 编码结果
        """
        return base64.b64encode(s.encode('utf-8'))
    
    @staticmethod
    def file(filename):
        """
        获取一个文件的 base64 值

        :param:
            * filename: (string) 需要进行 base64 编码 文件路径
        :return:
            * (bytes) base64 编码结果
        """
        with open(filename, 'rb') as f:
            return base64.b64encode(f.read())
    
    @staticmethod
    def decode(s):
        """
        获取 base64 解码结果

        :param:
            * filename: (string) 需要进行 base64 编码 文件路径
        :return:
            * (bytes) base64 解码结果
        """
        return base64.b64decode(s)


# v1.1.3 edit by Hu Jun, #100
# 2019.01.06 v1.1.6 edit by Hu Jun, #152
# 2019.01.21 v1.1.6 edit by Hu Jun, #200 move fish_common.FishSha256 to fish_crypt.FishSha256
class FishSha256(object):
    """
    计算字符串和密钥的 sha256 算法哈希值

    举例如下::

        print('--- GetSha256 demo ---')
        # 定义哈希字符串
        message = 'Hello HMAC'
        # 定义密钥
        secret = '12345678'
        print('hmac_sha256:', GetSha256.hmac_sha256(secret, message))
        print('hashlib_sha256:', GetSha256.hashlib_sha256(message))
        print('---')

    执行结果::

        --- GetSha256 demo ---
        hmac_sha256: 5eb8bdabdaa43f61fb220473028e49d40728444b4322f3093decd9a356afd18f
        hashlib_sha256: 4a1601381dfb85d6e713853a414f6b43daa76a82956911108512202f5a1c0ce4
        ---

    """
    @staticmethod
    def hmac_sha256(secret, message):
        """
        获取一个字符串的在密钥 secret 加密下的 sha256 哈希值

        :param:
            * secret: (string) 哈希算法的密钥
            * message: (string) 需要进行哈希的字符串
        :return:
            * hashed_str: sha256 算法哈希值
        """
        hashed_str = hmac.new(secret.encode('utf-8'),
                              message.encode('utf-8'),
                              digestmod=hashlib.sha256).hexdigest()
        return hashed_str

    @staticmethod
    def hashlib_sha256(message):
        """
        获取一个字符串的 sha256 哈希值

        :param:
            * message: (string) 需要进行哈希的字符串
        :return:
            * hashed_str: sha256 算法哈希值
        """
        hashlib_sha256 = hashlib.sha256()
        hashlib_sha256.update(message.encode('utf-8'))
        hashed_str = hashlib_sha256.hexdigest()
        return hashed_str
