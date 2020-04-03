# coding=utf-8
# 2020.3.28, create by David Yi;
"""

``fish_object`` 包含的是一些和面向对象相关的函数和类。

"""

from operator import attrgetter

# common data type
commonDataType = tuple([int, float, bool, complex, str, set, list, tuple, dict])


# 申明一个单例类
# 2018.2.13 create by David Yi, #11015
# 2018.4.20 5.19 edit, #19019，增加 docstring
# 2020.3.28, edit, #259, 从 system 移动到 object 单元；
class SingleTon(object):
    """
    申明一个单例类，可以作为需要单例类时候申明用的父类

    :param:
        无
    :returns:
        无

    举例如下::

        print('--- class singleton demo ---')
        t1 = SingleTon()
        t1.x = 2
        print('t1.x:', t1.x)

        t2 = SingleTon()

        t1.x += 1

        print('t1.x:', t1.x)
        print('t2.x:', t2.x)
        print('---')

    执行结果::

        --- class singleton demo ---
        t1.x: 2
        t1.x: 3
        t2.x: 3
        ---

    """

    _state = {}

    def __new__(cls, *args, **kwargs):
        ob = super(SingleTon, cls).__new__(cls)
        # 类维护所有实例的共享属性
        ob.__dict__ = cls._state
        return ob


# 2015.6.14  edit by david.yi
# 2019.03.19 v1.1.7 edit by Hu Jun, edit from Jia Chunying，#215
def serialize_instance(obj):
    """
    对象序列化

    :param:
        * obj: (object) 对象实例

    :return:
        * obj_dict: (dict) 对象序列化字典

    举例如下::

        print('--- serialize_instance demo ---')
        # 定义两个对象
        class Obj(object):
            def __init__(self, a, b):
                self.a = a
                self.b = b

        class ObjB(object):
            def __init__(self, x, y):
                self.x = x
                self.y = y

        # 对象序列化
        b = ObjB('string', [item for item in range(10)])
        obj_ = Obj(1, b)
        print(serialize_instance(obj_))
        print('---')

    执行结果::

        --- serialize_instance demo ---
        {'__classname__': 'Obj', 'a': 1,
        'b': {'__classname__': 'ObjB', 'x': 'string', 'y': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}}
        ---

    """
    obj_dict = {'__classname__': type(obj).__name__}
    obj_dict.update(obj.__dict__)
    for key, value in obj_dict.items():
        if not isinstance(value, commonDataType):
            sub_dict = serialize_instance(value)
            obj_dict.update({key: sub_dict})
        else:
            continue
    return obj_dict


# 2019.03.28 v1.1.8 edit by Hu Jun, edit from Jia Chunying，#215
class DeserializeInstance(object):
    """
    字典对象反序列化

    :param:
        * obj_dict: (dict) 对象序列化字典

    :return:
        * obj: (object) 对象

    举例如下::

        print('--- DeserializeInstance demo ---')
        temp_dict = {'user': {'name': {'last_name': 'zhang', 'first_name': 'san'}, 'address': 'Beijing'}}
        new_obj = DeserializeInstance(temp_dict)
        print('last_name is: ', new_obj.user.name.last_name)
        print('first_name is: ', new_obj.user.name.first_name)
        print('address is: ', new_obj.user.address)
        print('---')

    执行结果::

        --- DeserializeInstance demo ---
        last_name is:  zhang
        first_name is:  san
        address is:  Beijing
        ---

    """

    def __init__(self, obj_dict):
        self.user = None
        for key, value in obj_dict.items():
            if isinstance(value, dict):
                setattr(self, key, DeserializeInstance(value) if isinstance(value, dict) else value)
            else:
                setattr(self, key, value)


# v1.0.15 edit by Hu Jun, #64
def sort_objs_by_attr(objs, key, reverse=False):
    """
    对原生不支持比较操作的对象根据属性排序

    :param:
        * objs: (list) 需要排序的对象列表
        * key: (string) 需要进行排序的对象属性
        * reverse: (bool) 排序结果是否进行反转，默认为 False，不进行反转

    :return:
        * result: (list) 排序后的对象列表

    举例如下::

        print('--- sorted_objs_by_attr demo---')


        class User(object):
            def __init__(self, user_id):
                self.user_id = user_id


        users = [User(23), User(3), User(99)]
        result = sorted_objs_by_attr(users, key='user_id')
        reverse_result = sorted_objs_by_attr(users, key='user_id', reverse=True)
        print([item.user_id for item in result])
        print([item.user_id for item in reverse_result])
        print('---')

    执行结果::

        --- sorted_objs_by_attr demo---
        [3, 23, 99]
        [99, 23, 3]
        ---

    """
    if len(objs) == 0:
        return []
    if not hasattr(objs[0], key):
        raise AttributeError('{0} object has no attribute {1}'.format(type(objs[0]), key))
    result = sorted(objs, key=attrgetter(key), reverse=reverse)
    return result
