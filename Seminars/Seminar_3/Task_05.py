# 3. Напишите программу, которая определит позицию
#  второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*

# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# lst = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# str_find = 'йцу'
# count = 0

# for i in range(len(lst)):
#     if str_find == lst[i]:
#         count += 1
#         if count == 2:
#             print(i)

# if count < 2:
#     print('ничего не найдено')

list_1 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
def double_index(list_1: list, str_2: str):
    if list_1.count(str_2) < 2:
        return -1
    index_1 = list_1.index(str_2)
    index_2 = list_1.index(str_2, index_1 + 1)
    return index_2

res = double_index(list_1, 'йцу')
print(res)



