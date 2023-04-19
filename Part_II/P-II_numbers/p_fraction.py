from fractions import Fraction

x = Fraction(1, 3)
y = Fraction(4, 6)

print(x)
print(y)

print('\n')

print(x + y)
print(x - y)
print(x * y)

print('\n')

a = Fraction('.25')
b = Fraction('1.25')

print(a)
print(b)
print(a + b)

print('\n')

print((2.5).as_integer_ratio())

f = 2.5
z = Fraction(*f.as_integer_ratio())
print(z)
print(float(z))

print('\n')

print(x + 2)
print(x + 2.0)
print(x + (1. / 3))
print(x + (4. / 3))
print(x + Fraction(4, 3))
