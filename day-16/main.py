# while True:
#   print("This program is running")
#   goAgain = input("Go again?: ")
#   if goAgain == "no":
#     break
# print("Aww, I was having a good time 😭")

# while True:
#   color = input("Enter a color: ")
#   if color == "red":
#     break
#   else:
#     print("Cool color!")
# print("This is very dangerous color!")

attempts = 0
while True:
    print("""Fill-in the blank Lyrics!
          (type in the blank lyrics, see if you're as coll as me)""")
    u_input = input("Never going to ___ you up: ")
    attempts += 1
    if u_input == "give":
        break
print("Well done, it only took {0} attempts!".format(attempts))

