def print_numbers(limit):
    for i in range(limit):
        print(i)
n = int(input("n = "))
print_numbers(n)

def hello():
    print("Hello World!")
    print("this text gets printed from a function")
    print()
hello()
hello()

def print_info(object_name, color, price):
    print('Object:', object_name)
    print('Color:', color)
    print('Price:', price)
print_info('pen', 'blue', 1)
print_info(price=5, object_name='coffe', color='black')

ssh remoteuser@remoteserver