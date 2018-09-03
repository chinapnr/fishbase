# coding=utf-8
import os
import shutil
from fishbase.fish_project import init_project_by_yml


# 2018.6.27 v1.0.14 #73 create by Jia ChunYing
class TestProject(object):

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
