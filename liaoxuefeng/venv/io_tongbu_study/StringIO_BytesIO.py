#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@project=liaoxuefeng
@file=StringIO_BytesIO
@author=book
@create_time=18-6-21 下午3:26
"""
# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
"""
很多时候，数据读写不一定是文件，也可以在内存中读写。
StringIO顾名思义就是在内存中读写str。
StringIO操作的只能是str
"""
# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：
from io import StringIO
f = StringIO()
f.write('hello')
f.write('world')
print(f.getvalue()) # getvalue()方法用于获得写入后的str。


# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：

s = StringIO('what are you from ')
while True:
	m = s.readline()
	if m == '':
		break
	print(m.strip())


"""
要操作二进制数据，就需要使用BytesIO。

BytesIO实现了在内存中读写bytes
"""

from io import  BytesIO
f = BytesIO()
f.write('中国'.encode('utf-8'))
print(f.getvalue())


l = BytesIO(b'\xe4\xb8\xad')
m = l.read()
print(m)
