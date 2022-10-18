
# 2. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

lst = [1, 5, 9, 15, 35]

n = int(input('Введите число: '))
def find_num(lst, n): 
    for i in lst:
        if i == n:
            print(f'Число {n} есть в списке. ')
            return True
    print('Такого числа нет. ')   
    return False 

find_num(lst, n)