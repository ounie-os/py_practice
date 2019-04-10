# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 20:12:51 2019

@author: jon
"""

a = [5,9,1,3,0,4]
b = sorted(a)
print(b)
c = sorted(a, reverse=True)
print(c)

classmates = [('mary', 'A', 15), ('james', 'B', 13), ('mike', 'C', 9)]
# key参数为一个函数，它会作用到每一个元素上，之后，再进行排序
# 例如，下面的例子含义是，按照每个列表元素的第三个元素的排列顺序，对列表进行排序
d = sorted(classmates, key=lambda x: x[2])
print(d)