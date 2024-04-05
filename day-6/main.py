print("Test Fruits")

fav_fruit= input("You favorite fruit name? ")

if(fav_fruit=="Mango"):
    print("Mango is very delicious")
elif(fav_fruit == "Banana"):
    print("Banana is very testy")
else:
    print("I haven't tested yet!")


# programming check
print("Check your skill")

python= input("Do you know Python?")
javascript= input("Do you know Javascript?")

if python=="Y" and javascript=="Y":
    print("You are a very good Programmer")
elif python=="Y" or javascript =="Y"  :
    print("You will be a good programmer in future!")