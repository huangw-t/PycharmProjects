# coding=utf-8
__author__ = 'huangw-d'


def combine(parameter):
    print parameter + external


external = 'berry'
print combine('Super')


# 可以使用Globals()函数来获取全局变量的值
def combine1(parameter):
    print parameter + globals()["parameter"]


parameter = 'Shit'
print combine1("SupperMen ")

x = 1


def change_global():
    global x  # 指定变量x为全局变量
    x = x + 1


change_global()
print x


# 闭包,函数本身被返回了，并没有被调用，返回的函数还可以访问它定义的所在的作用域
def multiplier(factor):
    def multiplyByFactor(number):
        return factor * number

    return multiplyByFactor


double = multiplier(2)
print double(5)
triple = multiplier(3)
print triple(3)
print multiplier(5)(4)
