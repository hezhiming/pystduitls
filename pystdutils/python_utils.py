#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/10/12
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)


def is_none(value):
    return value is None


def is_not_none(value):
    return not is_none(value)


def is_empty(value):
    if not value:
        return True
    else:
        return False


def is_not_empty(value):
    return not is_empty(value)
