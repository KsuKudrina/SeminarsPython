# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def first_file(st):
    with open('file_1.txt', 'w') as data:
        data.write(st)

def create_mn(k):
    lst = []
    for i in range(k+1):
        lst.append(random.randint(0,101))
    return lst
    
def create_str(sp):
    lst= sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

# Создать файл для задачи 5.
# def second_file(st):
#     with open('file_2.txt', 'w') as data:
#         data.write(st)

k = int(input("Введите натуральную степень k = "))
koef = create_mn(k)
first_file(create_str(koef))
# для задачи 5
# second_file(create_str(koef))