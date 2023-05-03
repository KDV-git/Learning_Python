x = -1
while x:
    if x < 0:
        print('Time is overflow({})'.format(x))
        break
    print('{} second remaining.'.format(x))
    x -= 1
else:
    print('Time is over!')

print()


# Оператор pass
def func1():
    pass


def func2():
    ...


x = ...  # Альтернатива None
print(type(x))
print(x)

print()

# Оператор continue
x = 10
while x:
    x -= 1
    if x % 2 != 0: continue
    print(x, end=' ')

print()

# Оператор break
# while True:
#     name = input('Enter name: ')
#     if name == 'stop': break
#     age = input('enter age: ')
#     print('Hello', name, '=>', int(age) ** 2)

# Конструкция else цикла
y = -10000000
x = y // 2
while x > 1:
    if y % x == 0:
        print(y, 'has factor', x)
        break
    x -= 1
else:  # Выводится когда цикл while вообще не запускается (т.е. не проходит изначальную проверку условия)
    print(y, 'is prime')

print('\n' * 3)

# Циклы for
L = ['spam', 'ham', 'eggs']

for x in L:
    print(x, end=' ')

print('\n')

L = [1, 2, 3, 4]
summ = 0

for x in L:
    summ += x

print(L)
print('sum = {}'.format(summ))
print('x = {}'.format(x))

print()

prod = 1
for item in L: prod *= item

print(L)
print('prod = {}'.format(prod))
print('item = {}'.format(item))  # Unbound local variables

print('\n')

# Присваивание кортежей (tuples unpacking)
T = [(1, 2), (3, 4), (5, 6)]

for a, b in T:
    print(a, b)

D = {'a': 1, 'b': 2, 'c': 3}

for key in D:
    print(key, '=>', D[key])

for key, value in D.items():
    print(key, '=>', value)

print()

for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]: print(a, b, c)

for ((a, b), c) in [((1, 2), 3), ('XY', 'Z')]: print(a, b, c)

print('\n')

# Расширенное присваивание последовательностей в циклах for
for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]: print(a, b, c)

print('\n')

# Вложенные циклы for
items = ['aaa', 111, (4, 5), 2.01]
tests = [(4, 5), 3.14]

for key in tests:
    for item in items:
        if item == key:
            print(key, 'was found!')
            break
    else:
        print(key, 'not found!')

for key in tests:
    if key in items:
        print(key, 'was found!')
    else:
        print(key, 'not found!')

print()

seq1 = 'spam'
seq2 = 'scam'

res = []
for x in seq1:
    if x in seq2:
        res.append(x)

print(res)
print([x for x in seq1 if x in seq2])
