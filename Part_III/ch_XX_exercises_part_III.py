# 1. Написание базовых циклов.
S = 'spam'
# a
for c in S:
    print(ord(c), end=' ')
print()

# b
summ = 0
for c in S:
    summ += ord(c)
print(summ)

# c
L = []
for c in S:
    L.append(ord(c))
print(L)

print(list(map(ord, S)))
print([ord(c) for c in S])

print('\n')

# 2. Символы обратной косой, черты.
for i in range(50):
    print('hello %d\n\a' % i)

print('\n')

# 3. Сортировка словарей.
D = {'a': 1, 'e': 5, 'b': 2, 'd': 4, 'c': 3}
for item in sorted(D):
    print(item, D[item])

print('\n')

# 4. Альтернативные варианты программной логики.
L = [1, 2, 4, 8, 16, 32, 64]
X = 5
found = False
i = 0

while not found and i < len(L):
    if 2 ** X == L[i]:
        found = True
    else:
        i = i + 1
if found:
    print('at index', i)
else:
    print(X, 'not found')

# а
while i < len(L):
    if 2 ** X == L[i]:
        print('at index', i)
        break
    else:
        i = i + 1
else:
    print(X, 'not found')

# б
for i in range(len(L)):
    if 2 ** X == L[i]:
        print('at index', i)
        break
else:
    print(X, 'not found')

# в
if 2 ** X in L:
    print('at index', L.index(2 ** X))
else:
    print(X, 'not found')

# г
import math

list_of_power = []
for num in L:
    list_of_power.append(int(math.log(num, 2)))

print(list_of_power)

# Мой вариант
for i in range(len(L)):
    if 2 ** X == L[i]:
        print('at index', i)
        break
else:
    print(X, 'not found')
