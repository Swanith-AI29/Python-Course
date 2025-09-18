import random
try:
    name = str(input("Enter your name: "))
    birth = int(input("Enter your birth year (YYYY): "))
    lucky =int(input("Enter your lucky number: "))
except ValueError:
    print('Please enter numeric values to birth date,lucky number.')
symbols = ['!', '@', '#', '$', '%', '&', '*']
password = (
    name[:2].capitalize() + str(birth)[-2:] +              
    str(lucky) +                   
    random.choice(symbols) +  
    str(random.randint(10,99))
)
    
print("Your strong password is:", password)
