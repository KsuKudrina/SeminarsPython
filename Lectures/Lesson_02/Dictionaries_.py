# dictionary = {} # пустой словарь
# \ - чтобы описывать с новой строки

#from macpath import split
#.split()

dictionary = \
    {
        'up': '↑',
        'left': '←',
        'down': '↓',
        'right': '→'
    }
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# типы ключей могут отличаться

# # Посмотреть на ключи
# for k in dictionary.keys():
#     print(k)

# # Посмотреть на значения
# for k in dictionary.values():
#     print(k)

# # Посмотреть на все элементы словаря

# for v in dictionary:
#     print(dictionary[v])

# # Изменить значение
# print(dictionary['up'])
# dictionary['up'] = 'up'


'''
print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
#print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →
'''
