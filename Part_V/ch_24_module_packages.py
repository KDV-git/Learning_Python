# Основы импортирования пакетов

# import ch_17_1_global_scopes_test - ModuleNotFoundError: No module named 'ch_17_1_global_scopes_test'

# import part_iv.ch_17_1_global_scopes_test - ModuleNotFoundError: No module named 'part_iv'

import Part_IV.ch_17_1_global_scopes_test

print(Part_IV.ch_17_1_global_scopes_test.var)

# Пути к каталогам в сценарии после импорта становятся реальными цепочками вложенных объектов
print(Part_IV)
print(dir(Part_IV))

# print(Part_I) - NameError: name 'Part_I' is not defined. Did you mean: 'Part_IV'?

print('\n')

# Пример импортирования пакетов
