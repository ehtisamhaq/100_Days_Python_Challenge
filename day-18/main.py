print("One Million To One")

correct = 500000
guessCount = 0

while True:
    guess = int(input("What is your guess? "))
    guessCount += 1
    if guess > correct:
        print("Too high")
    elif guess < correct:
        print("Too low")
    elif guess == correct:
        print("Correct!") 
        break
    else: continue
print(f"It took you {guessCount} guesses to get it correct")