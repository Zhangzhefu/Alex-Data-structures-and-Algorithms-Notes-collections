"""Encapsulation is the process of making methods and data hidden inside the
 object they relate to. Languages accomplish this with what are called
 access modifiers like"""


class Employee():
    def __init__(self):
        self.id = None
        self._id = 4
        self.__id = 7

e = Employee()
print(dir(e))
