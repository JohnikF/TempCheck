#temp = int(input("What is the current temperature? "))
temp = 5
if temp <= 0:
    print("Its VERY cold")

elif 0 < temp <= 12:
    print("its cold")

elif 12 < temp <= 18:
    print("its chilly outside ")

elif 18 < temp <= 25:
    print("its warm outside")

elif 25 < temp <= 32:
    print("its hot outside")

elif temp > 32:
    print("Its VERY HOT outside")


money = True
seats = False
if money == True and seats == True:
    print("you can go inside the theater")
else:
    print("You cant go inside the theater")

age = 3
parents = True
if age >= 12 or parents == True:
    print("You can go inside the theater")
else:
    print("You cant go inside the theater")