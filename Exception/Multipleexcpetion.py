try:
    num1,num2=eval(input("Enter any two numbers-"))
    result=num1/num2
    print("Answer-",result)
except ZeroDivisionError:
    print("Division by zero is an error")
except SyntaxError:
    print("Comma is missing enter the numbers like 1,2 ")
except :
    print("Wrong input")
finally :
    print("This will excecute no matter what")
    