# Базовые словарные операции
D = {'spam': 2, 'ham': 1, 'eggs': 3}
print(D)
print(D['spam'])
print(len(D))
print('ham' in D)
print(D.keys())
print(list(D.keys()))

print('\n')

# Изменения словарей на месте
D['ham'] = ['grill', 'bake', 'fry']
print(D)
del D['eggs']
print(D)
D['brunch'] = 'Bacon'
print(D)

print('\n')

# Дополнительные словарные методы
print(D.keys())
print(D.values())
print(D.items())

print('\n')

print(D.get('spam'))
print(D.get('poop'))
print(D.get('poop', 666))

print('\n')

# Метод .update()
D1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: "poop"}
D2 = {1: 1, 2: 4, 3: 9, 4: 16}
print(D1)
print(D2)
print(D1 == D2)
print(D1 is D2)

D1.update(D2)
print(D1)
print(D2)
print(D1 == D2)
print(D1 is D2)

print('\n')

D = {'spam': 2, 'ham': 1, 'eggs': 3, 'muffin': 5, 'toast': 4}
print(D)
print(D.pop('muffin'))
print(D)

print('\n')

# Разные способы создания словарей
first_d = {'name': 'Bob', 'age': 40}
print(first_d)

second_d = {}
second_d['name'] = 'Bob'
second_d['age'] = 40
print(second_d)

third_d = dict(name="Bob", age=40)
print(third_d)

fourth_d = dict([('name', 'Bob'), ('age', 40)])
print(fourth_d)

keyslist = ['one', 'two', 'three']
valueslist = [1, 2, 3, 4, 5]

fifth_d = dict(zip(keyslist, valueslist))
print(fifth_d)

sixth_d = dict.fromkeys(['one', 'two', 'three'], [1, 2, 3])
print(sixth_d)

seventh_d = {x: x ** 2 for x in range(10)}
print(seventh_d)
