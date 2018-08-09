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
            - jarvis:
                - __init__.py
                - jaccount.py
                - jfetch.py
                - jfile.py
                - jman.py
            - saturn:
                - __init__.py
                - pegasus.py
                - pyxis.py
"""


def init_project_by_yml(project_config=None, dist=None):
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


def init_package_project(dist=None):
    init_project_by_yml(package_yml, dist)


def init_web_project(dist=None):
    init_project_by_yml(web_yml, dist)


if __name__ == '__main__':

    init_project_by_yml(web_yml)
