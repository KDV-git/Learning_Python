import decimal
from decimal import Decimal

x = Decimal(1) / Decimal(7)
print(x)
print('\n')

decimal.getcontext().prec = 5

y = Decimal(1) / Decimal(7)
print(x)
print(y)
print('\n')

with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(Decimal('1.00') / Decimal('3.00'))

print(x)
print(y)
