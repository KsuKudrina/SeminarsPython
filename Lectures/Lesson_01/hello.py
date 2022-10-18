# print('hello world')

# типы данных
'''
# int, float, boolean, str, list, None
'''
#value = None

# print(type(a))
# print(a)
# print(type(b))
# print(b)

# print(value)
# s = 'hello world'    # s = 'hello "world'
# s = "hello 'world" # s = 'hello \'world'
# \n - переход на новую строку

# print(s) # вывод строки
# print(a, '-', b, '-', s)
# print('{} - {} - {}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

#f = False
#print(f)

# Списки

# list = []
# list = ['1', '2', '3', 4, 5, 'hello world']
# list = ['1', '2', '3']
# col = ['hello world', 1, 2, 3, True]

# print(list)
# print(col)

# print() - Вывод данных
# input() - Ввод данных 

# print('Введите а');
# a = input()
# a = int(input())
# a = float(input())
# print('Введите b');
# b = input()
# b = int(input())
# b = float(input())
# print(a, '+', b, ' = ', a+b)          # Введите а # 10
                                        # Введите b # 20
                                      # 10 + 20  =  1020
# print('{} {}'.format(a,b))
# print(f'{a} {b}')

# АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ
'''
# +, -, *, /, %, //(целочисленное деление), **(возведение в степень)
# Приоритет операций
# **, ⊕, ⊖, *, /, //, %, +, -
# () Скобки меняют приоритет
'''
# a = 1.3123                  # round - округление
# b = 3                       # round(a * b, 3) - округление до 3 знаков
# c = round(a * b, 5)
# print(c)

# a = 3
# a = a + 5
# a += 5
# print(a)

# Логические операции
'''
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# is, is not, in, not in
'''

# a = 1 < 4 and 5 > 2
# a = 1 == 2
# a = 1 != 2
# a = 1 < 3 < 5 
# print(a)

# a = [1, 2, 3]   # a = ['one']
# b = [1, 2, 3]   # b = ['one']
# print(a == b)

# func = 1
# T = 4
# x = 123

# print(func < T > x)

# f = 1 > 2 or 4 < 6
# print(f)

# f = [1,2,3,4]
# print(f)
# print(2 in f) #содержится в списке
# print(not 2 in f) # не содержится в списке

# is_odd = f[0] % 2 == 0
# print(is_odd)

# Управляющие конструкции
# if / else
'''
if condition:
 # operator 1
 # operator 2
 # ...
 # operator n
else:
 # operator n + 1
 # operator n + 2
 # ...
 # operator n + m
'''

#a = int(input('a = '))
#b = int(input('b = '))

# if a > b:
#    print(a)
# else:
#    print(b)    

# if / elif
'''
username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же Маша!')
elif username == 'Марина':
    print('Я так ждала Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ')
else:
    print('Привет, ', username)
'''
# Переворачиваем число
'''
original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)
'''
'''
original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
    print(original)
else:
    print('Пожалуй')
    print('хватит )')
print(inverted)
'''
# for 
'''
for i in 1, 2, 3, 4, 5:
    print(i ** 2)
'''
# list = [1,2,3,4, 10, 5]
#r = range(10)
#for i in r:
#    print(i)

'''
text = 'съешь ещё этих мягких французских булок'
print(len(text))                     # 39       #количество символов
print('ещё' in text)                 # True     #наличие подстроки
print(text.isdigit())                # False    #являются ли все символы строки числами 
print(text.islower())                # True     #являются ли символами нижнего регистра
print(text.replace('ещё','ЕЩЁ'))     #          #что то заменить
for c in text:
    print(c)
'''
'''
numbers = [1, 2, 3, 4, 5]       #print(type(numbers))
#numbers = list(range(1, 6))    #ran = range(1, 6)
#print(numbers)                 #print(type(ran))

numbers[0] = 10
#print(f'{len(numbers)} len')
print(numbers)  # [10, 2, 3, 4, 5]

for i in numbers:
    i *= 2
    print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5]
'''
'''
colors = ['red', 'green', 'blue']

for e in colors:
    print(e)        # red green blue
for e in colors:
    print(e*2)      # redred greengreen blueblue

colors.append('gray')                               # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray'])   # True
colors.remove('red')                                # удалить элемент
#del colors[0]
'''
#Функции

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 2.3
print(f(arg))
print(type(f(arg)))
