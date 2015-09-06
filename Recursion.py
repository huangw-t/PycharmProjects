# coding=utf-8
__author__ = 'huangw-d'

#递归算法
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print factorial(1)
print factorial(3)

def power(x, n):
   if n == 1:
       return 1
   else:
       return x * power(x, n-1)
