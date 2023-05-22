# Локальные имена распознаются статически (Когда компилирует код def)
X = 99


def selector():
    print(X)


selector()


def selector():
    print(X)
    X = 88


# selector() - UnboundLocalError: cannot access local variable 'X' where it is not associated with a value

# ! На стадии компиляции Python видит присваивание X и решает, что X будет локальным именем повсюду в функции !

def selector():
    global X
    print(X)
    X = 88  # X изменяется уже в глобальной области видимости


selector()

print()

# Если действительно намерение состояло в том, чтобы вывести глобальную переменную,
# а затем установить локальную переменную с тем же именем, тогда придется импортировать включающий модуль.
X = 99


def selector():
    import __main__
    print(__main__.X)
    X = 88
    print(X)


selector()

print('\n')


# Стандартные значения и изменяемые объекты
def saver(x=[]):
    x.append(1)
    print(x)


saver([2])
saver()
saver()
saver()
saver([2])
saver([2])
saver()

x = saver
x()

print()


# Если так не надо
def saver(x=None):
    if x == None:
        x = []
    x.append(1)
    print(x)


saver([2])
saver()
saver()

print()


# Замена if?
def saver(x):
    x = x or []
    x.append(1)
    print(x)


poop = []
print(poop)
saver(poop)
print(poop)

print()


# Использование атрибутов функций
def saver():
    saver.x.append(1)
    print(saver.x)


# saver() - AttributeError: 'function' object has no attribute 'x'

saver.x = 1
# saver() - AttributeError: 'int' object has no attribute 'append'

saver.x = []
saver()
saver()
saver()

print()


# Функции без операторов return возвращают None
def shows(x):
    print(x)


F = shows('spam')
print(F)
