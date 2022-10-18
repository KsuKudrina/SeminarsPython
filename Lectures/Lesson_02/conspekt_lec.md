# Файлы
## Использование текстовых файлов
* Хранение данных
* Передача данных в клиент-серверных проектах
* Хранение конфигов
* Логирование действий

## Как работать с файлами
1. Создать переменную

2. Связать файловую переменную с файлом, определив модификатор работы.

3. Указать путь к файлу

4. Указать в каком режиме будем работать

    * a – открытие для добавления данных
    * r – открытие для чтения данных
    * w – открытие для записи данных
    * w+, r+

**Закрывает файл**

            data.close()
или

    with open('file.txt', 'a') as data:
- после завершения автоматически закрывает файл.


# Функции

import hello - импорт файла(где "hello" имя файла)

*Импорт через псевдоним*

    import hello as h
    print(h.f(1)) 

## Кортежи
*Кортеж* - неизменяемый список.

    a = (3, 4)
- это кортеж

*Кортеж из одного элемента*

    a = (3,) 

*Обратиться к элементу кортежа по индексу*

    a = (3, 1, 41, 4)
    print(a)
    print(a[0])

# Словари

*Словаари* - Неупорядоченные коллекции произвольных
объектов с доступом по ключу.

        dictionary = {} -Создать пустой словарь

* \ - чтобы описывать с новой строки

        dictionary = \
        {

        }

* Посмотреть на ключи

        for k in dictionary.keys():
            print(k)

* Посмотреть на значения

        for k in dictionary.values():
            print(k)

* Посмотреть на все элементы словаря

        for v in dictionary:
            print(dictionary[v])

* Изменить значение

        print(dictionary['up'])
        dictionary['up'] = 'up'

* Удаление элемента

        del dictionary['left'] 

# Множества

* Множества - Неупорядоченная совокупность элементов

    Возьмем множество

        colors = {'red', 'green', 'blue'}

- **Добавить элемент в множество**

        colors.add('gray')
        print(colors) # {'red', 'green', 'blue','gray'}

- **Удалить элемент из множества**

        colors.remove('red')
        print(colors) # {'green', 'blue','gray'}

    если такого элемента нет, вызовет ошибку

или


            colors.discard('red')

в этом случае ошибки не будет

- **Очистить множество**

        colors.clear() # { }
        print(colors) # set()


**Копировать множество**

    a = {1, 2, 3, 5, 8}
    c = a.copy() 
 c = {1, 2, 3, 5, 8}

**Объединить множества**

    a = {1, 2, 3, 5, 8}
    b = {2, 5, 8, 13, 21}
    u = a.union(b) 
u = {1, 2, 3, 5, 8, 13, 21}

**Пересечение множеств**

    a = {1, 2, 3, 5, 8}
    b = {2, 5, 8, 13, 21}
    i = a.intersection(b) 
i = {8, 2, 5}

-

    a = {1, 2, 3, 5, 8}
    b = {2, 5, 8, 13, 21}
    dl = a.difference(b) 
    
dl = {1, 3}

-

    a = {1, 2, 3, 5, 8}
    b = {2, 5, 8, 13, 21}
    dr = b.difference(a) 

dr = {13, 21}

**Неизменяемое множество**

    a = {1, 2, 3, 5, 8}
    b = frozenset(a)
    print(b)
- frozenset({1, 2, 3, 5, 8})


# Списки

*Удалить последний элемент списка*

- pop

        lst = [1, 2, 3, 4, 5]
        print(lst)
        print(lst.pop())
        print(lst)
- на выходе удален последний элемент

        [1, 2, 3, 4, 5]
        5
        [1, 2, 3, 4]

*Удалить определенный элемент списка*

- pop

        lst = [1, 2, 3, 4, 5]
        print(lst)
        print(lst.pop(2))
        print(lst)
- на выходе удален элемент с индексом 2

        [1, 2, 3, 4, 5]
        3
        [1, 2, 4, 5]

**Вставить элемент на нужную позицию**

- insert

        lst = [1, 2, 3, 4, 5]
        print(lst)
        print(lst.insert(2, 11))
        print(lst)
- на выходе на позицию с индексом 2 добавлен новый элемент

        [1, 2, 3, 4, 5]
        None
        [1, 2, 11, 3, 4, 5]

**Добавить элемент в конец списка**

- append

        lst = [1, 2, 3, 4, 5]
        print(lst)
        print(lst.append(11))
        print(lst)
- элемент добавлен в конец списка

        [1, 2, 3, 4, 5]
        None
        [1, 2, 3, 4, 5, 11]