# 1. Основы
print(2 ** 16)
print(2 / 5, 2 / 5.0)
print('spam' + 'eggs')
S = 'ham'
print('eggs' + S)
print(S * 5)
print(S[:0])
print('green %s and %s' % ('eggs', S))
print('green {0} and {1}'.format('eggs', S))

print('\n')

print(('x',)[0])
print(('x', 'y')[1])
L = [1, 2, 3] + [4, 5, 6]
print(L, L[:], L[:0], L[-2], L[-2:])
print(([1, 2, 3] + [4, 5, 6])[2:4])
print([L[2], L[3]])
L.reverse()
print(L)
L.sort()
print(L)
print(L.index(4))

print('\n')

print({'a': 1, 'b': 2}['b'])
D = {'x': 1, 'y': 2, 'z': 3}
print(D)
D['w'] = 0
print(D)
print(D['x'] + D['w'])
D[(1, 2, 3)] = 4
print(D)
print(list(D.keys()))
print(list(D.values()))
print((1, 2, 3) in D)
print([[]])
print(['', [], (), {}, None])

print('\n' * 3)

# 2. Индексация и нарезание
L = [0, 1, 2, 3]
# print(L[4]) - IndexError: list index out of range
print(L[-1000:1000])
print(L[3:1])

print('\n' * 3)

# 3. Индексация, нарезание и оператор del
L = ['one', 'two', 'three', 'four']
print(L)
L[2] = []
print(L)
L[2:3] = []
print(L)
# L[1:2] = 1 - TypeError: can only assign an iterable

print('\n')

L = ['one', 'two', 'three', 'four']
print(L)
del L[0]
print(L)
del L[1:]
print(L)

print('\n' * 3)

# 4. Присваивание кортежам
X = 'spam'
Y = 'eggs'
print(X, Y)
X, Y = Y, X
print(X, Y)

print('\n' * 3)

# 5. Ключи словарей
D = {}
print(D)
D[1] = 'a'
D[2] = 'b'
D[(1, 2, 3)] = 'c'
print(D)

print('\n' * 3)

# 6. Индексация словарей
D = {'a': 1, 'b': 2, 'c': 3}
print(D)
# print(D['d']) - KeyError: 'd'
D['d'] = 'spam'
print(D)

print('\n' * 3)

# 7. Универсальные операции
# print('spam' + 1) - TypeError: can only concatenate str (not "int") to str
# print({'a': 1, 'b': 2} + {'c': 3, 'd': 4}) - TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# print({'a': 1, 'b': 2} + (1, 2)) - TypeError: unsupported operand type(s) for +: 'dict' and 'tuple'
# S = 'spam'
# S.append('poop') - AttributeError: 'str' object has no attribute 'append'
# L = [1, 2, 3]
# print(L.keys()) - AttributeError: 'list' object has no attribute 'keys'

print('\n' * 3)

# 8. Индексация строк
S = 'spam'
print(S)
print(S[0][0][0][0][0])
L = ['s', 'p', 'a', 'm']
print(L)
print(L[0][0][0][0][0])

print('\n' * 3)

# 9. Неизменяемые типы
S = 'spam'
print(S)
S = S[:1] + 'l' + S[2:]
print(S)
S = 'spam'
print(S)
S = S[0] + 'l' + S[2] + S[3]
print(S)
# S[1] = 'l' - TypeError: 'str' object does not support item assignment

print('\n' * 3)

# 10. Вложение
D = {'name': {'first': 'Даниил', 'middle': 'Валерьевич', 'last': 'Кононов'}, 'age': 25, 'job': None, 'address': 'USSR',
     'email': 'poop_in_the_soup@kekis.lol', 'phone': '8(800)555-35-35'}
print(D)
print(' '.join(list(D['name'].values())))
print(f"Возраст: {D['age']}")
print(D['email'])

print('\n' * 3)

# 11. Файлы
F = open('myexercisesfile.txt', 'w')
F.write('Hello file world!\n')
F.close()

# F = open('D:\\myexercisesfile.txt') - FileNotFoundError: [Errno 2] No such file or directory: 'D:\\myexercisesfile.txt'
F = open('myexercisesfile.txt')
print(F.read())
F.close()
