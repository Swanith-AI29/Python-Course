notes=int(input("Enter The Money You Have"))
#calculating the denomination
note100=notes//100
note50=(notes%100)//50
note10=((notes%100)%50)//10
print("Amount-",notes)
print("notes of 100 rupees",note100)
print("notes of 50 rupees ",note50)
print("notes of 10 rupees ",note10)