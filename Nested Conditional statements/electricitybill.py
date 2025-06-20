unit=float(input("Enter the number of unit consumed"))
if unit<50:
   bill=(unit*2.60)+25
   print("Bill-",bill)
elif unit>=50 and unit<=100:
   bill2=(130+((unit-50)*3.25))+35
   print("Bill-",bill2)
elif unit>=101 and unit<=200:
   bill3=(292.5((unit-100)*5.26))+45
   print("Bill-",bill3)
else:
   bill4=(130+162.50+526+((unit-200)*8.45))+75
   print("Bill-",bill4)