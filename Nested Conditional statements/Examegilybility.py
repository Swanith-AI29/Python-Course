Medicalcause=str(input("Do you have a Medical cause"))
Attendance=int(input("Give your atendance percentage"))
if Medicalcause.lower() == "yes":
    print("Allowed for exam")
else:
    if Attendance>=75:
        print("Allowed for exam")
    else:
        print("Not allowed for exam")