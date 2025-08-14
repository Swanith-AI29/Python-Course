try:
    age=int(input("Enter your age-"))
    if age/2==0:
        print("It is an even number.")
    else:
        print("It is an odd number.")
except:
    print("Invalid input . Try to input an number other thn 0.")