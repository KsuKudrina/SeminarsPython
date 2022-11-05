# 42. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open ('file_03.txt', 'w') as file:
    file.write('WWWWWPPPPPPAAAAAAAANN')

with open ('file_03.txt', 'r') as file:
    lst = file.readline()


print(lst)
def econde(lst):
    code = ''
    prev_char = ''
    counter = 1
    if not lst: return ''

    for char in lst:
        if char != prev_char:
            if prev_char: 
                code += str(counter) + prev_char
            counter = 1 
            prev_char = char
        else:
            counter += 1 
    else:
        code += str(counter) + prev_char 
    return code

lst_1 = econde(lst)
print(lst_1)

with open ('file_04.txt', 'w') as file:
    file.write(lst_1)

with open ('file_04.txt', 'r') as file:
    lst_1 = file.readline()

def decode(lst):
    decode = ''
    counter = ''
    for char in lst:
        if char.isdigit():
            counter += char
        else:
            decode += char * int(counter)
            counter = ''
    return decode

print(decode(lst_1))