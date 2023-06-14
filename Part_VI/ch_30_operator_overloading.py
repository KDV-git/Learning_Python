# Перегрузка операций - это перехват встроенных операций в методах класса.

class Number:
    def __init__(self, start):
        self.data = start

    def __sub__(self, other):
        return Number(self.data - other)


X = Number(5)
Y = X - 2
print(X.data)
print(Y.data)

print('\n')


# Метод __getitem__ автоматически вызывается для операций индексирования экземпляров.
class Indexer:
    def __getitem__(self, index):
        return index ** 2


X = Indexer()

print(X[2])

for i in range(5):
    print(X[i], end=' ')

print('\n')

# Метод __getitem__ также вызывается для выражений срезов
L = [5, 6, 7, 8, 9]
print(L[2:4])
print(L[1:])
print(L[:-1])
print(L[::2], end='\n\n')

# На самом деле границы нарезания упаковываются в объект среза и передаются реализации индексирования списка
print(slice(1, 2))
print(type(slice(1, 2)), end='\n\n')

print(L[slice(2, 4)])
print(L[slice(1, None)])
print(L[slice(None, -1)])
print(L[slice(None, None, 2)], end='\n\n')


class Indexer:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, index):
        print('getitem:', index)
        return self.data[index]


X = Indexer()
print(X[0])
print(X[1])
print(X[-1])

print()

print(X[2:4])
print(X[1:])
print(X[:-1])
print(X[::2])

print('\n')


# Там, где необходимо, метод __getitem__ может проверять тип своего аргумента и извлекать границы объекта среза

class Indexer:
    def __getitem__(self, index):
        if isinstance(index, int):
            print('indexing', index)
        else:
            print('slicing', index.start, index.stop, index.step)


X = Indexer()

X[99]
X[1:99:2]
X[1:]

print('\n')


# Метод присваивания по индексу __setitem__ похожим образом перехватывает присваивания по индексу и срезу.

class IndexSetter:
    data = [1, 2, 3, 4, 5]

    def __setitem__(self, key, value):
        self.data[key] = value


X = IndexSetter()
print(X.data)
X[1:4] = [4, 6, 8]
print(X.data)

print('\n')


# Метод __index__ не имеет отношения к индексированию (Он возвращает целочисленное значение для экземпляра).
# И используется встроенными функциями, которые выполняют преобразование в строки цифр.

class C:
    def __index__(self):
        return 255


X = C()
print(hex(X))
print(bin(X))
print(oct(X))

# Данный метод также применяется в контекстах, которые требуют целого числа — включая индексацию (экземпляр как индекс)

print(('C' * 256)[255])
print(('C' * 256)[X])
print(('C' * 256)[X:])

print('\n')


# Итерация по индексам: __getitem__
class SuperIndex:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, item):
        return self.data[item]


X = SuperIndex('Spam')

print(X[1])

for item in X:
    print(item, end=' ')

print('\n\n')

# Итерационные контексты
print('p' in X)
print([c for c in X])
print(list(map(str.upper, X)))

a, b, c, d = X
print(d, c, b, a)

print(list(X), tuple(X), '.'.join(X))

print(X)

print('\n\n\n')


# Итерируемые объекты: __iter__ и __next__
class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        else:
            self.value += 1
            return self.value ** 2


for i in Squares(1, 5):
    print(i, end=' ')

print()

X = Squares(1, 5)
print(next(X))
print(next(X))
print(next(X))
print(next(X))
print(next(X))
# print(next(X)) - raise StopIteration

print()

X = Squares(1, 5)
# print(X[1]) - TypeError: 'Squares' object is not subscriptable
print(list(X)[1])

print()

# Метод __iter__ класса может быть предназначен только для единственного обхода
X = Squares(1, 5)

print([n for n in X])
print([n for n in X])

print([n for n in Squares(1, 5)])

print()

# Другие итерационные контексты
print(36 in Squares(1, 10))
a, b, c = Squares(1, 3)
print(a, b, c)
print(':'.join(map(str, Squares(1, 5))))

print()

# Преобразование в список поддерживает множество просмотров, ценой дополнительного расхода времени и пространства
X = Squares(1, 5)

print(tuple(X))
print(tuple(X))

X = list(Squares(1, 5))

print(tuple(X))
print(tuple(X))

print('\n')


# Множество итераторов в одном объекте
class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        return SkipIterator(self.wrapped)


class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item


alpha = 'abcdef'
skipper = SkipObject(alpha)
I = iter(skipper)
print(next(I), next(I), next(I))
# print(next(I)) - raise StopIteration

for x in skipper:
    for y in skipper:
        print(x + y, end=' ')

print()

a = SkipObject('abc')
b = SkipObject('abc')
print(a is b)

print('\n')


# Альтернативная реализация: __iter__ + yield
class SquaresYield:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2


for i in SquaresYield(1, 5):
    print(i, end=' ')

print()

S = SquaresYield(1, 5)
print(S)
I = iter(S)
print(I)
print(next(I))
print(next(I))
print(next(I))
print(next(I))
print(next(I))
# print(next(I)) - StopIteration

# Реализация генератора как __iter__ устраняет посредника в коде, хотя обе схемы создают новый генераторный объект для каждой итерации:
# • Наличие __iter__ запускает метод __iter__, который возвращает новый генераторный объект с методом __next__.
# • Отсутсвие __iter__ производит вызов для создания генераторного объекта, метод __iter__ которого возвращает сам объект.

print()

# Множество итераторов с помощью yield
