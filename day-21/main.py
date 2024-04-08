print()
print("Math Game!")
print()
print("How well do you know your math facts? Choose a number and I will give you 10 math facts to solve.")
print()

number = int(input("Choose a number which is you want to play: "))
count = 0

for i in range(1, 11):
    print()
    print(i, "x", number, "=")
    user_input = int(input("> "))
    answer = i*number
    if(user_input == answer):
        count += 1
        print("Great work! 😄")
    else:
        print(f"Nope 🙂! The answer was {answer}")

print()
if(count == 10):
    print("Great! You have done awesome! 🎉")
else:
    print("You scored {0} out of 10".format(count))