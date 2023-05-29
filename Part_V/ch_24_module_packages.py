# Основы импортирования пакетов

# import ch_17_1_global_scopes_test - ModuleNotFoundError: No module named 'ch_17_1_global_scopes_test'

# import part_iv.ch_17_1_global_scopes_test - ModuleNotFoundError: No module named 'part_iv'

import Part_IV.ch_17_1_global_scopes_test

print(Part_IV.ch_17_1_global_scopes_test.var)

# Пути к каталогам в сценарии после импорта становятся реальными цепочками вложенных объектов
print(Part_IV)
print(type(Part_IV))
print(dir(Part_IV))

# print(Part_I) - NameError: name 'Part_I' is not defined. Did you mean: 'Part_IV'?

print('\n')

# Пример импортирования пакетов
import dir1.dir2.mod
from importlib import reload

reload(dir1)
# reload(dir2) - NameError: name 'dir2' is not defined. Did you mean: 'dir1'?
reload(dir1.dir2)
# reload(mod) - NameError: name 'mod' is not defined
reload(dir1.dir2.mod)

print()

print(dir1)
print(dir1.dir2)
print(dir1.dir2.mod)

print()

print(dir1.x)
print(dir1.dir2.y)
print(dir1.dir2.mod.z)

# print(mod.z) - NameError: name 'mod' is not defined

print('\n')

# С пакетами часто удобнее использовать оператор from
from dir1.dir2 import mod

print(mod)
print(mod.z)

# Расширение import as также решает эту проблему
import dir1.dir2.mod as modas

print(modas)
print(modas.z)

from dir1.dir2 import mod as modfromas

print(modfromas)
print(modfromas.z)
