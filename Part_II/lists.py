# Примеры работы со списками
lst = [*range(-2, 3)]
abs_lst = [abs(x) for x in lst]
map_lst = list(map(abs, lst))
print(lst)
print(abs_lst)
print(map_lst)

print('\n')

# Присваивания по индексам и срезам
L = ['spam', 'Spam', 'SPAM!']
print(L)
L[0:2] = ['eat', 'more']
print(L)

print('\n')

L = [1, 2, 3]
print(L)
L[1:2] = [4, 5]
print(L)
L[1:1] = [6, 7]
print(L)

print('\n')

L = [0, 1]
print(L)
L[:0] = [2, 3, 4]
print(L)

print('\n')

# Дополнительные сведения о сортировке списков
L = ['abc', 'ABD', 'aBe']
print(L)
L.sort()
print(L)

print('\n')

L = ['abc', 'ABD', 'aBe']
print(L)
L.sort(key=str.lower)
print(L)

print('\n')

L = ['abc', 'ABD', 'aBe']
print(L)
L.sort(key=str.lower, reverse=True)
print(L)

print('\n')

# Сортировка с помощью встроенной функции
L = ['abc', 'ABD', 'aBe']
print(f'L = {L}')
sort_lst = sorted(L, key=str.lower, reverse=True)
print(f'L = {L}')
print(f'sort_lst = {sort_lst}')

print('\n')

L = ['abc', 'ABD', 'aBe']
print(f'L = {L}')
sort_lst = sorted([x.lower() for x in L], reverse=True)
print(f'L = {L}')
print(f'sort_lst = {sort_lst}')

print('\n')

# Примеры других списковых методов
L = ['spam', 'eggs', 'ham']
print(L)
print(f'\'eggs\' index = {L.index("eggs")}')
L.insert(1, 'toast')
print(L)

print('\n')

L = ['spam', 'eggs', 'ham', 'toast']
print(L)
del L[0]
print(L)
del L[1:]
print(L)

print('\n')

L = ['Already', 'got', 'one']
L[1:] = []
print(L)
print(len(L))
L[0:] = []
print(L)
print(len(L))

print('\n')

# Беглый взгляд на копирование списков
L = [1, 2, 3, 4, 5]
L2 = L.copy()
L3 = L[:]
L4 = list(L)

print(L)
print(L2)
print(L3)
print(L4)

print(L2 is L)
print(L3 is L)
print(L4 is L)

print('\n')

# Уровни глубины
L = [4, 5, 6]
X = L * 4
Y = [L] * 4

print(L)
print(X)
print(Y)

print('\n')

L[1] = 0

print(L)
print(X)
print(Y)

print('\n')

L = [4, 5, 6]
Y = [list(L)] * 4
L[1] = 0

print(L)
print(Y)

Y[0][1] = 99
print(Y)

print('\n')

L = [4, 5, 6]
Y = [list(L) for i in range(4)]
print(Y)

Y[0][1] = 99
print(Y)
