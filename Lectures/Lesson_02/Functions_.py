# import hello

# print(hello.f(1))

# import hello as h

# print(h.f(1))

# def new_string(symbol, count = 3):
#     return symbol * count

# print(new_string('!', 5)) # !!!!!
# print(new_string('!'))    # !!!
# print(new_string(4))      # 12

def concatenatio(*params):
    res: str = ""
    for item in params:
        res += item
    return res
print(concatenatio('a', 's', 'd', 'w')) # asdw
print(concatenatio('a', '1', 'd', '2')) # a1d2
# print(conatenatio(1, 2, 3, 4)) # TypeError: ...

