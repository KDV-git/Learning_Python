# Python хранит загруженные модули в таблице по имени sys.modules и просматривает ее в начале операции импортирования
import sys
# import sys - ModuleNotFoundError: No module named 'sysasfafawf'


def modules_check():
    print(sys.modules)
    print(type(sys.modules), end='\n\n')

    count = 0
    for key in sys.modules.keys():
        print(key, end=' | ')
        count += 1
        if count == 15:
            print()
            count = 0

    print()
    print(len(sys.modules))

    print('\n')


modules_check()

import math

x = math.sqrt(16)

modules_check()

# Путь поиска модулей
# sys .path — изменяемый список строк с именами каталогов
print(sys.path)
print(len(sys.path))

for path in sys.path:
    print(path)

print('\n')

# Изменение списка sys.path вручную
sys.path.append('D:\\Python\\After')
sys.path.insert(0, 'D\\Python\\Before')

for path in sys.path:
    print(path)
