'''
Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, 
второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''
from random import randint

n = int(input('Длинна списка: '))
def create_list():
    my_list = []
    for i in range(n):
        my_list.append(randint(1, 10))
    return my_list

def proiz_nums(lst):
    lst1 = []
    j = len(lst) -1
    if n % 2 == 0:
        s = n // 2
    else:
        s = n // 2 + 1

    for i in range(s):
        el = lst[i] * lst[j]
        lst1.append(el)
        j -= 1
    return lst1
lst = create_list()
print(lst)
lst1 = proiz_nums(lst)
print(lst1)    

