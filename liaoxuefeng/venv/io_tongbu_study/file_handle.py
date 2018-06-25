#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@project=liaoxuefeng
@file=file_handle
@author=book
@create_time=18-6-21 下午3:05
"""
# 写文件操作
fpath = r'/home/book/PycharmProjects/liaoxuefeng/venv/io_tongbu_study/yi.txt'
# 以'w'模式写入文件时，如果文件已存在，会直接覆盖
f = open(fpath, 'w')
f.write('hello,world!')
f.close()

# 追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入
# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法
with open(fpath, 'a') as f:
	f.write('nihaoma!')

# 读文件操作
"""""
如果文件很小，read()一次性读取最方便；
如果不能确定文件大小，反复调用read(size)比较保险；
如果是配置文件，调用readlines()最方便：
"""
f = open(fpath, 'r')
s = f.read()
f.close()
print(s)


""""
file-like Object

像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，
还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。
StringIO就是在内存中创建的file-like Object，常用作临时缓冲。
"""
"""
二进制文件
前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。
要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
"""
f = open(fpath, 'rb')
s = f.read()
f.close()
print(s)


"""
字符编码

要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：

>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
>>> f.read()
'测试'

遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：

>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

"""