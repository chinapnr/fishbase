# from distutils.core import setup
from setuptools import setup

setup(
    name='fish_base',
    version='1.0.10',
    install_requires=['python-dateutil'],

    url='https://github.com/chinapnr/fish_base',
    license='MIT',
    author='david.yi',
    author_email='wingfish@gmail.com',
    description='some useful functions for python',

    packages=['fish_base'],

    # packages=['fish_base', 'fish_base.naive_bayes'],
    # package_data={'': ['stopwords.txt']},

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]

)
