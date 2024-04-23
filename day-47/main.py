import random

trumps = {}
trumps["David"] = {"Intelligence": 178, "Speed": 4, "Guile": 80, "Baldness Level": 99}
trumps["Mr Spock"] = {"Intelligence": 200, "Speed": 50, "Guile": 50, "Baldness Level": 0}
trumps["Moica from Friends"] = {"Intelligence": 150, "Speed": 50, "Guile": 50, "Baldness Level": 0}
trumps["Professor X"] = {"Intelligence": 250, "Speed": 1, "Guile": 200, "Baldness Level": 101}






while True:
    print("TOP TRUMPS")
    print("--------------")
    print()

    print("Characters")
    print()

    for key in trumps:
        print(key)

    print()
    user = input("Pick your Character\n> ")
    comp = random.choice(list(trumps.keys()))
    print("Computer Picked: ", comp)

    answer = input("Choose your stat: Intelligence, Speed, Guile or Baldness Level\n> ")

    print(f"{user}: {trumps[user][answer]}")
    print(f"{comp}: {trumps[comp][answer]}")

    if(trumps[user][answer]> trumps[comp][answer]):
        print(user, "wins")
    elif trumps[user][answer] < trumps[comp][answer]:
        print(comp, "wins")
    else:
        print( "draw")

