# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from cmath import sqrt


print('Введите координаты точки A:')
xA = float(input('X: '))
yA = float(input('Y: '))
print('Введите координаты точки B:')
xB = float(input('X: '))
yB = float(input('Y: '))

quad = (xB - xA)**2 + (yB - yA)**2
dist = round(quad ** 0.5, 2)

print(f'Дистанция = {dist}')