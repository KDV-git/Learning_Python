# Упражнения для части IV
# 1. Основы.
def func(x):
    print(x)


func(1)
func([1, 2, 3])
func('spam')
func({'s': 1, 'p': 2, 'a': 3, 'm': 4})
# func() - TypeError: func() missing 1 required positional argument: 'x'
# func(1, 2) - TypeError: func() takes 1 positional argument but 2 were given
func((1, 2))

print('\n')


# 2. Аргументы.
def adder(a, b):
    return a + b


print(adder(5, 10))
print(adder('sp', 'am'))
print(adder([1, 2], [3, 4]))
print(adder(1.2, 3.4))

adder(5, 10)
adder('sp', 'am')
adder([1, 2], [3, 4])
adder(1.2, 3.4)

# 3. Переменное количество аргументов.
# 4. Ключевые аргументы.
# 5. Словарные инструменты.
# 6. Словарные инструменты.
# 7. Дополнительные примеры сопоставления аргументов.
# 8. Снова простые числа.
# 9. Итерации и включения.
# 10. Измерение времени выполнения инструментов.
# 11. Рекурсивные функции.
# 12. Вычисление факториалов.
