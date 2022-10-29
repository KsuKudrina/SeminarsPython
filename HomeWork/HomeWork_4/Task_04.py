# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


from random import randint
from unittest import result
def first_file(st):
    with open('file_1.txt', 'w') as data:
        data.write(st)

def create_mn(k):
    lst = []
    for i in range(k+1):
        lst.append(randint(0,101))
    return lst

def create_str(koefs):
    result = ''
    for i in range(len(koefs)):
        if len(result) > 0 and koefs[i] > 0:
            result = result + ' + '
        else:
            if i > 0:
                result = result + ' '
        if koefs[i] == 0:
            continue
        result = result + str(koefs[i]) + 'x'
        if (k - i) != 0 and (k - i) != 1:
            result = result + '^' + str(k - i) + ' '
    if koefs[- 1] != 0:
        result = result[: len(result) - 1]
    result = result + ' = 0'
    return result

 
# def create_str(sp):
#     lst= sp[::-1]
#     wr = ''
#     if len(lst) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(lst)):
#             if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                 wr += f'{lst[i]}x^{len(lst)-i-1}'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 2 and lst[i] != 0:
#                 wr += f'{lst[i]}x'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 1 and lst[i] != 0:
#                 wr += f'{lst[i]} = 0'
#             elif i == len(lst) - 1 and lst[i] == 0:
#                 wr += ' = 0'
#     return wr

# Создать файл для задачи 5.
# def second_file(st):
#     with open('file_2.txt', 'w') as data:
#         data.write(st)

k = int(input("Введите натуральную степень k = "))
koefs = create_mn(k)
res = create_str(koefs)
first_file(res)
print(res)
# для задачи 5
# second_file(create_str(koef))