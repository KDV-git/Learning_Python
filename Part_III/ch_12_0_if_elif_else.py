# Аналог конструкции if
# Метод выбора через словарь
choice = 'ham'
if_dict = {'spam': 1.25, 'ham': 1.99, 'eggs': 0.99, 'bacon': 1.10}
print(if_dict[choice])

# Тот же выбор использую конструкцию if
if choice == 'spam':
    print(1.25)
elif choice == 'ham':
    print(1.99)
elif choice == 'eggs':
    print(0.99)
elif choice == 'bacon':
    print(1.10)
else:
    print('Bad choice.')

print()

# Защита от исключений через метод .get
print(if_dict.get(choice, 'Bad choice'))
print(if_dict.get('Bad key', 'Bad choice'))

# Защита от исключений через конструкцию if
choice = 'Bad key'
if choice in if_dict:
    print(if_dict[choice])
else:
    print('Bad choice!')

# Защита от исключений через конструкцию try
try:
    print(if_dict[choice])
except KeyError:
    print('Bad choice!')


# Поддержка более сложных действий
def function(num):
    print('Hello, i\'m a function №{}'.format(num))


def default(num):
    print('Oops, function №{} is not found!'.format(num))


if_dict = {'spam': lambda x: print(x ** 2), 'ham': function, 'eggs': lambda x: print(x ** x)}

if_dict.get('spam', default)(5)
if_dict.get('ham', default)(5)
if_dict.get('eggs', default)(5)

print()

# Тернарное выражение if/else
X = 1
Y = 'Y'
Z = 'Z'

if X:
    A = Y
else:
    A = Z

print(A)

X = 0
A = Y if X else Z

print(A)

# Несколько примеров
A = 'true' if 'spam' else 'false'
print(A)

A = 'true' if '' else 'false'
print(A)

print()

# Тот же эффект через операторы and и or
A = ((X and Y) or Z)
print(A)

print()

# Решение примера через функцию bool
A = [Z, Y][bool(X)]
print(A)

print(['false', 'true'][bool('')])
print(['false', 'true'][bool('spam')])

# Лучший метод решения - if/else !
