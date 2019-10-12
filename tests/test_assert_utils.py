#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/10/12
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)

import pytest

from pystdutils.assert_uitls import assert_true, AssertFailedException, assert_value_not_none, assert_values_not_none


def func1(a, b, c):
    assert_true((a is not None and (b is not None) and (c > 10)),
                'a={},b={},c={}'.format(a, b, c))


def test_assert_true():
    with pytest.raises((AssertFailedException,), ):
        func1(1, None, 1)


def test_assert_value_not_none():
    def func2(a, b, c):
        assert_value_not_none(a, 'args: {}'.format([a, b, c]))

    with pytest.raises(AssertFailedException, ):
        func2(None, 1, 1)

    def func3(a, b, c):
        assert_values_not_none([a, b, c], 'args: {}'.format([a, b, c]))

    with pytest.raises(AssertFailedException, ):
        func3(1, 1, None)
