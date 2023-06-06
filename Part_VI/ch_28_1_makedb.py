from ch_28_0_a_more_realistic_example import Person, Manager

bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', pay=50000)

import shelve

db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj

db.close()

# Хранилища shelve (pickle) автоматически повторно связывают экземпляр с классом, из которого он был создан,
# когда экземпляр позже загружается обратно в память.
# Python внутренне заново импортирует класс из его модуля, создает экземпляр с сохраненными атрибутами
# и устанавливает ссылку__ class__ экземпляра, чтобы она указывала на первоначальный класс.
