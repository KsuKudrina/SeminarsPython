
# 3. Создайте программу для игры в "Крестики-нолики".

lst = [1, 2, 3, 
       4, 5, 6, 
       7, 8, 9]

def print_lst():
    print('-------------')
    for i in range(3):
        print('|', lst[0 + i * 3], '|', lst[1 + i * 3], '|', lst[2 + i * 3], '|')
        print('-------------')
    return lst

win_combo = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

from random import randint

player_1 = input('Введите имя первого игрока: ')
player_2 = input('Введите имя второго игрока: ')

flag = randint(0, 2)
if flag:
    print(f'Первый ход: игрок {player_1}')
else:
    print(f'Первый ход: игрок {player_2}')

def step_lst(step,symbol):
    ind = lst.index(step)
    lst[ind] = symbol
    

def result(win_combo):
    win = ""
    for i in win_combo:
        if lst[i[0]] == 'X' and lst[i[1]] == 'X' and lst[i[2]] == 'X':
            win = player_1
        if lst[i[0]] == 'O' and lst[i[1]] == 'O' and lst[i[2]] == 'O':
            win = player_2
    return win

def input_value(name):
    step = int(input(f'{name}, ваш ход: '))
    
    return step

game_over = False

while not game_over:
    print_lst()

    if flag:
        symbol = 'X'
        step = input_value(player_1)
        if step >= 1 and step <= 9:
            if (str(lst[step - 1]) not in 'XO'):
                step_lst(step, symbol)
            else:
                print('Эта клетка занята! ')
                continue
        else:
            print('Введите число от 1 до 9! ')
            continue
        flag = False
    else:
        symbol = 'O'
        step = input_value(player_2)
        if step >= 1 and step <= 9:
            if (str(lst[step - 1]) not in 'XO'):
                step_lst(step, symbol)
            else:
                print('Эта клетка занята! ')
                continue
        else:
            print('Введите число от 1 до 9! ')
            continue
        flag = True
    # step_lst(step, symbol)

    win = result(win_combo)
    if win != "":
        game_over = True
    else:
        game_over = False

print_lst()
print("Победил", win)