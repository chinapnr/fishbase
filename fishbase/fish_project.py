# coding=utf-8
"""

``fish_project`` 用来根据配置文件创建项目工程。

"""

# 2018.8.3 add by Jia ChunYing
from __future__ import print_function
import yaml
import os


package_yml = """
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

"""

web_yml = """
project: helloweb
tree:
    - README.md
    - server.py
    - requirements.txt
    - application:
        - __init__.py
        - controller:
            - __init__.py
        - model:
            - __init__.py
    - config:
        - __init__.py
    - doc:
    - docker:
        - Dockerfile
        - docker-compose.yml
        - start.sh
    - log:
    - sample:
      - hello.py
    - test:
        - __init__.py
    - tool:
        - __init__.py
        - sdk:
            - __init__.py
"""


# 通过配置文件初始化一个project
# create 2018.8.3 by Jia ChunYing
def init_project_by_yml(project_config=None, dist=None):
    """
        通过配置文件初始化一个 project

        :param:
            * project_config: (string) 用来生成 project 的配置文件
            * dist: (string) project 位置

        举例如下::

            print('--- init_project_by_yml demo ---')
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
            print(os.listdir('./hellopackage'))
            print('---')

        输出结果::

            --- init_project_by_yml demo ---
            ['demo', 'requirements.txt', 'test', 'MANIFEST.in', 'hellopackage', 'README.md', 'setup.py', 'doc']
            ---
    """
    if os.path.isfile(project_config):
        project_config = open(project_config)
    try:
        yml_data = yaml.load(project_config)
        project_name = yml_data['project']
        project_tree = yml_data['tree']
    except Exception as e:
        raise KeyError('project config format Error: {}'.format(e))
    if dist is None:
        dist = os.path.abspath('.')
    project_path = os.path.join(dist, project_name)
    _makedirs_if_not_extis(project_path)
    _makedirs_and_files(project_path, project_tree)


def _makedirs_and_files(rootdir, tree):
    if not tree:
        return
    for item in tree:
        if isinstance(item, str):
            file_path = os.path.join(rootdir, item)
            _create_null_file(file_path)
        elif isinstance(item, dict):
            subdir = list(item.keys())[0]
            subdir_path = os.path.join(rootdir, subdir)
            _makedirs_if_not_extis(subdir_path)
            _makedirs_and_files(subdir_path, item[subdir])


def _create_null_file(file_path):
    if os.path.isfile(file_path) is False:
        with open(file_path, 'wb') as f:
            f.close()


def _makedirs_if_not_extis(dir_path):
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
