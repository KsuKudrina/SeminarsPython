'''
# 1. Напишите программу, которая будет на вход принимать число N 
# и выводить числа от -N до N
# *Примеры:*
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
'''
# try:
#     n = int(input('Введите число: '))
#     m = n * (-1)
#     while m <= n:
#         print(m, end= ', ')
#         m += 1
# except:
#    print('Введите целое число')

try:
    n = int(input('Введите число: '))
    for i in range(-n, n + 1):
        print(i, end= ', ')
except:
    print('Введите целое число')