# Примеры операций над кортежами
T = tuple('spam')
print(T)

T = (1,)
X = (1)
print(X)
print(type(X))
print(T)
print(type(T))

T = 1, 2, 3, 4, 5, 6, 7
print(T)
print(type(T))

T = (1, 2) + (3, 4)
print(T)

T = (1, 2) * 4
print(T)

T = (1, 2, 3, 4)
print(T[0], T[1:3])

print('\n')

# Сортировка кортежей
T = (3, 2, 4, 1, 6, 5)
print(T)
print(type(T))

T = sorted(T)
print(T)
print(type(T))

T = tuple(sorted(T))
print(T)
print(type(T))

print('\n')

# Методы кортежей
T = (1, 2, 3, 2, 4, 2)
print(T.index(2))
print(T.count(2))

print('\n')

# Неизменяемость кортежей работает только на верхнем уровне(вложенные объекты можно изменять)
T = (1, [2, 3], 4)
print(T)
T[1][0] = 'spam'
print(T)

print('\n')

# Именованные кортежи (смесь кортежа, класса и словаря)
from collections import namedtuple

Rec = namedtuple('Rec', ['name', 'age', 'jobs'])
bob = Rec(name='Bob', age=40.5, jobs=['dev', 'mgr'])

print(bob)
print(type(bob))
print((bob[0], bob[2]))
print(bob.name, bob.jobs)

print('\n')

# Преобразование в словарь
O_dict = bob._asdict()
print(O_dict)
print(type(O_dict))
