
# 1. Реализуйте алгоритм задания случайных чисел 
# без использования встроенного генератора псевдослучайных чисел.

import time

n = int(input("Введите число: "))
my_list = []

def random_nums(max, min):
    time.sleep(0.3)
    return int((time.time() % 1 * (max - min)) + min)

for i in range(n):
    my_list.append(random_nums(1,9))

print(my_list)

# a = 123456

# my_list = []
# for i in range(10):
#     n = a % 100
#     my_list.append(n)
#     a = (a * 4125896453) % 1000000
# print(my_list)
