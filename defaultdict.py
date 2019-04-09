# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:30:13 2019

@author: jon
"""

from collections import defaultdict

lab_member = ['yanglei', 'songqinghua', 'liutong']
lab_dict = {}
for name in lab_member:
    #lab_dict[name] += 1
    if name not in lab_dict: # 如果字典中不存在这个key，则创建
        lab_dict[name] = 1
    else:
        lab_dict[name] += 1
print(lab_dict)

for name in lab_member:
    lab_dict[name] = lab_dict.setdefault(name, 0) + 1
print(lab_dict)

# defaultdict是一个类定义，test1是类的一个具体实例
s1_list = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
test_list = defaultdict(list)
for k,v in s1_list:
    test_list[k].append(v)
print(test_list.items())

s2 = 'philadelphia'
test_int = defaultdict(int)
for c in s2:
    test_int[c] += 1
print(test_int.items())

def fun():
    l = [1,2,3,4,5,6,7,8,9]
    e = 0
    for x in l:
        e += x
    print('haha, it is running : ', e)
    
# 可以将函数作为字典没有键值对应的默认值
test_func = defaultdict(fun)
print(test_func)
print(test_func.items())
print(test_func['abc'])
test_func['abc'] = 'hello'
print(test_func['abc'])
print(test_func)
