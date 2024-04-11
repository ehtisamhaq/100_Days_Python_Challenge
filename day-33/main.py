todoItem = []

def printTodoItem ():
    print("")
    for item in todoItem:
        print(item, "\t")
    print("")


while True:
    menu = input("Add or Remove? ")

    if menu == "add":
        item = input("What's item in your bucket? ")
        todoItem.append(item)
    elif menu == "remove":
        item = input("What's item you want to remove? ")
        if item in todoItem:
            todoItem.remove(item)
        else:
            print(f"{item} is not in the list")

    printTodoItem()
