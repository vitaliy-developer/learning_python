for x in range(0, 5):
    print('привет %s' % x)

wizard_list = ['паучьи лапки', 'жабий палец', 'язык улитки', 'крыло летучей мыши', 'жир слизня', 'медвежий коготь']
for mynumber in wizard_list:
    print(mynumber)

hugehairypants = ['огромные', 'волосатые', 'штаны']
for i in hugehairypants:
    print(i)
    for j in hugehairypants:
        print(j)

found_coins = 20
magic_coins = 70
stolen_coins = 3
coins = found_coins
for week in range(1, 53):
    coins = coins + magic_coins - stolen_coins
    print('Неделя %s = %s' % (week, coins))

x = 45
y = 80
while x < 50 and y < 100:
    x = x + 1
    y = y + 1
    print(x, y)
x = 25

for x in range(0, 20):
    print('привет %s' % x)
    if x < 9:
        break

x = 0
while x < 25:
    x = x + 5
    print(x)

ingredients = ['snails', 'leeches', 'gorilla belly-button lint','caterpillar eyebrows', 'centipede toes']
x = 1
for i in ingredients:
    print('%s %s' % (x, i))
    x = x + 1

fname = 111
lname = 222
def testfunc(fname, lname):
    print('Привет, %s %s' % (fname, lname))

firstname = 'Джо'
lastname = 'Робертсон'
def testfunc(firstname, lastname):
    print('Привет, %s %s' % (firstname, lastname))


def variable_test():
    first_variable = 10
    second_variable = 20
    return first_variable * second_variable
print(variable_test())
