#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@project=liaoxuefeng
@file=function_ly
@author=book
@create_time=18-6-21 上午10:53
"""

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x