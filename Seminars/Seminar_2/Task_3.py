# 13. Пользователь задаёт две строки. 
# Определить количество вхождений одной строки в другой.

st1 = input('Введите данные первой строки: ')
st2 = input('Введите данные второй строки: ')
# print(st1.count(st2))


index = -1

count = 0
while index < len(st1):
    index = st1.find(st2, index +1)
    if index == -1:
        break
    count+= 1     
print(count)
