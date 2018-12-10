# coding=utf-8
from fishbase.fish_data import *


# 2018.12.10 v1.1.3  create by Jia ChunYing
class TestData(object):

    def test_is_valid_id_number(self):
        # id number false
        id1 = '320124198701010012'
        assert is_valid_id_number(id1)[0] is False

        # id number true
        id2 = '130522198407316471'
        assert is_valid_id_number(id2)[0] is True

        # id number irregularity
        id3 = '030522198407316471'
        assert is_valid_id_number(id3)[0] is False

        # id number is int
        id3 = 130522198407316471
        assert is_valid_id_number(id3)[0] is True

