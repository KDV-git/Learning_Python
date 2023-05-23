# Упражнения для части IV
# 1. Основы.
def func(x):
    print(x)


func(1)
func([1, 2, 3])
func('spam')
func({'s': 1, 'p': 2, 'a': 3, 'm': 4})
# func() - TypeError: func() missing 1 required positional argument: 'x'
# func(1, 2) - TypeError: func() takes 1 positional argument but 2 were given
func((1, 2))

print('\n')


# 2. Аргументы.
def adder(a, b):
    return a + b


print(adder(5, 10))
print(adder('sp', 'am'))
print(adder([1, 2], [3, 4]))
print(adder(1.2, 3.4))

print('\n')


# 3. Переменное количество аргументов.
def adder(*args):
    res = args[0]
    try:
        for item in args[1:]:
            res += item
        return res
    except TypeError:
        return '\'TypeError: Unsupported operand type(s) for +=\''


print(adder(5, 10, 15))
print(adder('sp', 'am', '-', 'ham'))
print(adder([1, 2], [3, 4], [5]))
print(adder(1.2, 3.4, 5.6, 7.8, 9.1))
print(adder(1.2, 1, 50))

# Error
print(adder(1.2, 's'))
print(adder(10, [20, 30], '40'))
print(adder({'a': 1, 'b': 2, 'c': 3}, {'e': 4, 'f': 5, 'g': 6}))
print(adder({'a': 1, 'b': 2, 'c': 3}.values(), {'e': 4, 'f': 5, 'g': 6}.values()))

print('\n')


# 4. Ключевые аргументы.
def adder(good=5, bad=2, ugly=3):
    return good + bad + ugly


print(adder())
print(adder(ugly=1, good=2))
print(adder(1, 2, 3))
print(adder(1))
print(adder('good', 'bad', 'ugly'))

# print(adder(1, 2, 3, 4)) - TypeError: adder() takes from 0 to 3 positional arguments but 4 were given
# print(adder('good', 'bad')) - TypeError: can only concatenate str (not "int") to str

print()


def adder(**kargs):
    val = list(kargs.values())
    res = val[0]
    for item in val[1:]:
        res += item
    return res


D = {'e': 4, 'f': 5, 'g': 6}
print(adder(a=1, b=2, c=3))
print(adder(**D))
print(adder(**{'a': 1, 'b': 2, 'c': 3}))

# Error
# print(adder(*D)) - TypeError: adder() takes 0 positional arguments but 3 were given
# print(adder({'a': 1, 'b': 2, 'c': 3})) - TypeError: adder() takes 0 positional arguments but 1 was given

print('\n')


# 5. Словарные инструменты.
def copy_dict(dict):
    new_dict = {}
    for key in dict.keys():
        new_dict[key] = dict[key]
    return new_dict


D = {'a': 1, 'b': 2, 'c': 3, 'e': 4, 'f': 5, 'g': 6}
new_D = copy_dict(D)
print(new_D)
print(new_D is D)

print()


def copy_dict2(dict):
    return {key: dict[key] for key in dict.keys()}


D = {'a': 1, 'b': 2, 'c': 3, 'e': 4, 'f': 5, 'g': 6}
new_D = copy_dict2(D)
print(new_D)
print(new_D is D)

print('\n')


# 6. Словарные инструменты.
def add_dict(dict1, dict2):
    return {key: value for key, value in
            zip((list(dict1) + list(dict2)), (list(dict1.values()) + list(dict2.values())))}


D1 = {'a': 1, 'b': 2, 'c': 3}
D2 = {'e': 4, 'f': 5, 'g': 6}
print(D1)
print(D2)

print(add_dict(D1, D2))


def add_dict2(dict1, dict2):
    res = dict1.copy()
    for key in dict2.keys():
        res[key] = dict2[key]
    return res


print(add_dict2(D1, D2))

print()


def add_dict3(dict1, dict2):
    res = dict1.copy()
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        for key in dict2.keys():
            res[key] = dict2[key]
    elif isinstance(dict1, list) and isinstance(dict2, list):
        res += dict2
    else:
        print("Sorry, unsupported type in argument!")
        res = None
    return res


print(add_dict3(D1, D2))
print(add_dict3([1, 2, 3], [4, 5, 6]))
print(add_dict3(D1, [1, 2, 3]))

print('\n')


# 7. Дополнительные примеры сопоставления аргументов.
def f1(a, b): print(a, b)


def f2(a, *b): print(a, b)


def f3(a, **b): print(a, b)


def f4(a, *b, **c): print(a, b, c)


def f5(a, b=2, c=3): print(a, b, c)


def f6(a, b=2, *c): print(a, b, c)


f1(1, 2)
f1(b=2, a=1)
f2(1, 2, 3)
f3(1, x=2, y=3)
f4(1, 2, 3, x=2, y=3)
f5(1)
f5(1, 4)
f6(1)
f6(1, 3, 4)

print('\n')

# 8. Снова простые числа.
y = 10
x = y // 2
while x > 1:
    if y % x == 0:
        print(y, 'has factor', x)
        break
    x -= 1
else:
    print(y, 'is prime')

print()


def is_prime(y):
    if y < 2:
        print("Error! (y < 2)")
        return None
    x = y // 2
    L = [num for num in range(2, int(x) + 1) if y % num == 0]
    if L:
        print(y, 'has factor', L[-1])
    else:
        print(y, 'is prime')


is_prime(10)
is_prime(11)
is_prime(20)
is_prime(13)
is_prime(13.0)
is_prime(15)
is_prime(15.0)

is_prime(0)
is_prime(-20)

print('\n')

# 9. Итерации и включения.
import math

L = [2, 4, 9, 16, 25]
new_L = []
for x in L:
    new_L.append(math.sqrt(x))

print(new_L)
print(list(map(math.sqrt, L)))
print([math.sqrt(x) for x in L])
print(list(math.sqrt(x) for x in L))

print('\n')

# 10. Измерение времени выполнения инструментов.
import timeit

print(sorted(timeit.repeat(setup='import math\nx = 123456789', stmt='math.sqrt(x)', number=100000, repeat=5)))
print(sorted(timeit.repeat(setup='x = 123456789', stmt='x ** 0.5', number=100000, repeat=5)))
print(sorted(timeit.repeat(setup='x = 123456789', stmt='pow(x, 0.5)', number=100000, repeat=5)))

print('\n')


# 11. Рекурсивные функции.
def countdown(x):
    if not x:
        return 'stop'
    else:
        print(x, end=' ')
        return countdown(x - 1)


print(countdown(5))

x = 5
print(*list(range(1, x + 1))[::-1], 'stop')
print(*list(range(x, 0, -1)), 'stop')

print('\n')

# 12. Вычисление факториалов.
import functools


def fact1(N=6):
    if not N:
        return 1
    else:
        return N * fact1(N - 1)


def fact2(N=6):
    return functools.reduce((lambda x, y: x * y), range(1, N + 1))


def fact3(N=6):
    res = 1
    while N > 1:
        res *= N
        N -= 1
    return res


def fact3_1(N=6):
    res = 1
    for i in range(1, N + 1):
        res *= i
    return res


def fact4(N=6):
    return math.factorial(N)


print(fact1(6))
print(fact2(6))
print(fact3(6))
print(fact3_1(6))
print(fact4(6))

print(fact1.__name__, (timeit.repeat(stmt=fact1, number=100000, repeat=5)))
print(fact2.__name__, sorted(timeit.repeat(stmt=fact2, number=100000, repeat=5, setup='import functools')))
print(fact3.__name__, sorted(timeit.repeat(stmt=fact3, number=100000, repeat=5)))
print(fact3_1.__name__, sorted(timeit.repeat(stmt=fact3_1, number=100000, repeat=5)))
print(fact4.__name__, sorted(timeit.repeat(stmt=fact4, number=100000, repeat=5, setup='import math')))
