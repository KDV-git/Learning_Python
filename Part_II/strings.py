path = 'C:\test\new'
print(path)

giga_path = r'C:\test\new'
print(giga_path)

alp_path = 'C:\\test\\new'
print(alp_path)

uni_str = 'sp\xc4m'
print(uni_str)

code_str = 'sp\xc4\u00c4\U000000c4m'
print(code_str)

byte_str = b'a\x01c'
print(type(byte_str))
print(byte_str)

print('\u00A3', '\u00A3'.encode('latin1'), b'\xA3'.decode('latin1'))

print('\n---\n')

x = ord('s')
print(x)
print(chr(x))
print('\n')

s = "3"
for num in range(10):
    s = chr(ord(s) + 1)
    print(s)

print('\n')

# Преобразование двоичных чисел в целое число с помощью ord
B = '1101'
I = 0
while B != '':
    I = I * 2 + (ord(B[0]) - ord('0'))
    B = B[1:]

print(I)
print(int('1101', 2))

print('\n')

# Примеры форматирования через %
print('That is %d %s bird!' % (1, 'dead'))
print('%d %s %g you' % (1, 'spam', 4.0))

x = 1.23456789
print('%e | %f | %g' % (x, x, x))
print('%E' % x)

print('%-6.2f | %05.2f | %+06.1f' % (x, x, x))
print('%s' % x, str(x))

print('%f, %.2f, %.*f' % (1 / 3.0, 1 / 3.0, 4, 1 / 3.0))

print('\n')

# Примеры форматирования через % со словарём
print('%(qty)d more %(food)s' % {'qty': 1, 'food': 'spam'})

reply = """
Greetings...
Hello %(name)s!
Your age is %(age)s
"""
values = {'name': 'Bob', 'age': '40'}
print(reply, values)
print(reply % values)

food = 'spam'
qty = 10
print(vars())
print('%(qty)d more %(food)s' % vars())

print('\n')

# Примеры форматирования через ".format"
template = '{0},{1} and {2}'
print(template.format('spam', 'ham', 'eggs'))

template = '{motto},{pork} and {food}'
print(template.format(motto='spam', pork='ham', food='eggs'))

template = '{motto},{0} and {food}'
print(template.format('ham', motto='spam', food='eggs'))

template = '{},{} and {}'
print(template.format('spam', 'ham', 'eggs'))

print('\n')

# Добавление ключей, атрибутов и смещений
import sys

text = 'My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'})
print(text)

text = 'My {map[kind]} runs {sys.platform}'.format(sys=sys, map={'kind': 'laptop'})
print(text)

somelist = list('SPAM')
print(somelist)

print('first={0[0]}, third={0[2]}'.format(somelist))

print('first={0}, last={1}'.format(somelist[0], somelist[-1]))

parts = somelist[0], somelist[-1], somelist[1:3]
print(parts)

print('first={0}, last={1}, middle={2}'.format(*parts))
print('first={}, last={}, middle={}'.format(*parts))

print('\n')

# Расширенный синтаксис методов форматирования
print('{0:10} = {1:10}'.format('spam', 123.4567))
print('{:>10} = {:<10}'.format('spam', 123.4567))
print('{0.platform:>10} = {1[kind]:<10}'.format(sys, dict(kind='laptop')))

print('{0:e}, {1:.3e}, {2:g}'.format(3.14159, 3.14159, 3.14159))
print('{0:f}, {1:.2f}, {2:06.2f}'.format(3.14159, 3.14159, 3.14159))

print('\n')

# Форматирования между системами счисления
print('{0:x}, {1:o}, {2:b}'.format(255, 255, 255))
print(bin(255), int('11111111', 2), 0b11111111)
print(hex(255), int('FF', 16), 0xFF)
print(oct(255), int('377', 8), 0o377)

print('\n')

# Строгое кодирование и сравнение с %
print("{0:.2f}".format(1 / 3.0))
print("%.2f" % (1 / 3.0))

print('{0:.{1}f}'.format(1 / 3.0, 4))
print('%.*f' % (4, 1 / 3.0))

print('{0:.2f}'.format(1.2345))  # Строковый метод
print(format(1.2345, '.2f'))  # Встроенная функция
print('%.2f' % 1.2345)  # Выражение
