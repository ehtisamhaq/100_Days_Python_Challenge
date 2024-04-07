# print("Teen times table")
# for i in range(1, 1002, 25):
#     print(i, "x 10 = ", i*10)

# for i in range(100, -1, -3):
#     print(i)

print("Welcome to my number list generator.")
print()
print("You are going to give me a number you want to start with, an ending number, and by how many you want me to add each time.")
print()

x = int(input("What number do you want to start with? "))
y = int(input("What number do you want to end with? "))
z = int(input("How many should I add each time? "))

for i in range(x, y, z):
  print(i) 