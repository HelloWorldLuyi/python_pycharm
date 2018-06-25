#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@project=liaoxuefeng
@file=class_ly
@author=book
@create_time=18-6-21 上午10:58
"""

"""
由于类可以起到模板的作用，因此，可以在创建实例的时候，
把一些我们认为必须绑定的属性强制填写进去。
通过定义一个特殊的__init__方法，在创建实例的时候，
就把name，score等属性绑上去
注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，
就可以把各种属性绑定到self，因为self就指向创建的实例本身。

有了__init__方法，在创建实例的时候，就不能传入空的参数了，
必须传入与__init__方法匹配的参数，但self不需要传，
Python解释器自己会把实例变量传进去：
"""
class Student(object):

	def __init__(self, name, score):
		self.name = name
		self.score = score
	# 类的方法

	def print_score(self):
		print('%s: %s' % (self.name, self.score))

	def get_grade(self):
		if self.score >= 90:
			return'A'
		elif self.score >= 60:
			return'B'
		else:
			return'C'


lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())


# 访问限制

"""在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。

但是，从前面Student类的定义来看，外部代码还是可以自由地修改一个实例的name、score属性：

>>> bart = Student('Bart Simpson', 59)
>>> bart.score
59
>>> bart.score = 99
>>> bart.score
99

如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），
只有内部可以访问，外部不能访问，所以，我们把Student类改一改：
"""
class Student2(object):

	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def print_score(self):
		print('%s:%s' % (self.__name, self.__score))

	def get_name(self):
		return self.__name

	def get_score(self):
		return  self.__score

	def set_score(self,score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')


bart = Student2('bartnihao', 59)
s = bart.get_name()
print(s)

# 继承和多态 以及获取对象信息
# 这里看教程


# 实列属性和类属性

"""
实列属性
实例绑定属性的方法是通过实例变量，或者通过self变量
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

"""

"""
但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：

class Student(object):
    name = 'Student'

当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。来测试一下：

>>> class Student(object):
...     name = 'Student'
...
>>> s = Student() # 创建实例s
>>> print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
Student
>>> print(Student.name) # 打印类的name属性
Student
>>> s.name = 'Michael' # 给实例绑定name属性
>>> print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
Michael
>>> print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
Student
>>> del s.name # 如果删除实例的name属性
>>> print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
Student

从上面的例子可以看出，在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
"""
"""
小结

实例属性属于各个实例所有，互不干扰；

类属性属于类所有，所有实例共享一个属性；

不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
"""