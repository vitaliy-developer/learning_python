fred = """Почему у горилл большие ноздри? Потому что у них толстые пальцы!
Что это: розовое и пушистое? Розовый пушистик!
"Тут что-то не так,
не будь я д'Артаньян", — подумал он."""
print(fred)
double_quote_str = "\"Тут что-то не так, не будь я д'Артаньян\", - подумал он."
print(double_quote_str)

myscore = 1050
message = 'Мой счет: %s очков'
print(message % myscore)

joke_text = '%s: приспособление для поиска мебели в темноте'
bodypart1 = 'Коленка'
print(joke_text % bodypart1)

var1 = """%s: loves BABLO :)"""
var2 = "Alex"
var3 = "Alex2"
var4 = "Alex3"
print(var1 % var4)

nums = 'Что сказало число %s числу %s? Славный поясок!'
print(nums % (0, 8))

spaces = ' ' * 10
print('%s Задний переулок 12' % spaces)

wizard_list = ['паучьи лапки', 'жабий палец', 'глаз тритона', 'крыло летучей мыши', 'жир слизня', 'перхоть змеи']
wizard_list.append('ты ПИДОР')
print(wizard_list)
del wizard_list[5]
print(wizard_list)

print(wizard_list[2])
wizard_list[2] = 'язык улитки'
print(wizard_list[2])


numbers_and_strings = [7, 'раз', 'отпей', 1, 'раз', 'отъешь']
print(numbers_and_strings)

numbers = [1, 2, 3, 4, 5]
strings = ['хватит', 'циферки', 'считать']
mylist = [numbers, strings]
print(mylist)

fibs = (0, 1, 45, 2, 3, 4,)
print(fibs[2])

favorite_sports = {'Ральф Уильямс': 'Футбол',
'Майкл Типпетт': 'Баскетбол',
'Эдвард Элгар': 'Бейсбол',
'Ребекка Кларк': 'Нетбол',
'Этель Смит': 'Бадминтон',
'Фрэнк Бридж': 'Регби'}
print(favorite_sports['Ральф Уильямс'])

games = ['futbol', 'ribalka', 'avtoezda']
foods = ['shaurma', 'pivo', 'riba']
favorites = (games + foods)
print(favorites)

home = 3
nindzya = 25
tunel = 2
samuray = 40
result = ((3 * 25) + (2 * 40))
print(result)

myscore = 1050
message = 'Мой счет: %s очков'
print(message % myscore)

name = 'Vitaliy'
family = 'Katkalo'
best = 'The best %s'
print(best % name, family)

import turtle
t = turtle.Pen()
t.forward(50)
t.left(90)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.reset()
t.backward(100)
t.up()
t.right(90)
t.forward(20)
t.left(90)
t.down()
t.forward(100)