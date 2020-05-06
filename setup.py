#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-django-cache-xdist',
    version='0.1.0',
    author='Anton Tuchak',
    author_email='anton.tuchak@gmail.com',
    maintainer='Anton Tuchak',
    maintainer_email='anton.tuchak@gmail.com',
    license='BSD-3',
    url='https://github.com/atuchak/pytest-django-cache-xdist',
    description='A djangocachexdist plugin for pytest',
    long_description=read('README.rst'),
    py_modules=['pytest_django_cache_xdist'],
    python_requires='>=3.4',
    install_requires=['pytest>=3.5.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
    ],
    entry_points={
        'pytest11': ['djangocachexdist = pytest_django_cache_xdist']
    },
    project_urls={
        'Source': 'https://github.com/atuchak/pytest-django-cache-xdist',
    },
)
