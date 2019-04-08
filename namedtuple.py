# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 18:14:54 2019

@author: jon
"""

import collections

# 创建一个类
Person = collections.namedtuple("Person", ["age", "height", "weight"])

# 产生tom这个对象
tom    = Person(age=12, height=150, weight=40)

# 产生jerry这个对象
jerry = Person._make(["10", "135", "30"])

info = {
        'age':9,
        'height':120,
        'weight':30
        }

jack = Person(**info)

print(tom.age, tom.height, tom.weight)
print(jerry.age, jerry.height, jerry.weight)
print(jack.age, jack.height, jack.weight)

# 修改属性
tom = tom._replace(age=11)
print(tom.age)

print(tom._asdict())