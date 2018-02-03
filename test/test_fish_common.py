# fish_common.py 单元测试
# 2017.5.23 create by Leo

from fish_base.fish_common import *
import unittest


class test_if_any_elements_is_space(unittest.TestCase):

    def setUp(self):
        self.empty = ' '
        self.cotain_space = 'Hello World'
        self.cotain_none = [None, 'Hello', 'World']
        self.normal = 'HelloWorld'
        self.not_string = None

    def test_empty_string(self):
        self.assertEquals(if_any_elements_is_space(self.empty), True)

    def test_contain_space_string(self):
        self.assertEquals(if_any_elements_is_space(self.cotain_space), True)

    def test_contain_none_string(self):
        self.assertEquals(if_any_elements_is_space(self.cotain_none), True)

    def test_normal_string(self):
        self.assertEquals(if_any_elements_is_space(self.normal), False)

    def test_not_string(self):
        with self.assertRaises(TypeError):
            if_any_elements_is_space(self.not_string)


class test_if_any_elements_is_special(unittest.TestCase):

    def setUp(self):
        self.contain_special_elements = 'Hello$World'
        self.normal = 'HelloWorld'
        self.not_string = None

    def test_contain_special_elements(self):
        self.assertEquals(if_any_elements_is_special(self.contain_special_elements), False)

    def test_normal_string(self):
        self.assertEquals(if_any_elements_is_special(self.normal), True)

    def test_not_string(self):
        with self.assertRaises(TypeError):
            if_any_elements_is_space(self.not_string)


class test_if_any_elements_is_number(unittest.TestCase):

    def setUp(self):
        self.contain_number_elements = '123'
        self.normal = 'HelloWorld'
        self.not_string = None

    def test_contain_number_elements(self):
        self.assertEquals(if_any_elements_is_number(self.contain_number_elements), True)

    def test_normal_string(self):
        self.assertEquals(if_any_elements_is_number(self.normal), False)

    def test_not_string(self):
        with self.assertRaises(TypeError):
            if_any_elements_is_number(self.not_string)


class test_if_any_elements_is_letter(unittest.TestCase):

    def setUp(self):
        self.contain_letter_elements = 'HelloWorld'
        self.normal = '738&3892*%'
        self.not_string = None

    def test_contain_letter_elements(self):
        self.assertEquals(if_any_elements_is_letter(self.contain_letter_elements), True)

    def test_normal_string(self):
        self.assertEquals(if_any_elements_is_letter(self.normal), False)

    def test_not_string(self):
        with self.assertRaises(TypeError):
            if_any_elements_is_letter(self.not_string)


if __name__ == '__main__':
    unittest.main()
