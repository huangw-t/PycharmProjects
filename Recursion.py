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


# 二分法查找
def search(sequence, number, lower=0, upper=None):
    if upper is None:
        upper = len(sequence) - 1
    if lower == upper:
        # assert语句用来判断某个条件是否为真，为假时会引发AssertionError异常
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)


seq = [34, 67, 8, 123, 5, 100, 98]
seq.sort()
print seq
print search(seq, 34, 0, 7)
