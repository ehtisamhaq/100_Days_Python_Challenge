import random

print("""EPIC BATTLE     🪨     🗞️     ✂️""")

userMove = input("Select your move (R or P or S): ")

computerMove = random.choice(["R", "P", "S"])

print(f"User move: {userMove} & Computer move: {computerMove}")

if userMove == computerMove :
    print("Both you are same. Draw!")
elif userMove == "R":
    if computerMove == "P" :
        print(f"You are lose! {computerMove} covers {userMove}.")
    else:
        print(f"You win! {userMove} smashes {computerMove}")
elif userMove == "P":
    if computerMove == "S" :
        print(f"You lose! {computerMove} cuts {userMove}.")
    else:
        print(f"You win! {userMove} covers {computerMove}.")
elif userMove == "S":
    if computerMove == "R" :
        print(f"You lose! {computerMove} smashes {userMove}.")
    else:
        print (f"You win! {userMove} cuts {computerMove}.")
else:
    print("You have choose wrong move! please choose (R or P or S)")