number = int(input("Enter a number: "))
if number > 5:
    print("This number > 5")
else:
    print("Number < 5")


name = input("Enter you name: ")

if name == "Alex":
    print("You have entered", name)
    print("This is my name, too.")
else:
    print("You not Alex")

x = int(input(" x = "))
if 0 < x < 7:
    print("значение")
    y = 2 * x - 5
    if y < 0:
        print("negative")
    elif y > 0:
            print("positive")
    else: 
            print("y = 0")

print("""
1. file
2. View
3. Exit
""")
choise = input("Enter you choise: ")
if choise == "1":
    print("You have selected 'File' menu")
elif choise == "2":
    print("You have selected 'View' menu")
elif choise == "3":
    print("Stoping.")
else:
    print("Incorected choise")