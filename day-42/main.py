pokemon = {"Name": None, "Type": None, "Move": None,}

print("PokeMon")

for key, value in pokemon.items():
    pokemon[key] = input(f"{key}:\t").strip().title()

if(pokemon["Type"] == "Earth"):
    print("\033[32m", end="")
elif pokemon["Type"] == "Air":
    print("\033[37m", end="")
elif pokemon["Type"] == "Fire":
    print("\033[31m", end="")
elif pokemon["Type"] == "Water":
    print("\033[34", end="")
else:
    print("\033[33", end="")
    
print()
for key, value in pokemon.items():
    print(f"{key:<15}: {value}")

print("\033[0m", end="")