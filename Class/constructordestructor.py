class employee():
    def __init__(self):
        print('Employee created.')
    def __del__(self):
        print('Destructor called.')
def createobject():
    print('Making mobjects')
    obj=employee()
    print('Function end')
    return obj

print('Calling create object function')
obj=createobject()
print('Program end')
