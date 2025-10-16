class student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def display(self):
        print("Name:", self.__name)
        print("Age:", self.__age)
result = student('Swanith', 12)
result.display()
