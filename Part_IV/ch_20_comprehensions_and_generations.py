# Микро примерчик
L = [0, 1, 2, 3, 4, 5]
print(list(filter((lambda x: x * 0), L)))
print(list(filter((lambda x: x ** 2), L)))

print()

# Списковые включения и матрицы
lol = [[1, 2, 3], [10, 11, 12], [19, 20, 21],
       [4, 5, 6], [13, 14, 15], [22, 23, 24],
       [7, 8, 9], [16, 17, 18], [25, 26, 27]]

kek = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
       [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
       [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
       [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
       [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
       [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
       [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
       [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
       [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]]

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

N = [[2, 2, 2],
     [3, 3, 3],
     [4, 4, 4]]

print(M[2])
print(M[2][1])
print(N)

print()

print([row[1] for row in M])

print()

# Извлечение диагоналей
print([M[i][i] for i in range(len(M))])

print([M[i][len(M) - 1 - i] for i in range(len(M))])

# Изменение матрицы на месте использую списковые включения
print([col + 10 for row in M for col in row])
print([[col + 10 for col in row] for row in M])

print()

# Поэлементное сложение элементов двух матриц
NM = [[M[row_i][i] + N[row_i][i] for i in range(len(M[row_i]))] for row_i in range(len(M))]

for row in NM:
    print(row)

print()

# Эквивалент через функцию zip
print([[col1 + col2 for col1, col2 in zip(row1, row2)] for row1, row2 in zip(M, N)])

print('\n\n')


# Генераторные функции и выражения

# Генераторные функции: yield
def gensquares(N):
    for i in range(N):
        yield i ** 2


for i in gensquares(5):
    print(i, end=' : ')

print('\n')

x = gensquares(3)
print(x.__next__())
print(x.__next__())
print(x.__next__())
# print(x.__next__()) - StopIteration

print(iter(x) is x)

print()

# Расширенный протокол генераторных функций: send
print([_ for _ in dir(x) if not _.endswith('__')], end='\n\n')


def generate_numbers():
    i = 0
    while i < 10:
        i += 1
        from_send = yield i
        print(f'GENERATOR: Received {from_send}')


gen = generate_numbers()
# print(gen.send(1)) - TypeError: can't send non-None value to a just-started generator
print(gen.__next__())
print(gen.send(999))

# throw - вызывает исключение подобно raise
# generator.throw(value)
# generator.throw(type[, value[, traceback]])
#
# close - закрывает генерацию и вызывает GeneratorExit
# generator.close()

print('\n\n')

# Генераторные выражения
# Тот же синтаксис, что у списковых включений, только круглые скобки ()

print([x ** 2 for x in range(3)])
print((x ** 2 for x in range(3)))
print(list((x ** 2 for x in range(3))))  # функциональность также что и у включения

print()

G = (x ** 2 for x in range(3))
print(iter(G) is G)
print(next(G))
print(next(G))
print(next(G))
# print(next(G)) - StopIteration

print()

print(''.join(x.upper() * 3 for x in 's,p,a,m'.split(',')))

# Согласно синтаксису, когда генераторное выражение является единственным элементом, уже заключенном в круглые скобки,
# предназначенные для других целей, то помещать его в еще одну пару круглых скобок не требуется.

print(sum(x ** 2 for x in range(5)))
print(sorted(x ** 2 for x in range(5)))
print(sorted((x ** 2 for x in range(5)), reverse=True))  # Здесь круглые скобки обязательны!

print()

# Сравнение генераторных выражений и функции map
nums = (-1, -2, 3, 4)

print(list(map(abs, nums)))
print(list(abs(x) for x in nums))

# Случай без применения функции
print(list(map(lambda x: x ** 2, nums)))
print(list(x ** 2 for x in nums))

print()

# Примеры с вложением
print([x * 2 for x in [abs(x) for x in nums]])
print(list(map(lambda x: x * 2, map(abs, nums))))
print(list(x * 2 for x in (abs(x) for x in nums)))

# Результатом всех трех форм является объединение операций, но генераторы не создают множество временных списков.

print()

# (Не стоит)
print(list(map(abs, map(abs, map(abs, (-1, 0, 1))))))
print(list(abs(x) for x in (abs(x) for x in (abs(x) for x in (-1, 0, 1)))))

print('\n')

# Сравнение генераторных выражений и функции filter
line = 'aa bbb c'

print(''.join(x for x in line.split() if len(x) > 1))
print(''.join(filter(lambda x: len(x) > 1, line.split())))

# С доп обработкой
print(''.join(x.upper() for x in line.split() if len(x) > 1))
print(''.join(map(str.upper, filter(lambda x: len(x) > 1, line.split()))))

print('\n\n')

# Генераторы являются объектами с одиночной итерацией
G = (c * 4 for c in 'SPAM')
I1 = G
I2 = G
I3 = G
print(next(G))
print(next(I1))
print(next(I2))
print(next(I3))

# print(next(G)) - StopIteration
# print(next(I1)) - StopIteration
# print(next(I2)) - StopIteration
# print(next(I3)) - StopIteration

# То же самое работает и с генераторными функциями

print('\n\n')


# Расширение yield from
def both(N):
    for i in range(N):
        yield i

    for i in (x ** 2 for x in range(N)):
        yield i


print(list(both(5)))


def both(N):
    yield from range(N)
    yield from (x ** 2 for x in range(N))


print(list(both(5)))

print('\n')

# Инструменты прохода по каталогам
import os

for (root, subs, files) in os.walk('.'):
    for name in files:
        print(root, name)

print('\n')

G = os.walk('.')

print(iter(G) is G)
print(next(G))
print(next(G))
# print(next(G)) - StopIteration

print('\n\n')


# Генераторы и применение функций
def f(a, b, c):
    print('{}, {} and {}'.format(a, b, c))


f(0, 1, 2)
f(*range(3))
f(*(i for i in range(3)))

print()

D = dict(a='Bob', b='dev', c=40.5)

f(a='Bob', b='dev', c=40.5)
f(**D)
f(*D)
f(*D.values())

print()

for x in 'spam':
    print(x.upper(), end=' ')

print()

print(list(print(x.upper(), end=' ') for x in 'spam'))

print(*(x.upper() for x in 'spam'))

print('\n')


# Перестановки: все возможные комбинации
def permute1(seq):
    if not seq:
        return [seq]
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i + 1:]
            for x in permute1(rest):
                res.append(seq[i:i + 1] + x)
        return res


def permute2(seq):
    if not seq:
        yield seq
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i + 1:]
            for x in permute2(rest):
                yield seq[i:i + 1] + x


print(permute1('abc'))
print(list(permute2('abc')))

G = permute2('abc')

print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
# print(next(G)) - StopIteration

print('\n')

print(permute1('spam'))
print(list(permute2('spam')))

print('\n')

# Единовременно такое количество результатов будет очень долго обрабатываться
# print(permute1(list(range(10))))
# print(list(permute2(list(range(10)))))

# Но генератор выводит следующий результат моментально
G = permute2(list(range(10)))
print(G.__next__())
print(G.__next__())
print(G.__next__())
print(G.__next__())
print(G.__next__())
print(G.__next__())
print(G.__next__())

G = permute2(list(range(50)))
print(G.__next__())
print(G.__next__())
print(G.__next__())

# Обычная функция банально зависнет
# print(permute1(list(range(50))))

print('\n\n')


# Эмуляция zip и map с помощью генераторной функции

def mymap(func, *seqs):
    for args in zip(*seqs):
        yield func(*args)


def myzip(*seqs):
    seqs = [list(S) for S in seqs]
    while all(seqs):
        yield tuple(s.pop(0) for s in seqs)


def myzipPad(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    while any(seqs):
        yield tuple((S.pop(0) if S else pad) for S in seqs)


print(list(map(abs, (-2, -1, 0, 1))))
print(list(mymap(abs, (-2, -1, 0, 1))))

print()

print(list(zip([1, 2, 3], [11, 22, 33])))
print(list(myzip([1, 2, 3], [11, 22, 33])))

print()

print(list(myzip([1, 2, 3], [11, 22, 33, 44, 55])))
print(list(myzipPad([1, 2, 3], [11, 22, 33, 44, 55])))

print('\n')

# Сводка по синтаксису включений (+множеств и +словарей):
print([x * x for x in range(10)])
print(x * x for x in range(10))
print({x * x for x in range(10)})
print({x: x * x for x in range(10)})

print()

# Синтаксический сахар
print({x * x for x in range(10)})
print(set(x * x for x in range(10)))
print({x: x * x for x in range(10)})
print(dict((x, x * x) for x in range(10)))
