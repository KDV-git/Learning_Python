# Формы оператора присваивания
# 1. Базовая форма
spam = 'Spam'
print(spam)

print('\n')

# 2. Присваивание кортежа
spam, ham = 'yum', 'YUM'
print(spam)
print(ham)

print('\n')

# 3. Присваивание списка
[spam, ham] = ['yum', 'YUM']
print(spam)
print(ham)

print('\n')

# 4. Присваивание последовательности
a, b, c, d = 'spam'
print(a)
print(b)
print(c)
print(d)

# a, b = 'spam' - ValueError: too many values to unpack (expected 2)

((a, b), c) = ('SP', 'AM')
print(a)
print(b)
print(c)

print('\n')

# 5. Расширенная распаковка последовательности
a, *b = 'spam'
print(a)
print(b)

*a, b = 'spam'
print(a)
print(b)

a, *b, c = 'spam'
print(a)
print(b)
print(c)

print('\n')

# Граничные случаи
a, b, c, *d = 'spam'
print(a)
print(b)
print(c)
print(d)

a, b, c, *d = 'spa'
print(a)
print(b)
print(c)
print(d)

# a, *b, c, *d = 'spam' - SyntaxError: multiple starred expressions in assignment

# *a = 'spam' - SyntaxError: starred assignment target must be in a list or tuple

*a, = 'spam'
print(a)

print('\n')

# Употребление в циклах for
for a, *b, c in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)

for a, *b, c in [(1, 2, 3), (4, 5, 6)]:
    print(a, b, c)

print('\n')

# 6. Групповое присваивание
spam = ham = 'lunch'
print(spam)
print(ham)

a = b = 0
b += 1
print(a, b)

a = b = []
b.append(42)
print(a, b)

print('\n')

# 7. Дополненное присваивание
spams = 0
spams += 42
print(spams)

X = 2
Y = 4

X += Y
X *= Y
X %= Y
X &= Y
X ^= Y
X <<= Y
X -= Y
X **= Y
X |= Y
X >>= Y
X /= Y
X //= Y

print(X)
print(Y)

L = [1, 2]
M = L
print(L)
print(M)

L = L + [3, 4]
print(L)
print(M)

L = [1, 2]
M = L
L += [3, 4]  # эквивалентно L.extend([3, 4])
print(L)
print(M)
