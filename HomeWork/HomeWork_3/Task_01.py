'''
Задайте список из нескольких чисел. 
Напишите программу, которая найдёт сумму 
элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''
from random import randint

def change_list():
    my_list = []
    n = int(input('Длина списка: '))
    for i in range(n):
        my_list.append(randint(1, 100))
    return my_list

def sum_elements(lst):
    summ = 0
    for i in range(1, len(lst), 2):
        summ += lst[i]
    return summ

lst = change_list()
print(lst)
print(f'Сумма элементов на нечетных позициях: {sum_elements(lst)}')

