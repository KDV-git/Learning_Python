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

