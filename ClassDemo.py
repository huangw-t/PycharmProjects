# coding=utf-8
__author__ = 'huangw-d'
__metaclass__ = type  # 确定使用新式类


class Person:
    def setName(self, name):
        self.name = name

    def getName(self, name):
        return self.name

    def greet(self):
        print "Hello World! I'm %s." % self.name


foo = Person()
bar = Person()
foo.setName("Luke SKYwalker")
bar.setName("Mexi")
print foo.getName("Luke SKYwalker")
foo.greet()
print bar.getName("Mexi")
bar.greet()
