import timeit

print(timeit.repeat(stmt='[x ** 2 for x in range(1000)]', number=1000, repeat=5))
print(min(timeit.repeat(stmt='[x ** 2 for x in range(1000)]', number=1000, repeat=5)))

# Команда для запуска из командной строки
# py -3 -m timeit -n 1000 -r 5 "[x ** 2 for x in range(1000)]"

print()

# Измерение времени выполнения многострочных операторов
stmt = '''
L = [1, 2, 3, 4, 5]
i = 0
while i < len(L):
    L[i] += 1
    i += 1'''

print(timeit.repeat(number=10000, repeat=3, stmt=stmt))
print(min(timeit.repeat(number=10000, repeat=3, stmt=stmt)))

print()

# Другие режимы использования: настройка, суммарное время и объекты

# Настройка
setup = '''
L = [1, 2, 3, 4, 5]
i = 0'''

stmt = '''
while i < len(L):
    L[i] += 1
    i += 1'''

print(timeit.repeat(number=10000, repeat=3, setup=setup, stmt=stmt))
print(min(timeit.repeat(number=10000, repeat=3, setup=setup, stmt=stmt)))

print()

stmt = '[x ** 2 for x in range(1000)]'

# Суммарное время
print(timeit.timeit(stmt=stmt, number=1000))

# API-интерфейс класса модуля
print(timeit.Timer(stmt=stmt).timeit(1000))

print()


# Вызываемые объекты или строки кода
def testcase():
    y = [x ** 2 for x in range(1000)]


print(timeit.repeat(stmt=testcase, number=1000, repeat=3))
print(min(timeit.repeat(stmt=testcase, number=1000, repeat=3)))
