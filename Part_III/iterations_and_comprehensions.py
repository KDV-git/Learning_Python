print(open('test2.txt', 'r').read())

print('\n')

f = open('test2.txt')
print(f.readline(), end='')  # Файловый метод
print(f.__next__(), end='')  # Итерационный метод
print(f.readline(), end='')  # Файловый метод
print(next(f), end='')  # Итерационный метод

# print(next(f), end='')  - Вызовет исключение StopIteration , т.к. файл закончился

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
