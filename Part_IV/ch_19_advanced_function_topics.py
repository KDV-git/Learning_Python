# Рекурсивные функции
def mysum(lst):
    if not lst:
        return 0
    else:
        print(lst)
        return lst[0] + mysum(lst[1:])


L = [1, 2, 3, 4, 5]

print(mysum(L), end='\n\n')


# Альтернативные варианты
# Тернарное выражение
def mysum(lst):
    return 0 if not lst else lst[0] + mysum(lst[1:])


print(mysum(L))


# print(mysum(['s', 'p', 'a', 'm'])) - TypeError: can only concatenate str (not "int") to str


# Для любых элементов поддерживающих + (хотя-бы с одним элементом)
def mysum(lst):
    return lst[0] if len(lst) == 1 else lst[0] + mysum(lst[1:])


print(mysum(L))
print(mysum(['s', 'p', 'a', 'm']))


# Расширенное присваивание последовательности, работает с любыми итерируемыми объектами (хотя-бы с одним элементом)
def mysum(lst):
    first, *rest = lst
    return first if not rest else first + mysum(rest)


print(mysum(L))
print(mysum('spam'), end='\n\n')


# Пример косвенной рекурсии
def mysum(lst):
    if not lst: return 0
    return nonempty(lst)


def nonempty(lst):
    return lst[0] + mysum(lst[1:])


print(mysum([1.1, 2.2, 3.3, 4.4]), end='\n\n')

# Операторы цикла или рекурсия
L = [1, 2, 3, 4, 5]
summ = 0

while L:
    summ += L[0]
    L = L[1:]

print(summ)

# Цикл for ещё лучше

L = [1, 2, 3, 4, 5]
summ = 0

for num in L:
    summ += num

print(summ, end='\n\n')

# Обработка произвольных структур (цикл for тут не поможет)
L = [1, [2, [3, 4], 5], 6, [7, 8]]


# for num in L: summ += num - TypeError: unsupported operand type(s) for +=: 'int' and 'list'

def sumtree(lst):
    tot = 0
    for x in lst:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot


print(sumtree(L))

# Патологические случаи
print(sumtree([1, [2, [3, [4, [5]]]]]))
print(sumtree([[[[[1], 2], 3], 4], 5]))

print('\n')


# Рекурсия или очереди и стеки (лучше рекурсия)
def sumtree(lst):
    tot = 0
    items = list(lst)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            items.extend(front)
    return tot


# Защита от циклов
#
# В рекурсивных функциях
# if stste not in visited:
#   visited.add(state)
#   ...обработка...
#
# В нерекурсивных альтернативах
# visited.add(front)
#   ...обработка...
# items.extend([x for x in front if x not in visited])
#
# Также необходимо учитывать ограничение глубины стека вызовов
# import sys
# sys.getrecursionlimit()
# help(sys.getrecursionlimit())

print('\n')


# Объекты функций: атрибуты и аннотации
# Косвенные вызовы функций: "первоклассные" объекты

# Функция - это объект, её имя - это переменная
def echo(message):
    print(message)


echo('Direct call')
x = echo
x('x-Direct call')
print(x is echo)

print()


# Функцию как и любой объект можно передать как аргумент другой функции
def indirect(func, arg):
    func(arg)


indirect(echo, 'Argument call')
indirect(x, 'x-Argument call')

print()

# Функции могут помещаться внутрь структур данных
schedule = [(echo, 'Spam!'), (x, 'x-Spam!')]

for func, arg in schedule:
    func(arg)

print()


# Функции можно создавать и возвращать в других функциях (замыкания(фабричная функция)
def make(label):
    def echo(message):
        print(label + ':' + message)

    return echo


F = make('Spam')
F('Ham!')
F('Eggs!')

# Функция - это универсальная первоклассная объектная модель!

print('\n')


# Интроспекция функций
def func(a):
    b = 'spam'
    return b * a


print(func(8))
print(func.__name__)
print(dir(func))


def dirring(obj):
    count = 0
    print(f'\n\nList of attribute for {obj}:')
    try:
        for atr in dir(obj):
            if count == 10:
                print()
                print(atr, end=' | ')
                count = 0
            else:
                print(atr, end=' | ')
                count += 1
    except AttributeError:
        print('Ops AttributeError for object')
    finally:
        print('\n\n')


dirring(func)

print(func.__code__)
dirring(func.__code__)
print(func.__code__.co_varnames)
print(func.__code__.co_argcount)

print('\n')

# Атрибуты функций (присоединяются к объекту функции)
print(func)
func.count = 0
func.count += 1
print(func.count)
func.handles = 'Button-Press'
print(func.handles)
dirring(func)

poop = func
dirring(poop)
dirring(dirring)

print(len(dir(func)))
print(len([x for x in dir(func) if not x.endswith('__')]))
print([x for x in dir(func) if not x.endswith('__')])

# Атрибуты классные (информации о состоянии like "статические локальные переменные")

print('\n')


# Аннотации функций

# Аннотирующая информация — произвольные определяемые пользователем данные об аргументах и результате функции
# Они совершенно необязательны и когда присутствуют, то просто присоединяются к атрибуту __ annotations__

def func(a, b, c):
    return a + b + c


print(func(1, 2, 3))


# Качественная аннотация
def func(a: int, b: int, c: int) -> int:
    return a + b + c


print(func.__annotations__)


# Аннотация уровня ну типа
def func(a: 'spam', b: (1, 2), c: float) -> int:
    return a + b + c


print(func.__annotations__)
print(type(func.__annotations__))

print()

# По сути аннотация - это объект (словарь(dict)) присоединённый к объекту (функция(func))
print(func.__annotations__.items())

for x in func.__annotations__.items(): print(x)

print()


# Стандартные значения аргументов указываются после аннотации
def func(a: 'spam' = 4, b: (1, 10) = 5, c: float = 6) -> int:
    return a + b + c


print(func(1, 2, 3))
print(func())
print(func(1, c=10))

# Пробелы не обязательны (не надо)

# def func(a:'spam'=4,b:(1,10)=5,c:float=6)->int:
#     return a+b+c

print('\n\n')


# Анонимные функции: выражения lambda

# Сравнение с def
def func(x, y, z): return x + y + z


print(func(2, 3, 4))

F = lambda x, y, z: x + y + z

print(F(2, 3, 4))

# Использование стандартных значений
x = lambda a='fee', b='fie', c='foe': a + b + c

print(x('wee'))


# Правила поиска в областях видимости (LEGB) для выражения lambda полностью соответствуют оператору def
def knights():
    title = 'Sir'
    action = (lambda x: title + ' ' + x)
    return action


act = knights()
print(act('Bagel'))

print()

# Для чего используется выражение lambda?

# Обработчики обратных вызовов часто записываются как внутристрочные выражения lambda (см. далее)

# Выражения lambda также широко используются при реализации таблиц переходов (списки или словари действий)
L = [lambda x: x ** 2,
     lambda x: x ** 3,
     lambda x: x ** 4]

for f in L:
    print(f(2))

print(L[1](3))

# Эквивалентный код с def потребовал бы временных имен функций (они могли бы конфликтовать с остальными именами)

print()

# Переключатели для множественного ветвления: окончание
key = 'got'
D = {'already': (lambda: 2 + 2),
     'got': lambda: 2 * 4,
     'one': lambda: 2 * 6}

print(D[key])
print(D[key]())

# Кодовая близость, обеспечиваемая выражениями lambda, очень полезна для функций, используемых только в одном контексте

print()

# Как (не) запутать свой код на Python (лучше не надо)
lower = (lambda x, y: x if x < y else y)
print(lower('bb', 'aa'))
print(lower(22, 33))

print()

# Циклы внутри lambda (вызовы map и списковые включения)
import sys

showall = lambda x: list(map(sys.stdout.write, x))

L = ['spam\n', 'eggs\n', 'ham\n']
t = showall(L)

print(t)  # Write возвращает количество записанных символов
print(type(t))

print()

# То же самое через списковое включение
showall = lambda x: [sys.stdout.write(line) for line in x]

t = showall(L)

print(t)
print(type(t))

print()

# Эквивалент через print (Но будет возвращён лист из None)
showall = lambda x: [print(line, end='') for line in x]

t = showall(L)

print(t)
print(type(t))

print()

# Вариант print без спискового включения (Но будет возвращен один объект None)
showall = lambda x: print(*x, sep='')

t = showall(L)

print(t)
print(type(t))

print('\n\n')


# Выражения lambda также могут быть вложенными
def action(x):
    return (lambda y: x + y)


act = action(99)

print(act)
print(act(2))

# То же самое через
action = (lambda x: (lambda y: x + y))
act = action(99)

print(act)
print(act(2))

print('\n')

# Обратные вызовы lambda
# С модулем tkinter, предназначенным для создания графических пользовательских интерфейсов
from tkinter import Button, mainloop

x = Button(text='Press me',
           command=(lambda: sys.stdout.write('Spam\n')))

x.pack()
mainloop()

print('\n')

# Python сочетает в себе поддержку множества парадигм программирования:
# 1. Процедурная (посредством своих базовых операторов)
# 2. Объектно-ориентированная (с помощью классов)
# 3. Функциональная

# Инструменты функционального программирования
# Отображение функций на итерируемые объекты: map
counters = [1, 2, 3, 4, 5]


def inc(x): return x + 10


print(list(map(inc, counters)))
print(list(map((lambda x: x + 3), counters)))


# Эквивалент функции map через оператор def
def mymap(func, seq):
    res = []
    for x in seq: res.append(func(x))
    return res


print(list(map(inc, [1, 2, 3])))
print(mymap(inc, [1, 2, 3]))

print()

print(pow(3, 4))
print(list(map(pow, [1, 2, 3], [2, 3, 4])))  # map ожидает функцию с N аргументами для N последовательностей

# Сравнение со списковыми включениями
print(list(map(inc, [1, 2, 3, 4])))
print([inc(x) for x in [1, 2, 3, 4]])

# В ряде случаев map способна выполняться быстрее, чем списковое включение (когда отображается встроенная функция)
# Однако map требует функцию, а не произвольное выражение

print('\n')

# Выбор элементов из итерируемых объектов: filter

# Выбирает элементы из итерируемых объектов на основе проверочной функции
print(list(range(-5, 5)))
print(list(filter((lambda x: x > 0), range(-5, 5))))

# Эквивалент с применением цикла for
res = []

for x in range(-5, 5):
    if x > 0:
        res.append(x)

print(res)

# Эквивалент с применением спискового включения
print([x for x in range(-5, 5) if x > 0])

print('\n')

# Комбинирование элементов из итерируемых объектов: reduce
from functools import reduce

print(reduce((lambda x, y: x + y), [1, 2, 3, 4]))
print(reduce((lambda x, y: x * y), [1, 2, 3, 4]))

print()

# Эквивалент через цикл for
L = [1, 2, 3, 4]
res = L[0]

for x in L[1:]:
    res += x

print(res)

print()


# Эквивалент через оператор def
def myreduce(func, seq):
    res = seq[0]
    for x in seq[1:]:
        res = func(res, x)
    return res


print(myreduce((lambda x, y: x + y), [1, 2, 3, 4]))
print(myreduce((lambda x, y: x * y), [1, 2, 3, 4]))
