# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 09:34:07 2019

@author: jon
"""

# method 1
g = (x*x for x in range(1,10))
for n in g:
    print(n)

# method 2
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(6)
for x in f:
    print(x)

# or do it like this
for x in fib(6):
    print(x)
    
# or to get return value, we should catch the exception
z = fib(6)
while True:
    try:
        j = next(z)
        print("z:", j)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
    
# pratice 杨辉三角
def triangles():
    a = [1]
    while True:
        yield a
        a = [1] + [a[i] + a[i+1] for i in range(len(a)-1)] + [1]
        
t = triangles()
for z in range(10):
    print(next(t))

          
