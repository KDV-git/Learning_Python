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
del f1
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
def make_actions():
    acts = []
    for i in range(5):  # Попытка запомнить каждое значение i
        acts.append(lambda x: i ** x)
    return acts


# На практике все функции запоминают последние значение i!
acts = make_actions()
print(acts[0](2))
print(acts[1](2))
print(acts[2](3))
print(acts[3](3))

# Код не работает — из-за того, что переменная из объемлющей области видимости ищется, когда функции вызываются
# (после завершения цикла, т.е. когда i=4)

print()


# Решение, которое исправляет эту проблему:
def make_actions():
    acts = []
    for i in range(5):  # Стандартные значения оцениваются при создании вложенных функций
        acts.append(lambda x, i=i: i ** x)  # (а не при вызове их в более позднее время)
    return acts


acts = make_actions()
print(acts[0](2))
print(acts[1](2))
print(acts[2](3))
print(acts[3](3))

print()


# Произвольное вложение областей видимости (не стоит)
def f1():
    x = 99

    def f2():
        def f3():
            print(x)  # Находится в локальной области видимости fl!

        f3()

    f2()


f1()

print('\n\n\n')

# Оператор nonlocal
# nonlocal no_glob - SyntaxError: nonlocal declaration not allowed at module level
x = 1000


def func():
    x = 10

    def func2():
        nonlocal x
        x += 1
        print(x)

    print(x)
    func2()


print(x)
func()
print(x, end='\n\n\n')


# Примеры
def tester(start):
    state = start

    def nested(label):
        # state += 1 - UnboundLocalError: local variable 'state' referenced before assignment
        nonlocal state
        state += 1
        print(label, state)

    return nested


F = tester(0)
F('spam')
F('ham')
F('eggs')

print()

G = tester(42)
G('spam')
G('ham')
F('bacon')

# В функции замыкания нелокальные переменные являются данными с множеством копий для каждого вызова.

print()


# Перечисленным именам действительно должны быть присвоены значения в области видимости объемлющего def
def tester(start):
    def nested(label):
        # nonlocal state - SyntaxError: no binding for nonlocal 'state' found
        state = 0
        print(label, state)

    return nested


# Нелокальные переменные НЕ ищутся в глобальной области видимости или в области видимости за пределами всех def
spam = 99


def tester():
    def nested(label):
        # nonlocal spam - SyntaxError: no binding for nonlocal 'spam' found
        spam = 0
        print(label, spam)

    return nested


# Варианты сохранения состояния

# 1. Состояние с помощью оператора nonlocal
def tester(start):
    state = start

    def nested(label):
        nonlocal state
        print(label, state)
        state += 1

    return nested


F = tester(0)  # Переменная state видима только внутри замыкания
F('spam')
# F.state - AttributeError: 'function' object has no attribute 'state'

print('\n')


# Состояние с помощью глобальных переменных: только одиночная копия (не стоит)
def tester(start):
    global state
    state = start

    def nested(label):
        global state
        print(label, state)
        state += 1

    return nested


F = tester(0)
F('spam')
F('eggs')

G = tester(42)  # Сбрасывает единственную копию state в глобальной
G('toast')
G('bacon')
F('ham')  # Счетчик был перезаписан!

print('\n')


# Состояние с помощью классов: явные атрибуты (предварительный обзор)
class tester:
    def __init__(self, start):
        self.state = start

    def nested(self, label):
        print(label, self.state)
        self.state += 1


F = tester(0)
F.nested('spam')
F.nested('ham')

G = tester(42)  # Сбрасывает единственную копию state в глобальной
G.nested('toast')
G.nested('bacon')
F.nested('ham')


# Функция __call__ перехватывает прямые обращения к экземпляру
class tester:
    def __init__(self, start):
        self.state = start

    def __call__(self, label):
        print(label, self.state)
        self.state += 1


H = tester(99)
H('juice')
H('pancakes')

print('\n')


# Состояние с помощью атрибутов функций
def tester(start):
    def nested(label):
        print(label, nested.state)
        nested.state += 1

    nested.state = start  # Инициализация состояния после определения функции
    return nested


F = tester(0)
F('spam')
F('ham')
print(F.state)  # Доступ к состоянию извне функции

G = tester(42)
G('toast')
G('bacon')

print(F.state)
print(G.state)
print(F is G)


# Состояние с помощью изменяемых объектов: неотчетливый призрак прошлого Python? (НЕ НАДО!)
def tester(start):
    def nested(label):
        print(label, state[0])
        state[0] += 1

    state = [start]
    return nested


# Не надо.

print('\n\n\n')


# Настройка open
def makeopen(id):
    original = builtins.open

    def custom(*pargs, **kargs):
        print('Custom open call %r:' % id, pargs, kargs)
        return original(*pargs, **kargs)

    builtins.open = custom


path = 'D:\\Python\\Projects\\Learning_Python\\Part_III\\test2.txt'

F = open(path)
print(F.read(), end='\n\n')

makeopen('spam')
F = open(path)
print(F.read(), end='\n\n')

makeopen('eggs')
F = open(path)
print(F.read(), end='\n\n')
