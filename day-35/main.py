import os, time

todoItem = []

def printTodoItem ():
    print()
    for index in range(len(todoItem)):
        print(f"{index}: {todoItem[index]}")
    time.sleep(1)


while True:
    print("TODO LIST")
    menu = input("1: Add item\n2: Remove item\n3: Edit item\n4: Delete items\n5: Show items> ")

    if menu == "1":
        item = input("Item > ").strip().capitalize()
        if item not in todoItem:
            todoItem.append(item)
    elif menu == "2":
        item = input("Item > ").strip().capitalize()
        check = input("Are you sure you want to remove this?\n")
        if check[0]=="y":
            if item in todoItem:
                todoItem.remove(item)
    elif menu == "3":
        item = input("What do you want to edit?\n").strip().capitalize()
        new = input("What do you want to change it to?\n").strip().capitalize()
        for i in range(0,len(todoItem)):
            if todoItem[i]==item:
                todoItem[i]=new
    elif menu == "4":
       todoItem = []
    elif menu == "5":
       printTodoItem()
    time.sleep(1)
    os.system("cls")