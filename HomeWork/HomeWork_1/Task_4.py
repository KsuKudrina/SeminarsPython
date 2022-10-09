'''
задача 4 HARD необязательная. Напишите простой калькулятор, который считывает с пользовательского ввода три строки:
первое число, второе число и операцию, после чего применяет операцию к введённым числам 
("первое число" "операция" "второе число") и выводит результат на экран.
    Поддерживаемые операции: +, -, /, *, mod, pow, div, где
        mod — это взятие остатка от деления,
        pow — возведение в степень,
        div — целочисленное деление.
Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
    На вход программе приходят вещественные числа.

Sample Input 1:    Sample Output 1:        Sample Input 2:         Sample Output 2:     Sample Input 3:     Sample Output 3:
5.0                Деление на 0!           -12.0                   96.0                 5.0                 0.5
0.0                                         -8.0                                        10.0
mod                                         *                                           /
'''
try:
    num1 = float(input('Введите число 1: '))
    sign = input('Введите символ операции: ')
    num2 = float(input('Введите число 2: '))
    
    if num2 == 0 and (sign == '/' or  sign == 'mod' or sign == 'div'):
        print('Деление на 0!')
    elif sign == "+":
        print(num1 + num2)
    elif sign == "-":
        print(num1 - num2)
    elif sign == "/":
        print(num1 / num2)
    elif sign == "*":
        print(num1 * num2)
    elif sign == "mod":
        print(num1 % num2)
    elif sign == "pow":
        print(num1 ** num2)
    elif sign == "div":
        print(num1 // num2)
except:
    print('Введите число')

