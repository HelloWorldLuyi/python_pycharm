#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@project=liaoxuefeng
@file=serialization
@author=book
@create_time=18-6-21 下午3:51
"""

"""
我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。

序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

Python提供了pickle模块来实现序列化。

Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。
"""

import  pickle

d = dict(name='Bob', age=20, score=88) # 定义一个dict
s = pickle.dumps(d) # 法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件
print(s)

# pickle.dump()直接把对象序列化后写入一个file-like Object
f = open('dump.txt', 'wb')# 应为返回的f对象拥有 read函数，所以属于file-like Object
pickle.dump(d,f)
f.close()

"""
当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，
然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
我们打开另一个Python命令行来反序列化刚才保存的对象：
"""
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)



"""
JSON

如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：
JSON类型 	Python类型
{} 			dict
[] 			list
"string" 	str
1234.56 	int或float
true/false 	True/False
null 	None

Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON：
"""
"""
Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON：
"""
import  json
d = dict(name='Bob', age=20, score=88)
f = json.dumps(d)
print(f)
"""
dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。

要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
"""
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
s = json.loads(json_str)
print(s)

# 由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换

"""
Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，
我们更喜欢用class表示对象，比如定义Student类，然后序列化：
"""
# 这里我没怎么看懂


class Student(object):

	def __init__(self):
		self.name = name
		self.age = age
		self.score = score
	# 这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON：

	def student2dict(self):
		return {
			'name': self.name,
			'age': self.age,
			'score': self.score
		}



	s = Student('Bobb', 20, 88)
	print(json.dumps(s, default=student2dict))