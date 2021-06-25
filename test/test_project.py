# coding=utf-8
import os
import shutil

import pytest

from fishbase.fish_project import init_project_by_yml


# 2018.6.27 v1.0.14 #73 create by Jia ChunYing
class TestProject(object):

    # 2021.6.22, #294, 修复小错误
    def test_load_bad_01(self):
        """
        empty file
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        target_file = base_dir + os.sep + 'test_project_with_empty_file.yaml'
        with open(target_file, 'wb') as f:
            f.close()
        with pytest.raises(KeyError) as e:
            init_project_by_yml(target_file, '.')
        exec_msg = e.value.args[0]
        assert exec_msg == 'project config format Error: fail to load'
        # os.remove(target_file)

    def test_init_project_by_yml(self):
        # define yml string
        package_yml = '''
                    project: hellopackage
                    tree:
                        - README.md
                        - requirements.txt
                        - setup.py
                        - MANIFEST.in
                        - hellopackage: # project name
                            - __init__.py
                        - test: # unittest file
                            - __init__.py
                        - demo: # usage demo
                            - __init__.py
                        - doc: # documents
                    '''
        # init project by yml
        init_project_by_yml(package_yml, '.')
        result = os.listdir('./hellopackage')
        expect = ['demo', 'requirements.txt', 'test', 'MANIFEST.in', 'hellopackage', 'README.md', 'setup.py', 'doc']
        for ele in expect:
            assert ele in result

        # 删除临时文件
        shutil.rmtree('./hellopackage')
