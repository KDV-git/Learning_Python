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

print()

# Приёмы просмотра файлов
# Чтение всего содержимого в одну строку
file = open('test.txt', encoding='utf-8')
print(file.read())

# Загрузка файла проциями
file.seek(0)

# Посимвольное чтение (При этом файл целиком помещается в память!)
while True:
    char = file.read(1)
    if not char: break
    print(char)

file.seek(0)

for char in file.read():
    print(char)

print()
file.seek(0)

# Чтение по строкам или блокам
while True:
    line = file.readline()
    if not line: break
    print(line.rstrip())  # Строка уже содержит \n

print()
file.seek(0)

# Чтение байтовых порций (до 10 байтов)
bin_file = open('test.txt', 'rb')
while True:
    chunk = bin_file.read(10)
    if not chunk: break
    print(chunk)

# Оптимальное чтение файлов по строкам через цикл for
for line in file.readlines():
    print(line.rstrip())

print()
file.seek(0)

# Наилучший способ для чтения файлов
for line in file:
    print(line.rstrip())

print()
file.seek(0)

# Пример использования метода .readlines() - изменения порядка следования строк на противоположный (с конца документа)
for line in reversed(file.readlines()):
    print(line.rstrip())

file.close()
bin_file.close()

print('\n' * 3)

# Методики написания циклов (range, zip, enumerate, map)
# Функция range (является итерируемым объектом)
print(range(1, 11))
print(list(range(1, 11)))
print(list(range(500, -501, -100)))

S = 'spam'
for i in range(len(S)):
    S = S[1:] + S[:1]
    print(S, end=' ')

print()

for i in range(len(S)):
    X = S[i:] + S[:i]
    print(X, end=' ')

print()
# Метод среза (не оч)
S = 'xyxyxyxy'
for i in range(0, len(S), 2):
    print(S[i], end=' ')

print()
# Лучше так
for c in S[::2]:
    print(c, end=' ')

print()

# Поэлементное изменение списка значений
L = [1, 2, 3, 4, 5]
print(L)

# Метод простым циклом for (не оч)
for x in L:
    L[L[::-1].index(x)] += 1

print(L)

# Более простой способ через функцию range
for i in range(len(L)):
    L[i] += 1

print(L)

# То же самое решение через цикл While
i = 0
while i < len(L):
    L[i] += 1
    i += 1

print(L)

# Самое лучшее решение данной задачи через списковое включение
L = [x + 1 for x in L]
print(L)

print('\n')

# Параллельные обходы (Функция zip)
L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]

print(zip(L1, L2))
print(list(zip(L1, L2)))

for a, b in zip(L1, L2):
    print(a, b)

print()
S1 = 'abcdefg'

for a, b in zip(L1, S1):
    print(a, b)

print()

# Создание словарей с помощью zip
keys = ['spam', 'ham', 'eggs']
values = [1, 3, 5]

D = dict(zip(keys, values))
print(D)

# Альтернативный метод с помощью словарного включения
D = {k: v for k, v in zip(keys, values)}
print(D)

print('\n')

# Генерация смещений и элементов (Функция enumerate) - возвращает генераторный объект
S = 'spam'
for (offset, item) in enumerate(S):
    print(item, 'appears at offset', offset)

print()

E = enumerate(S)
print(type(E))
print(E)
print(next(E))
print(next(E))
print(next(E))
print(next(E))
