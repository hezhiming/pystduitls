#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/10/12
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)

import setuptools
from setuptools import setup

_CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3.6",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
]

setup(
    name="pystdutils",
    version="0.1",

    platforms="any",
    url="https://github.com/hezhiming/pystduitls",
    license="MIT",
    author="he.zhiming",
    author_email="he.zhiming@foxmail.com",
    description="Python Utils for Python2 and Python3",
    long_description='Python Utils for Python2 and Python3',

    keywords="Python Utils",

    packages=setuptools.find_packages(exclude=['./tests']),
    tests_require=['pytest'],
    classifiers=_CLASSIFIERS
)
