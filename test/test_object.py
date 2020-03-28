# coding=utf-8
# fish_object.py 单元测试
# 2020.3.28 create by David Yi

from fishbase.fish_object import *
import pytest;


# 2020.3.28 v1.2 create by David Yi; #259
class TestFishObject(object):

    # test singleton() test case
    def test_singleton_01(self):
        t1 = SingleTon()
        t1.x = 2
        t2 = SingleTon()
        t1.x += 1

        assert t2.x == t1.x

        t2.x = 5
        assert t1.x == 5

    # test sort_objs_by_attr() tc
    def test_sort_objs_by_attr_01(self):
        class User(object):
            def __init__(self, user_id):
                self.user_id = user_id

        users = [User(23), User(3), User(99)]
        result_0 = sort_objs_by_attr(users, key='user_id')
        assert result_0[0].user_id == 3

        reverse_result = sort_objs_by_attr(users, key='user_id', reverse=True)
        assert reverse_result[0].user_id == 99

    # test sort_objs_by_attr() tc
    def test_sort_objs_by_attr_02(self):
        class User(object):
            def __init__(self, user_id):
                self.user_id = user_id

        users = [User(23), User(3), User(99)]

        with pytest.raises(AttributeError):
            sort_objs_by_attr(users, key='user_id1')

        assert len(sort_objs_by_attr([], key='user_id')) == 0

    # 测试 serialize_instance() tc
    def test_serialize_instance(self):
        # 定义两个对象
        class ObjA(object):
            def __init__(self, a, b):
                self.a = a
                self.b = b

        class ObjB(object):
            def __init__(self, x, y):
                self.x = x
                self.y = y

        obj_b = ObjB('string', [item for item in range(10)])
        obj_a = ObjA(1, obj_b)
        obj_attr_dict = serialize_instance(obj_a)

        assert '__classname__' in obj_attr_dict
        assert obj_attr_dict.get('__classname__') == 'ObjA'
        assert isinstance(obj_attr_dict.get('b'), dict)

    def test_deserialize_instance(self):
        temp_dict = {'user': {'name': {'last_name': 'zhang', 'first_name': 'san'}, 'address': 'Beijing'}}
        new_obj = DeserializeInstance(temp_dict)
        assert hasattr(new_obj, 'user')
        assert hasattr(new_obj.user, 'name')
        assert new_obj.user.name.last_name == 'zhang'
        assert new_obj.user.address == 'Beijing'
