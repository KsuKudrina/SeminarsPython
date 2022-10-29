# Задайте последовательность чисел. 
# Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.
# nums = [2, 3, 5, 9, 3, 1, 2]
from random import randint

def change_list():
    my_list = []
    n = int(input('Длина списка: '))
    for i in range(n):
        my_list.append(randint(1, 10))
    return my_list

def new_list(nums):
    list_n = []
    for i in nums:
        if nums.count(i) == 1:
            list_n.append(i)
    return list_n
nums = change_list()
print(nums)

lst = new_list(nums)
print(lst)

# mn = set(nums)
# print(mn)

