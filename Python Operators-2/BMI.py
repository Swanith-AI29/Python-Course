Weight=int(input("Enter your weight-"))
Height=int(input("Enter your height-"))
BMI=Weight/(Height/100)**2
print("BMI=",BMI)
if BMI<=18.5:
    print("underweight")
elif BMI>=18.5 and BMI<=24.9:
    print("Healthy")
elif BMI>=24.9 and BMI<=29.9:
    print("Overweight")
elif BMI>=30.0:
    print("Obese")
else:
    print("invalid input")
    