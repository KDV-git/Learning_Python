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
