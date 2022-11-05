
# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

txt = input('Введите текст: ')
print(f'Исходный текст: \n{txt}')
find_txt = 'абв'
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')