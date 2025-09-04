num1=[1,2,3]
num2=[4,5,6]
result=map(lambda x,y:x+y,num1,num2)
print('Addition of two lists')
print(list(result))

numbers=[1,2,3,4,5]
def square(n):
    return n*n
square=list(map(square,numbers))
print(square)