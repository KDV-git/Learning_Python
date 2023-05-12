X = 99


def func(Y):
    Z = X + Y
    return Z


# Глобальные имена: X, func
# Локальные имена: Y, Z

# Встроенная область видимости
# В действительности встроенная область видимости представляет собой всего лишь встроенный модуль под названием builtins

import builtins

print(dir(builtins))
print(len(dir(builtins)), end='\n\n')
list_of_name = [[], [], [], [], [], [], [], [], [], [], [], [], [], []]
index = count = 0

for name in dir(builtins):
    if count < 10:
        list_of_name[index].append(name)
        count += 1
    else:
        index += 1
        count = 0

for lst in list_of_name:
    print(lst)
print()

print(zip)
print(builtins.zip)
print(zip is builtins.zip)
print()


# Переопределение встроенных имён (В основном не стоит, но иногда..)
def hider():
    open = 'spam'
    f = open('data.txt')


# Переопределение глобальных имён
X = 88


def func():
    X = 99
    print(X)


func()
print(X)

print('\n\n\n')

# Оператор global
X = 88


def func():
    global X
    X = 99
    print(X)


func()
print(X)

Y, Z = 1, 2


def all_global():
    global glob_X  # Если переменная не была объявлена ранее в модуле, то global создаст её
    glob_X = Y + Z
    print(glob_X)


all_global()
print(glob_X)

print('\n')

# Глобальные изменения в обход global
import ch_17_1_global_scopes_test

ch_17_1_global_scopes_test.test()
print(ch_17_1_global_scopes_test.var)

print('\n')

# Области видимости и вложенные функции
X = 99


def f1():
    X = 88

    def f2():
        print(X)

    f2()


f1()

print()


# Поиск в объемлющей области видимости работает, даже если уже произошел возврат из объемлющей функции
def f1():
    X = 88

    def f2():
        print(X)

    return f2  # Возвращает объект функции f2, но не взывает её


action = f1()
action()  # Происходит вызов функции f2

print('\n')


# Фабричные функции: замыкания
def maker(N):
    def action(X):
        return X ** N

    return action


f = maker(2)
print(f(3), f(4), sep='\n', end='\n\n')

g = maker(3)
print(g(3), g(4), sep='\n', end='\n\n')


# Аналогичная функция с использованием lambda
def maker(N):
    return lambda X: X ** N


sigma = 2
alpha = 8.3

f_res = maker(sigma)
a1 = f_res(alpha)
print(a1)

if a1 < 50:
    sigma += 2
    alpha -= 1
else:
    sigma += 1
    alpha += 1

s_res = maker(sigma)
a1 = f_res(alpha)
a2 = s_res(alpha)
print(a1, a2)

if a2 < 500:
    sigma += 2
    alpha -= 1
else:
    sigma += 1
    alpha += 1

t_res = maker(sigma)
a1 = f_res(alpha)
a2 = s_res(alpha)
a3 = t_res(alpha)
print(a1, a2, a3)

print('\n\n\n')


# Сохранение состояния из объемлющей области видимости с помощью стандартных значений
def f1():
    X = 88

    def f2(X=X):
        print(X)

    f2()


f1()


# Эквивалент, в котором отсутствует вложение
def f1():
    x = 88
    f2(x)


# f1() - NameError: name 'f2' is not defined

def f2(x):
    print(x)


f1()

print('\n')


# Вложенные области видимости, стандартные значения и выражения lambda
def func():
    x = 4
    act = (lambda n: x ** n)  # Выражение lambda вводит новую локальную область видимости для функции, которую создает
    return act


x = func()
print(x(2))


# Передача х вручную (устаревший способ)
def func():
    x = 4
    act = (lambda n, x=x: x ** n)
    return act


x = func()
print(x(2))

print('\n')

# Переменные цикла могут требовать стандартные значения, а не области видимости
