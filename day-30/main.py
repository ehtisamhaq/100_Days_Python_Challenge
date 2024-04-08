# name = "Katie"
# age = "28"
# pronouns = "she/her"

# print("This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far".format(name=name, pronouns=pronouns, age=age))


# response = f"This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far"

# print(response)

print("30 Days Down - What did you think?")
print()
for i in range(1, 31):
  thought = input(f"Day {i}:\n")
  print()
  myText = f"You thought Day {i} was"
  print(f"{myText:^35}")
  print(f"{thought:^35}")
  print()