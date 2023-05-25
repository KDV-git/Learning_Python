import test_module

test_module.painter('spam')
test_module.double_painter('spam', 'ham')
test_module.mega_painter('spam', 'ham', 'eggs', 'bacon')

print()

from test_module import painter

painter('Hello, i am new global name func!')
# double_painter('spam', 'ham') - NameError: name 'double_painter' is not defined
# mega_painter('spam', 'ham', 'eggs', 'bacon') - NameError: name 'mega_painter' is not defined

print()

# Получить копии всех имён модуля (по существу сворачивает пространство имен одного модуля внутрь другого)
from test_module import *

painter('Hello, i am new global name func!')
double_painter('I am', 'too')
mega_painter('I', 'am', 'also', 'too')

print('\n')

print(spam)
print(test_module.spam)

spam = 'spam'
test_module.spam = 100
print(spam)
print(test_module.spam)

print()

# Поскольку процесс импортирования (три шага) происходят всего один раз за выполнение,
# переменная spam НЕ будет инициализироваться заново!
import test_module

print(spam)
print(test_module.spam)

print()

# Модификация разделяемого изменяемого объекта через скопированное имя изменяет его в модуле, откуда оно копировалось
print(ham)
print(test_module.ham)

ham[1] = 'ham'

print(ham)
print(test_module.ham)

print('\n')

# Словари пространств имен: __diсt__
print(test_module.__dict__, end='\n\n\n')
print(type(test_module.__dict__))
print(list(test_module.__dict__))

from importlib import reload

reload(test_module)
