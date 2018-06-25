#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@project=liaoxuefeng
@file=classs_test
@author=book
@create_time=18-6-21 上午10:59
"""

from class_ly import Student

lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())
