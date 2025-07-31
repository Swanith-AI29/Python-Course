def Add(num1,num2):
    return num1+num2
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