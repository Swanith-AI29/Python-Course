Ride=str(input("Which type of transportation do you need?\n1.Bike \n2.Car\nEnter your choice:"))
if Ride=="Bike":
    print("What type of Vehicle you want")
    print("1.Scooty\n2.Motorbike")
    Choice=str(input("Enter your choice:"))
    if Choice=="Scooty":
        print("Enjoy your ride wuth the scooty")
    else:
        print("Enjoy your ride with the Motorbike")
elif Ride=="Car":
    print("What type of car do you need")
    print("1.Sedan\n2.SUV")
    Choice2=str(input("Enter your choice:"))
    if Choice2=="Sedan":
        print("Enjoy your ride with Sedan")
    else:
        print("Enjoy your ride with SUV")
else:
    print("invalid input")