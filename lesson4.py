#>,<, ==, <=, >=, !=

#logiceskie operatori

#or , and , not

#print(7 > 5 and 7 < 8 and 7 == 7 and 8 > 6)  # ++
#print(7 > 7 and 7 < 8)   # --

#print("hello" + name)

#print(7 == 6 or 4 !=4 or 8 > 6)

#print(8 > 6 and 7 != 7 or 8 < 10)

#print(not 1)    # da net

#print(not(7 < 4))   # exz

#dog = int(input("type your dog power: "))
#cat = int(input("type your cat power:"))

#print("cat stronger then dog ?:" , dog >< cat)  # exz
# ysloviya

# if, elif, else

#if 4 < 5:
#    print("hello")

#age = int( input(" type your age: "))

#if age > 0 and age <= 12:
    #print("you yet child")
#elif age > 13 and age <= 18:
    #print("you teenage")
#elif age > 19 and age <= 65:
   # print("you human")
#else:
  #  print("time to grand")

from random import randint

#print(randint(0 , 20)
#num_1 = randint(0, 20)
#num_2 = int(input("type the your number"))

#print(("мое число больше?", num_1 < num_2))
#print(f"мое число {num_2} равно {num_1}?", num_1 == num_2)

login = input(" type your role:")
password = input("type your password:")

correct_password = "apple" # lower(all)

if login == "admin":
#    password = input(t y pass)
   if password == correct_password:
       print("hello admin")
   else:
       print("wrong password")
elif login == "user":
    password = input(" t y pass")
else:
   print("access denied")





num_1 = int(input('type 1st num:'))
num_2 = int(input('type 2nd num:'))
operand = input('type youe operaand:')

