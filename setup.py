# from distutils.core import setup
from setuptools import setup
import io
import re

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

with io.open('fishbase/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

setup(
    name='fishbase',
    version=version,
    install_requires=['python-dateutil',
                      'pyyaml'],

    url='https://github.com/chinapnr/fishbase',
    license='MIT',
    author='David Yi',
    author_email='wingfish@gmail.com',
    description='some useful functions for python',
    long_description=readme,
    packages=['fishbase'],
    package_data={'db': ['fishbase/db/*']},
    include_package_data=True,

    # packages=['fishbase', 'fishbase.naive_bayes'],
    # package_data={'': ['stopwords.txt']},

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]

)
