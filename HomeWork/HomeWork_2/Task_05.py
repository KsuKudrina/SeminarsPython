# Реализуйте алгоритм перемешивания списка.

from random import randint

n = int(input('Длина списка: '))
my_list = []

for i in range(n):
    my_list.append(randint(1, 100))
print(my_list)

def mix_my_list(my_list):
    lst = my_list

    for i in range(len(lst)):
        j = randint(0, len(lst) -1)
        temp = lst[i]
        lst[i] = lst[j]
        lst[j] = temp
    return lst

lst_ = mix_my_list(my_list)
print(lst_)

