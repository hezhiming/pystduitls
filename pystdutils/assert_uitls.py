#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/10/12
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)

from .python_utils import is_not_empty


class AssertFailedException(Exception):
    pass


def assert_true(true_value, context_err_str):
    """断言为true

    :type true_value: bool
    :param true_value:
    :param context_err_str:
    :return:
    """
    if true_value is False:
        raise AssertFailedException("assert failed! context: {}".format(context_err_str))


def assert_value_not_none(value, context_err_str):
    """某值不为None

    :param value:
    :param context_err_str:
    :return:
    """
    assert_true(value is not None, context_err_str)


def assert_values_not_none(values, context_err_str):
    """某一系列值,都不为None

    :param values:
    :param context_err_str:
    :return:
    """

    for value in values:
        assert_value_not_none(value, context_err_str)


def assert_value_not_empty(value, context_err_str):
    """某值,不为空值

    :param value:
    :param context_err_str:
    :return:
    """
    assert_true(is_not_empty(value), context_err_str)


def assert_values_not_empty(values, context_err_str):
    """某一系列值,都不为空值

    :param values:
    :param context_err_str:
    :return:
    """
    for value in values:
        assert_value_not_empty(value, context_err_str)
