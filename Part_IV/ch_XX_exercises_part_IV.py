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
    return {key: value for key, value in zip(zip(dict1, dict1.values()), zip(dict2, dict2.values()))}


D1 = {'a': 1, 'b': 2, 'c': 3}
D2 = {'e': 4, 'f': 5, 'g': 6}
print(list(zip(D1, D1.values())))
print(list(zip(D2, D2.values())))
print(list(zip(zip(D1, D1.values()), zip(D2, D2.values()))))

print()

print(add_dict(D1, D2))

# 7. Дополнительные примеры сопоставления аргументов.
# 8. Снова простые числа.
# 9. Итерации и включения.
# 10. Измерение времени выполнения инструментов.
# 11. Рекурсивные функции.
# 12. Вычисление факториалов.
