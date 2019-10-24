#цикл while

response = ""
while response != "exit":
    response = input("Type 'exit' to exit: \n")

n = 1 
while n <=3: 
    print("n =", n)
    n += 1

number = 0
while number <= 0:
    number =  int(input("Enter a positive integer: "))
print("You have entered", number)

print("All natural numbers:")
n = 1
while True:
    print(n)
    n += 1

#Операторы break and continue

while True:
    print("Enter 'exit' to exit loop")
    response = input("> ")
    if response == "exit":
        break
print("Loop has stopped.")

name = None
while True:
    print("Menu:")
    print("1. Enter name")
    print("2. Print greeting")
    print("3. Quit")
    response = input("Please choose an action: ")
    print()
    if response == "1":
        name =  input("Enter you name: ")
    elif response == "2":
        if name:
            print("Hello, ", name, "!", sep="")
        else:
            print("I dont know your name.")
    elif response == "3":
        break
    else:
        print("Incorrect input")
    print()

number = 0
while number < 10:
    number += 1
    if number == 5:
        continue
    print("Current number is", number)

retries_left = 3
while retries_left > 0:
    retries_left -= 1
    password = input("Enter your password: "
    "(you have {} retries_left): ".format(retries_left + 1))
    if password == "1111":
        print("Welcome: access successful!")
        break
else:
    print("Access denied!")

Цикл for

for test in range(10):
    print("test =", test)

for test in range(10):
    print("test =", test)
    if test == 8:
        break

#Вложеные циклы
for row in range(5):
    for column in range(30):
        print("*", end="")
    print()