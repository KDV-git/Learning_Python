# Kekis
def poop(): print('Hello!'); print('I\'m poop!', end='\n\n'); return 42


x = poop()
print(x)

# В имени функции нет ничего особенного. Важен объект, на который оно ссылается
lul = poop
lul()

# Присваивание аттрибута функции
poop.attr = 10

print(poop.attr)
print(lul.attr)

print()


def multiple(x, y):
    return x * y


print(multiple(2, 10))
print(multiple('2', 10))

print()


def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res


L1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
L2 = [0, 8, 0, 7, 1, 9, 9, 7]
S1 = 'bad_bitch_13'
S2 = '1337_pines_228'
D1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
# print(intersect(L1, S2)) - Сравнение разнотипных объектов вызовет TypeError
print(intersect(L1, L2))
print(intersect(S1, S2))
print(intersect(S1, D1))
print(intersect(L1, D1.values()))

print()

# Тот же результат через списковое включение
print([x for x in S1 if x in S2], end='\n\n')


# Объекты, поддерживающие изменения на месте, при передаче внутрь функции и изменяемые внутри неё без копирования,
# сохраняют все изменения в объекте, на который также ссылается и глобальная переменная, что может привести к
# нежелательному изменению в глобальной области видимости!
def mult(one, two):
    one.append(1.0)
    one.append(2000)
    two += 5
    return one * two


x = [3, 33]
y = 5
print(x, y)
print(mult(x, y))
print(x, y)

print()


# Как надо:

def mult_nice(one, two):
    local_one = one.copy()
    local_one.append(1.0)
    local_one.append(2000)
    two += 5
    return one * two


x = [3, 33]
y = 5
print(x, y)
print(mult_nice(x, y))
print(x, y)
