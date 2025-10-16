from abc import ABC,abstractmethod
class absclass(ABC):
    def print(self,x):
        print('Passed value',x)
    def task(self):
        print('We are inside the abs class')
class testclass(absclass):
    def task(self):
        print('We are inside testclass')

testobj=testclass()
testobj.task()
testobj.print(99)


