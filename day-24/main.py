def login(username, password):
    print("")
    if username == "ehtisam" and password == "Test@123":
        print("Login successful!")
        return True
    else:
        print("Oops!, something went wrong! please try again.")
        return False


print("Awesome Login System")
while True:
    username = input("What is user username? ")
    password = input("What is your password? ")

    result = login(username, password)
    if result: break
