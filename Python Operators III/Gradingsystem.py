mathsMarks=int(input("Enter your maths marks-"))
englishMarks=int(input("Enter your english marks-"))
ScienceMarks=int(input("Enter your Science marks-"))
SocialMarks=int(input("Enter your Social marks-"))
computerMarks=int(input("Enter your omputer marks-"))
Average=(mathsMarks+englishMarks+ScienceMarks+SocialMarks+computerMarks)/5
if Average>91 and Average<100:
    print("Grade=A")
elif  Average>81 and Average<90:
    print("Grade=B")
elif Average>71 and Average<80:
    print("Grade=C")
elif Average>61 and Average<70:
    print("Grade=D")
elif Average>51 and Average<60:
    print("Grade=E")
else :
    print("Fail")