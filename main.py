import os, time
toDoList = []

def printList():
  print()
  for todoItems in toDoList:
    print(todoItems)
  print()

while True:
  menu = input("ToDo List Manager\nDo you want to view, add, edit, remove or delete the todo list?\n")
  if menu=="view":
    printList()
  elif menu=="add":
    todoItem = input("What do you want to add?\n").title()
    toDoList.append(todoItem)
  elif menu=="remove":
    todoItem = input("What do you want to remove?\n").title()
    check = input("Are you sure you want to remove this?\n")
    if check[0]=="y":
      if todoItem in toDoList:
        toDoList.remove(todoItem)
    else:
      print("item not deleted")
  elif menu=="edit":
    todoItem = input("What do you want to edit?\n").title()
    edited = input("What do you want to change it to?\n").title()
    for i in range(0,len(toDoList)):
      if toDoList[i]== todoItem:
        toDoList[i]=edited
  elif menu=="delete":
    toDoList = []
  time.sleep(1)
  os.system('clear')