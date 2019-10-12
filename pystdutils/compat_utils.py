#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/10/12
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)

import six


def ensure_unicode(s):
    return six.ensure_text(s)


def ensure_bytes(u):
    return six.ensure_binary(u)


def is_py2():
    return six.PY2


def is_py3():
    return six.PY3
