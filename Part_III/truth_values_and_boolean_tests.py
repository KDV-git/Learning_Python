# Сравнения относительных величин возвращают значения True или False в качестве своих результатов истинности
print(2 < 3)
print(3 < 2)

print()

# Операции and и or всегда возвращают объект — либо объект в левой части операции, либо объект в правой ее части.
# Движется слева направо, возвращает первый истинный объект и прерывается
print(2 or 3)
print(3 or 2)  # Возвращает левый операнд, если он истинный
print([] or 3)  # В противном случае возвращает правый операнд (истинный или ложный)
print([] or {})

print()

# Движется слева направо, возвращает первый ложный объект и прерывается
print(2 and 3)
print(3 and 2)  # Возвращает левый операнд, если он ложный
print([] and {})  # В противном случае возвращает правый операнд (истинный или ложный)
print(3 and [])

print()

# Один из распространенных способов применения or - выбор из набора объектов
A = 0
B = 0
C = 42

X = A or B or C or None
print(X)

# Установка стандартного значения
default = 'def'
X = A or default
print(X)
