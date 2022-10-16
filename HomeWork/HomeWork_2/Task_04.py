# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

n = int(input("Введите число: "))

my_list = []
for i in range(n):
    my_list.append(randint(-n, n))
print(my_list)

with open('file.txt', 'w') as f:
    for i in range(n):
        f.write(str(randint(0, n -1)) + '\n')

fact = 1
with open('file.txt', 'r') as f:
    f = f.read().splitlines()
    for num in f:
        fact *= my_list[int(num)]
print(fact)
