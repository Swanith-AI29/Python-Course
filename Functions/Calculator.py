def Add(num1,num2):
    return num1+num2
def Subtraction(num1,num2):
    return num2-num1
def Multiply(num1,num2):
    return num1*num2
def Division(num1,num2):
    return num2/num1
print("Pick your operation-")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Division")
Choice=(input("Enter your choice-"))
num1=int(input("Enter first number-"))
num2=int(input("Enter your second number-"))
if Choice=="1":
    print("Answer of addition-",Add(num1,num2))
elif Choice=="2":
    print("Answer of subtraction-",Subtraction(num1,num2))
elif Choice=="3":
    print("Answer of Multiplication-",Multiply(num1,num2))
elif Choice=="4":
    print("Answer of division-",Division(num1,num2))
else:
    print("Invalid input")
