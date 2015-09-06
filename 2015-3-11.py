__author__ = 'huangw-d'


class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]  # Split string on blanks

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)  # update pay in-place


bob = Worker('Bob Smith', 50000)
sue = Worker('Sue Jones', 60000)
print(bob.lastName())
print(sue.lastName())
sue.giveRaise(.10)
print(sue.pay)
