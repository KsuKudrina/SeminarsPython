#a, b = 3,4 # в переменную а - 3, в переменную b - 4
# если обрамление в виде скобок
# a = (3, 4)#- Это кортеж
# print(a)
# print(a[0])

# a = (3, 1, 41, 4)
# print(a)
# print(a[-2])

# a[0] = 12 # для кортежей не работает!
# a = (3,) # кортеж из одного элемента

t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r: {} g: {} b: {}'.format(red, green, blue))
# r:red g:green b:blue
# print(t[0]) # red
# print(t[2]) # blue
# # print(t[10]) # IndexError: tuple index out of range
# print(t[-2]) # green
# # print(t[-200]) # IndexError: tuple index out of range
# for e in t:
#     print(e) # red green blue
# t[0] = 'black' # TypeError: 'tuple' object does not support
# item assignment