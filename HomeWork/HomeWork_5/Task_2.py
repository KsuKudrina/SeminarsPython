# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

#   a) Добавьте игру против бота

#   b) Подумайте как наделить бота "интеллектом"

from random import randint
player_1 = input('Введите ваше имя: ')
player_2 = 'bot' #input('Введите имя второго игрока: ')
all_candies = int(input('Сколько конфет лежит на столе? '))

flag = randint(0, 2)
if flag:
    print(f'Первый ход: игрок {player_1}')
else:
    print(f'Первый ход: игрок {player_2}')

def input_num(name):
    num = int(input(f'{name}, сколько берете конфет (от 1 до 28)? '))
    if num < 1 or num > 28:
        num = int(input('Введите число от 1 до 28: '))
    return num

def interim_results(name, num, current, all_candies):
    print(f'{name} взял {num} конфет, теперь у него {current} \nНа столе осталось {all_candies} конфет')
    print()

current_1 = 0
current_2 = 0

while all_candies > 28:
    if flag:
        num = input_num(player_1)
        current_1 += num
        all_candies -= num
        flag = False
        interim_results(player_1, num, current_1, all_candies)
    else:
        if all_candies > 28 and all_candies < 56:
            num = randint(1, 10)
        else:
            num = randint(1, 29) #num = input_num(player_2)
        current_2 += num
        all_candies -= num
        flag = True
        interim_results(player_2, num, current_2, all_candies)

if flag:
    print(f'Победил {player_1}')
else:
    print(f'Победил {player_2}')




