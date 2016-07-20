# -*- coding: utf-8 -*-

import re
import os

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)

setup(
    name='django-hesab',
    version=get_version('hesab'),
    description='Customizable Elasticsearch backend for django-haystack',
    long_description='Makes the Haystack Elasticsearch backend configurable through django settings file',
    author='Rolf Håvard Blindheim',
    author_email='rhblind@gmail.com',
    url='https://github.com/rhblind/django-hesab',
    download_url='https://github.com/rhblind/django-hesab.git',
    license='MIT License',
    packages=[
        'hesab',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.8.0',
        'django-haystack>=2.5.dev1',
        'elasticsearch<2.0.0'
    ],
    tests_require=[
        'nose',
        'coverage',
        'unittest2',
    ],
    zip_safe=False,
    test_suite='tests.runtests.start',
    classifiers=[
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
