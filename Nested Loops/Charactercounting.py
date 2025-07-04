a=str(input("Enter the word"))
char=input("Please enter your own charcter")
i=0
count=0
while(i<len(a)):
    if(a[i] == char):
        count=count+1
    i=i+1
print("The total number of times",char,"Has occured=",count)