import random

letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
        'o','p','q','r','s','t','u','v','w','x','y','z','A','B',
        'C','D','E','F','G','H','I','J','K','L','M','N','O','P',
        'Q','R','S','T','U','V','W','X','Y','Z']
number=['0','1','2','3','4','5','6','7','8','9']
sign=['@','!','#','$','%','^','&','*']


print("WELCOME TO PASSWORD GENERATOR!!!!!!")
print("Try yourself to have secure password")

my_letter=int(input("How many letters would you like to use in your password?\n"))
my_number=int(input("How many number would you like to use in your password?\n"))
my_sign=int(input("How many sign would you like to use in your password?\n"))


password=[]

for char in range(1,my_letter+1):
    password.append(random.choice(letter))

for char in range(1,my_number+1):
    password+=random.choice(number)

for char in range(1,my_sign+1):
    password+=random.choice(sign)

random.shuffle(password)

password_lst=""
for char in password:
    password_lst+=char
print(f"Your password is : {password_lst}")

  