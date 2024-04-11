import os, time

todoItem = []

def printTodoItem ():
    print()
    for index in range(len(todoItem)):
        print(f"{index}: {todoItem[index]}")
    time.sleep(1)


while True:
    print("TODO LIST")
    menu = input("1: Add item\n2: Remove item\n3: Show items\n4: Get SPAMMING\n> ")

    if menu == "1":
        item = input("Item > ")
        todoItem.append(item)
    elif menu == "2":
        item = input("Item > ")
        if item in todoItem:
            todoItem.remove(item)
    elif menu == "3":
        printTodoItem()
    elif menu == "4":
        print("will develop")
    time.sleep(1)
    os.system("cls")