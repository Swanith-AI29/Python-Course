Age=int(input("Give me your age"))
if Age<18:
    if Age<=12 and Age>=1:
        print("You are a kid")
    elif Age>=13 and Age<=18:
        print("You are a teenager")
else:
    print("You are an adult")