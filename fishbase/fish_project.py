# coding=utf-8
"""

``fish_project`` 用来根据配置文件创建项目工程。


"""

# 2018.8.3 add by Jia ChunYing
import yaml

package_yml =  """
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


def init_project_by_yml(yml=None, dist=None):
    pass


def _makedirs_and_files(tree=None):

    pass


tree = yaml.load(package_yml)
print(tree)
a = pannle()