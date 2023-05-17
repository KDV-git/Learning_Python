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
