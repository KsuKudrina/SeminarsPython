# Напишите программу, которая принимает на вход число N
# и выдаёт последовательность из N членов.

# n = int(input('Введите число: '))
# current = 0
# while current < n:
#     print(n, end= ' ')
#     current += 1

# import random
# from random import randint
# n = int(input('Введите число: '))
# lst = []
# for i in range(n):
#     num = randint(1, 100)
#     lst.append(num)              #lst.append(randint(1, 100))
# print(lst)

# Для N = 5: 1, -3, 9, -27, 81 и т.д.
n = int(input('Введите число: '))
lst = []
for i in range(n):
    lst.append((-3) ** i)
print(lst)
