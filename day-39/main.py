word = "Hello"
life = len(word)
guessedLetters = []

while life > 0:
  guessedLetter = input("Guess a letter \n> ")
  if guessedLetter in guessedLetters:
     print("You have already tried that before!")
     continue
  elif guessedLetter.lower().strip() in word.lower():
      # index = print(word.lower().index(guessedLetter.lower().strip()))
      guessedLetters.append(guessedLetter)

      print(f"You are correct!")

      for i in word.lower():
        if i in guessedLetters:
          print(i, end="")
        else:
          print("_", end="")
      print()
  else:
      life -= 1
      print(f"Nope, not in there. you have {life} life")