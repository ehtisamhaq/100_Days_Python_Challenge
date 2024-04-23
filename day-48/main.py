# file = open("example.txt", "a+")
# whatText = input("> ")
# file.write(f"{whatText}\n")
# file.close()

import os, time

print("High Score Table")

while True:
    initials = input("Initials > ")
    score = input("Score > ")

    file = open("sore_board.txt", "a+")
    file.write(f"{initials} {score}\n")
    file.close()

    print("Added")
    time.sleep(1)
    os.system("cls")