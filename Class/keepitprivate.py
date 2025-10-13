class myclass:
    __privatevariable=27;
    def __privatemethod(self):
        print('I am inside the class.')
    def hello(self):
        print('Private variable value is',myclass.__privatevariable)

object1=myclass()
object1.hello()
object1.__privatemethod()
