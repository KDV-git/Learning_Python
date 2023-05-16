def f(a):
    a = 99  # Изменяется локальная переменная а


b = 88
f(b)
print(b, end='\n\n')


# Передача изменяемого объекта
def changer(a, b):
    a = 2
    b[1] = 'spam'  # Изменение объекта на месте


X = 1
L = [1, 2, 3]

changer(X, L)
print(X, L, sep='\n')

# Способ защиты от изменений
X = 1
L = [1, 2, 3]

changer(X, L[:])
print(X, L, sep='\n')


# Копирование внутри функции
def changer(a, b):
    b = b[:]
    a = 2
    b[1] = 'spam'


X = 1
L = [1, 2, 3]

changer(X, L)
print(X, L, sep='\n')

print('\n')


# Вывод множества значений
def multiple(x, y):
    x = 2
    y = [3, 4]
    return x, y  # Упаковка выводимых значений в кортеж


X = 1
L = [1, 2, 3]
X, L = multiple(X, L)

print(X, L, sep='\n', end='\n\n\n')


# Специальные режимы сопоставления аргументов

# Примеры ключевых слов и стандартных значений
def f(a, b, c): print(a, b, c)


f(1, 2, 3)  # Сопоставление имён слева направо

# Ключевые слова
f(c=3, b=2, a=1)  # Аргументы сопоставляются по имени, а не по позиции

# f(1, a=1, c=3) - TypeError: f() got multiple values for argument 'a'

print()


# Стандартные значения
def f(a, b=2, c=3): print(a, b, c)


f(1)  # Использование стандартных значений
f(a=1)
f(1, 4)  # Переопределение стандартных значений
f(1, 4, 5)
f(1, c=6)  # Выбор стандартных значений

print()


# Примеры комбинирования
def func(spam, eggs, toast=0, ham=0):
    print((spam, eggs, toast, ham))


func(1, 2)
func(1, ham=1, eggs=0)
func(spam=1, eggs=0)
func(toast=1, eggs=2, spam=3)
func(1, 2, 3, 4)

print('\n')


# Примеры произвольного количества аргументов
# Заголовки: сбор аргументов
def f(*args): print(args)


f()
f(1)
f(1, 2, 3, 4)


def f(**args): print(args)


f()
f(a=1, b=2)

print()


def f(a, *pargs, **kargs): print(a, pargs, kargs)


f(1, 2, 3, x=1, y=2)

print('\n')


# Вызовы: распаковка аргументов
def func(a, b, c, d): print(a, b, c, d)


args = (1, 2)
args += (3, 4)
func(*args)

args = {'a': 1, 'b': 2, 'c': 3}
args['d'] = 4
func(**args)

print()

# Примеры комбинирования
func(*(1, 2), **{'d': 4, 'c': 3})
func(1, *(2, 3), **{'d': 4})
func(1, c=3, *(2,), **{'d': 4})
func(1, *(2, 3), d=4)
func(1, *(2,), c=3, **{'d': 4})

print('\n')


# Аргументы с передачей только по ключевым словам
def kwonly(a, *b, c):
    print(a, b, c)


kwonly(1, 2, c=3)
kwonly(a=1, c=3)

# kwonly(1, 2, 3) - TypeError: kwonly() missing 1 required keyword-only argument: 'c'

print()


# Сам по себе символ ★ означает, что функция не принимает список аргументов переменной длины
# Но по-прежнему ожидает передачи всех аргументов, следующих за символом ★, по ключевому слову
def kwonly(a, *, b, c):
    print(a, b, c)


kwonly(1, c=3, b=2)
kwonly(c=3, b=2, a=1)
# kwonly(1, 2, 3) - TypeError: kwonly() takes 1 positional argument but 3 were given
# kwonly(1) - TypeError: kwonly() missing 2 required keyword-only arguments: 'b' and 'c'

print()


# Использование стандартных значений для аргументов с обязательным ключевым словом
def kwonly(a, *, b='spam', c='ham'):
    print(a, b, c)


import sys


def new_print(*args, file=sys.stdout, sep=' ', end='\n'):
    text = ''
    for arg in args:
        text = text + str(arg) + sep
    text = text + end
    file.write(text)


new_print('poop', 'in', ('my',), ['soup', 1])

kwonly(1)
kwonly(1, c=3)
kwonly(a=1)
kwonly(c=3, b=2, a=1)
# kwonly(c=3, b=2, 1) - SyntaxError: positional argument follows keyword argument
# kwonly(1, 2) - TypeError: kwonly() takes 1 positional argument but 2 were given

print('\n')


# Правила упорядочения

# Аргументы с передачей только по ключевым словам должны указываться после одиночной звездочки, а не двух
# def kwonly(a, **params, b, c): pass - SyntaxError: invalid syntax
# def kwonly(a, **, b, c): pass - SyntaxError: invalid syntax

# Аргументы с передачей только по ключевым словам должны записываться между ★ и ★★
# def f(a, *b, **d, c=6): pass - SyntaxError: invalid syntax
def f(a, *b, c=6, **d):
    print(a, b, c, d)


f(1, 2, 3, x=4, y=5)
f(1, 2, 3, x=4, y=5, c=7)
f(1, 2, 3, x=4, c=7, y=5)


# f(c=7, 1, 2, x=5) - SyntaxError: positional argument follows keyword argument


def f(a, c=6, *b, **d):  # Здесь с - не аргумент с передачей только по ключевым словам!
    print(a, b, c, d)


f(1, 2, 3, x=4)

print()


# В вызовах функций keyword-only argument должен располагаться:
def f(a, *b, c=6, **d):
    print(a, b, c, d)


# 1. Между позиционными и ★
f('aaa', c='ccc', *('bbb', 'bbb'), **{'ddd': 'ddd'})
# 2. Между ★ и ★★
f('aaa', *('bbb', 'bbb'), c='ccc', **{'ddd': 'ddd'})
# 3. Внутри ★★
f('aaa', *('bbb', 'bbb'), **dict(ddd='ddd', c='ccc'))

print('\n\n\n')


# Обобщенные функции для работы с множествами
def intersect(*args):
    res = []
    for x in args[0]:
        if x in res: continue
        for other in args[1:]:
            if x not in other: break
        else:
            res.append(x)
    return res


def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)
    return res


s1, s2, s3 = 'SPAM', 'SCAM', 'SLAM'

print(intersect(s1, s2, s3))  # Возвращает список из элементов существующих в каждой последовательности
print(union(s1, s2, s3))  # Возвращает список элементов, существующих хотя-бы в одной последовательности

print(intersect([1, 2], [1, 3, 6]))
print(union([1, 2], [1, 3, 6]))

print()


def tester(func, items, trace=True):
    for i in range(len(items)):
        items = items[1:] + items[:1]
        if trace: print(items)
        print(sorted(func(*items)))


tester(intersect, ('a', 'abcdefg', 'abdst', 'albmcnd'))
tester(union, ('a', 'abcdefg', 'abdst', 'albmcnd'), False)
tester(intersect, ('ba', 'abcdefg', 'abdst', 'albmcnd'), False)
