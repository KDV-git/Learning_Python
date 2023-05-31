# Сокрытие данных в модулях
import os

# Сведение к минимуму вреда от from * : _х и __all__
# Используя имена с _ вначале предотвращает их импортирование через from * (и только через неё)
from test_module2 import *

print(a, c)
# print(_b, _d) - NameError: name '_b' is not defined

from test_module2 import _b

print(_b)

import test_module2

print(test_module2._d)

del a, _b, c, test_module2

# print(a) - NameError: name 'a' is not defined
# print(_b) - NameError: name '_b' is not defined
# print(c) - NameError: name 'c' is not defined
# print(_d) - NameError: name '_d' is not defined. Did you mean: 'id'?

print('\n')

# Другой способ связан с использованием переменной __all__ (список со строками имён переменных)
from test_module2a import *

print(a, _b)
# print(_d) - NameError: name '_d' is not defined

# __all__ имеет приоритет над _x
# print(c) - NameError: name 'c' is not defined

# Список __all__ также работает только через from *
from test_module2a import c

print(c)

import test_module2a

print(test_module2a._d)

# Внутри файлов __init__.ру пакетов, списки __all__ объявляют подмодули,
# которые подлежат автоматической загрузке для оператора from * с их контейнером.

print('\n')

# Названия будущих средств никогда не удалятся, поэтому совершенно безопасно оставлять импортирование __future__
# даже в коде, запускаемом под управлением версии Python, где такие средства присутствуют как нормальные.
import __future__

print(dir(__future__))

print('\n')

print(__name__)
print(__future__.__name__)

print('\n')

# Символы валют: Unicode в действии

# 1. Порядковый номер (целое число) декодированной кодовой точки Unicode в текстовой строке.

# Обозначив ее как шестнадцатеричную
print('\xA3')
# Обозначив ее как Unicode
print('\u00A5')

# 2. Низкоуровневая закодированная форма символа в байтовой строке, которая декодируется перед передачей.

# Обозначив ее как шестнадцатеричную
print(b'\xA3'.decode('latin-1'))

# 3. Фактический символ в тексте программы вместе с объявлением кодировки исходного кода.
print(b'\xA4'.decode('iso-8859-15'))

print('\n')

# Изменение пути поиска модулей
import sys
from importlib import reload

print(sys.path)
sys.path.append('D:\\Python\\After')
sys.path.insert(0, 'D\\Python\\Before')
print(sys.path)

sys.path = [0, 1, 2, 3]
print(sys.path)

reload(sys)
print(sys.path)

print('\n')

# Расширение as для операторов import и from
import test_module2 as tm2

print(dir(tm2))

# Эквивалент расширения as
import test_module2a

tm2a = test_module2a
del test_module2a

print(dir(tm2a))

print('\n')

# Модули являются объектами
import test_module2

print(test_module2.a)
print(test_module2.__dict__['a'])
print(sys.modules['test_module2'].a)
print(getattr(test_module2, 'a'))

print('\n')

# Импортирование модулей по строкам с именами

# import 'os' - SyntaxError: invalid syntax
x = 'os'
# import x - ModuleNotFoundError: No module named 'x'

# Выполнение строк с кодом
exec('import ' + x)

print(os)

# Прямые вызовы: два варианта
modname = 'importlib'

importlib = __import__(modname)
print(importlib)

modname = 'math'
math = importlib.import_module(modname)
print(math)

print('\n')

# Затруднения, связанные с модулями
# 1. Конфликты имен модулей: операции импортирования пакетов и относительно пакетов
# 2. Порядок следования операторов в коде верхнего уровня имеет значение
# 3. Оператор from копирует имена, но не ссылки на них
# 4. Форма оператора from * может сделать неясным смысл переменных
# 5. Функция reload может не оказывать влияния на результаты операторов импортирования from
# 6. reload, from и тестирование в интерактивном сеансе (после reload придётся заново from)
# 7. Рекурсивные операции импортирования from могут не работать
