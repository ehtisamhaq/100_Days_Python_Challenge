# def rollDice():
#     import random
#     dice = random.randint(1, 6)
#     print("You rolled", dice)

# for i in range(10):
#     rollDice()


def login():
  while True:
    username = input("What is user username? ")
    password = input("What is your password? ")

    print("")
    if username == "ehtisam" and password == "Test@123":
        print("Login successful!")
        break
    else:
        print("Oops!, something went wrong! please try again.")
        continue

print("Awesome Login System")
login()
