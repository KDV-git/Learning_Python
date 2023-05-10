import sys

ending = '\n\n---\n\n'

# Функция dir
print(dir(sys))
print(len(dir(sys)))
print(len([x for x in dir(sys) if not x.endswith('_')]))
print(len([x for x in dir(sys) if not x.startswith('_')]))

print()

# Атрибуты объектов встроенных типов
print(dir(''), [x for x in dir('') if not x.endswith('_')], sep='\n', end='\n\n')
print(dir([]), [x for x in dir([]) if not x.endswith('_')], sep='\n', end='\n\n')


def dir1(x):
    """
    This function returns the named attributes of the current object.
    :param x: object
    :return: list of attributes
    """
    return [_ for _ in dir(x) if not _.endswith('_')]


print(dir1(tuple), end='\n\n')

# Строки документации __doc__
print(dir1.__doc__, end=ending)
print(sys.__doc__, end=ending)
print(sys.settrace.__doc__, end=ending)

# Сведение о встроенной функции
print(int.__doc__, end=ending)
print(map.__doc__, end=ending)

# PyDoc: функция help
help(sys.settrace)
help(list)

print(ending)

# PyDoc: отчеты в формате HTML
# Команда для запуска локального веб сервера из командной строки: python -m pydoc -b

# За рамками строк документации: Sphinx
# Sphinx (http://sphinx-doc.org)
