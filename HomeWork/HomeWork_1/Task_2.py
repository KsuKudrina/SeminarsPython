'''
задача 2. Напишите программу для проверки истинности утверждения
 ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
'''
try:
    x = int(input('Введите число x '))
    y = int(input('Введите число y '))
    z = int(input('Введите число z '))

    left = not (x or y or z)
    right = not x and not y and not z
    result = left == right

    if result == True:
        print('Утверждение истинно')
    else:
        print('Утверждение ложно')
except:
    print('Введите число')
