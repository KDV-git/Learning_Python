print(open('test2.txt', 'r').read())

print('\n')

f = open('test2.txt')
print(f.readline(), end='')  # Файловый метод
print(f.__next__(), end='')  # Итерационный метод
print(f.readline(), end='')  # Файловый метод
print(next(f), end='')  # Итерационный метод

# print(next(f), end='')  - Вызовет исключение StopIteration, т.к. файл закончился

print('\n')
f.seek(0)

# Лучший способ чтения файла построчно
for line in f:
    print(line.rstrip())

print('\n')
f.close()

# Первый шаг протокола итерации - получение объекта итератора из итерируемого объекта
L = [1, 2, 3]
print(L)
print(type(L), end='\n\n')

I = iter(L)
print(I)
print(type(I), end='\n\n')

print(I.__next__())
print(I.__next__())
print(I.__next__())
# print(I.__next__()) - StopIteration

# print(L.__next__()) - AttributeError: 'list' object has no attribute '__next__'

print()

# Файловый объект является итератором сам по себе
f = open('test2.txt', 'r')
print(iter(f) is f)
print(iter(f) is f.__iter__())
print(f.__next__())

# Суть работы цикла for и ручная итерация
print(L)

# Автоматическая итерация
for X in L:
    print(X ** 2, end=' ')  # Получает iter, вызывает __next__ и перехватывает исключения

print()

# Ручная итерация: то, что по сути делают циклы for
I = iter(L)
while True:
    try:
        X = I.__next__()
    except StopIteration:
        break
    print(X ** 2, end=' ')

print('\n')

# Итерируемые объекты других встроенных типов
# Словари
D = {'a': 1, 'b': 2, 'c': 3}

for key in D:
    print(key, D[key])

I = iter(D)
print(next(I))
print(next(I))
print(next(I))
# print(next(I)) - StopIteration

print()

# os.popen() - инструмент для чтения вывода команд оболочки
import os

P = os.popen('dir')
print(P.__next__())
print(P.__next__())

# Объекты popen поддерживают метод __next__, но НЕ поддерживают встроенную функцию next()!
# print(next(P)) - TypeError: '_wrap_close' object is not an iterator

P = os.popen('dir')
I = iter(P)
print(I.__next__())
print(next(I))

print('\n')

# Итерируемые объекты возвращают по одному результату за раз, а не физический список
R = range(5)
print(R)  # Итерируемый объект
# print(next(R)) - TypeError: 'range' object is not an iterator

I = iter(R)  # Использование протокола итерации для выпуска результатов
print(next(I))
print(next(I))

print(list(R))  # Применение вызова list для сбора всех результатов

print('\n')

# Инструмент enumerate также итерируемый
E = enumerate('spam')
print(E)

I = iter(E)
print(next(I))
print(next(I))

print(list(E), end='\n\n')

print(list(enumerate('spam')))

print('\n')

# Включения вместе с циклами for входят в число наиболее известных контекстов, в которых применяется проток итерации
L = [1, 2, 3, 4, 5]
print(L)

# Не самый оптимальный способ изменения списка
for i in range(len(L)):
    L[i] += 10

print(L)

# Оптимальный способ через списковое включение
L = [x + 10 for x in L]
print(L)

# То, что по сути делает списковое включение
res = []
for x in L:
    res.append(x + 10)

print(res, end='\n\n')

# Списковое включение с файлами
f = open('test2.txt')
lines = f.readlines()
print(lines)

lines = [line.rstrip() for line in lines]
print(lines)

# Та же операция, без предварительного открытия файла (Открытый файл подвергается сборке мусора после выполнения)
lines = [line.rstrip() for line in open('test2.txt')]
print(lines, end='\n\n')

# Несколько примеров
lines = [line.replace('s', '$').capitalize() for line in open('test2.txt')]
print(lines)

lines = [line.rstrip().upper().replace('I', 'P').replace('P', 'pig') for line in open('test2.txt')]
print(lines)

lines = [(line.rstrip()[-1].lower() * 5, line[0].upper() * 5) for line in open('test2.txt')]
print(lines)

lines = [(line.isalnum(), line.upper().isupper(), "SPAM" in line.replace(' ', 'SPAM')) for line in open('test2.txt')]
print(lines)

print('\n')

# Расширенный синтаксис списковых включений
# Конструкции фильтров: if
lines = [line.rstrip() for line in open('test2.txt') if line.lower()[0] == 'p']
print(lines)

lines = [line.rstrip() for line in open('test2.txt') if line.rstrip()[-1:].isdigit()]
print(lines)

lens = len([line for line in open('test.txt') if line.rstrip() != ''])
print(len(open('test.txt').readlines()))
print(lens)

print('\n')

# Вложенные циклы for поддерживают любое количество конструкций с необязательным фильтром if для каждой
combinations = [x + y for x in 'abc' for y in 'def']
print(combinations)

print('\n')

# Другие итерационные контексты (все они являются итерационными инструментами)
uppers = [line.upper() for line in open('test2.txt')]
print(uppers)

# Функция map
map_uppers = map(str.upper, open('test2.txt'))
print(map_uppers)
print(type(map_uppers))
print(list(map_uppers))

print()

print(sorted(open('test2.txt')))  # Единственная функция, возвращающая реальный список, а не итерируемый объект
print(list(zip(open('test2.txt'), open('test2.txt'))))
print(list(enumerate(open('test2.txt'))))
print(list(filter(bool, open('test2.txt'))))

# Функция reduce - прогоняет пары элементов через указанную функцию
import functools, operator

print(functools.reduce(operator.add, open('test2.txt')))

print()

# Инструменты также поддерживающие протокол итерации
print(list(open('test2.txt')))
print(tuple(open('test2.txt')))
print('##'.join(open('test2.txt')))

print()

# Присваивание последовательностей
a, b, c, d = open('test2.txt')
print(d)

# Расширенная форма
a, *b = open('test2.txt')
print(b)

# Проверка членства
print('y = 2\n' in open('test2.txt'))
print('x = 2\n' in open('test2.txt'))

# Присваивание срезов
L = [11, 22, 33, 44]
L[1:3] = open('test2.txt')
print(L)

# Метод list.extend()
L = [11]
L.extend(open('test2.txt'))
print(L)

# Но НЕ list.append()!
L = [11]
L.append(open('test2.txt'))
print(L)
print(list(L[1]))

# Функция set()
S = set(open('test2.txt'))
print(S)

print()

# Также включения множеств и словарей (Они также поддерживают конструкцию if)
S = {line for line in open('test2.txt')}
print(S)

D = {i: line for i, line in enumerate(open('test2.txt'))}
print(D)

print()

# Итерируемые словарные представления
D = dict(a=1, b=2, c=3)
print(D)

# Объекты представления не являются итераторами, но являются итерируемыми объектами
K = D.keys()
V = D.values()
Items = D.items()

I1, I2, I3 = iter(K), iter(V), iter(Items)
print(I1, I2, I3)
print(next(I1), next(I2), next(I3), sep=' - ')
print(next(I1), next(I2), next(I3), sep=' - ')
print(next(I1), next(I2), next(I3), sep=' - ')
# print(next(I1), next(I2), next(I3), sep=' - ') - StopIteration


# Генераторные выражения
print(list(line.upper() for line in open('test2.txt')))

print('\n')

# Примеры более узконаправленных функций, поддерживающих протокол итерации
print(sum([3, 2, 4, 1, 5, 0]))
print(any(['spam', '', 'ni']))  # True если хоть одно значение истинно
print(all(['spam', '', 'ni']))  # True если ВСЕ значение истинны
print(max([3, 2, 5, 1, 4]))
print(min([3, 2, 5, 1, 4]))

# Взаимодействие min и max с файлами
print(max(open('test2.txt')))  # Строка с максимальным строковым значением
print(min(open('test2.txt')))  # Строка с минимальным строковым значением


# Специфальная форма "*аргумент" применяемая при вызове функций, для распаковки аргументов
def f(a, b, c, d):
    print(a, b, c, d, sep='@#$%')


print(f(*open('test2.txt')))

print()

# Развёртывание сжатых кортежей
X = (1, 2)
Y = (3, 4)

print(list(zip(X, Y)))

A, B = zip(X, Y)
print(A)
print(B)

A, B = zip(zip(X, Y))
print(A)
print(B)

print('\n')

# Отдельное рассмотрение объектов map, zip и filter
# Они являются собственными итераторами(результаты после однократного прохода по ним - израсходуются!)
M = map(abs, (-1, 0, 1))
print(M)
print(M.__next__())
print(next(M))
print(next(M), end='\n\n')

# print(next(M)) - StopIteration
# print(M[0]) - TypeError: 'map' object is not subscriptable

for x in M:
    print(x)

M = map(abs, (-1, 0, 1))

for x in M:
    print(x)

print(list(M))
print(list(map(abs, (-1, 0, 1))))

# Аналогично работают функции zip и filter

print('\n')

# Разница с функцией range
R = range(3)
I1 = iter(R)
I2 = iter(R)

print(next(I1))
print(next(I1))
print(next(I1))

print(next(I2))

# В отличие от остальных функций, функция range поддерживает несколько итераторов
Z = zip((1, 2, 3), (11, 12, 13))
I1 = iter(Z)
I2 = iter(Z)

print(next(I1))
print(next(I1))
print(next(I1))

# print(next(I2)) - StopIteration

# Функции zip, map и filter поддерживает только один активный проход по элементам
