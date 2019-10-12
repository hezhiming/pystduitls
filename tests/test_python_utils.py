#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/10/12
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)
from pystdutils.python_utils import is_none, is_empty

import pytest


@pytest.mark.parametrize(
    ['value', 'expected'],

    [
        [None, True],
        [0, False],
        ['', False],
        [0.0, False],

    ]
)
def test_is_none(value, expected):
    assert is_none(value) == expected


@pytest.mark.parametrize(
    ['value', "expected"],

    [
        [None, True],
        [0, True],
        ['', True],
        [0.00, True],
        [False, True],
        [[], True],
        [set(), True],
        [dict(), True],

        [1, False]
    ]
)
def test_is_empty(value, expected):
    assert is_empty(value) == expected
