'''
Задайте список из вещественных чисел. 
Напишите программу, которая найдёт разницу между максимальным 
и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''

from random import uniform
n = int(input('Длинна списка: '))
def create_list():
    my_list = []
    for i in range(n):
        num = uniform(0, 10)
        my_list.append(round(num, 2))
    return my_list

def new_list(lst):
    lst1 = []
    for i in range(n):
        el = lst[i]
        num = el - int(el)
        if num != 0:
            lst1.append(round(num, 2))
    return lst1

def max_el(lst1):
    max_ = lst1[0]
    for i in range(len(lst1)):
        if max_ < lst1[i]:
            max_ = lst1[i]
    return max_

def min_el(lst1):
    min_ = lst1[0]
    for i in range(len(lst1)):
        if min_ > lst1[i]:
            min_ = lst1[i]
    return min_

print('Разница между максимальным и минимальным значением дробной части элементов')
lst = create_list()
print(lst)
lst1 = new_list(lst)

max_ = max_el(lst1)
min_ = min_el(lst1)

# max_ = max(lst1)
# min_ = min(lst1)
result = max_ - min_
print(f'Равна {round(result, 2)}')

