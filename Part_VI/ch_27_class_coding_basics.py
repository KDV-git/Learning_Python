class FirstClass:
    def set_data(self, value):
        self.data = value

    def display(self):
        print(self.data)


x = FirstClass()
y = FirstClass()

x.set_data("King Arthur")
FirstClass.set_data(y, 3.14159)

# FirstClass.set_data() - TypeError: FirstClass.set_data() missing 2 required positional arguments: 'self' and 'value'
# FirstClass.set_data(3.14159) - TypeError: FirstClass.set_data() missing 1 required positional argument: 'value'
# FirstClass.set_data(z, 'z') - NameError: name 'z' is not defined

x.display()
FirstClass.display(y)

x.data = 'New Value'
x.display()

# Мы могли бы генерировать совершенно новый атрибут в пространстве имен экземпляра
x.another_name = 'spam'

print('\n')


class SecondClass(FirstClass):
    def display(self):
        print('Current value = "{}"'.format(self.data))


z = SecondClass()
z.set_data(42)

z.display()
SecondClass.display(z)
FirstClass.display(z)

print('\n')


class ThirdClass(SecondClass):
    # ThirdClass.poop = 'poop' - NameError: name 'ThirdClass' is not defined

    def __init__(self, value):
        self.data = value
        ThirdClass.poop = 'poop'

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return '[ThirdClass: {}]'.format(self.data)

    def mul(self, other):
        self.data *= other


a = ThirdClass('abc')

a.display()
print(a)

b = a + 'xyz'
b.display()
print(b)

a.mul(3)
a.display()
print(a)

print()

print(ThirdClass.poop)
print(a.poop)
print(b.poop, end='\n\n')

a.poop = 'a-poop'

print(ThirdClass.poop)
print(a.poop)
print(b.poop, end='\n\n')

ThirdClass.poop = 'new-poop'

print(ThirdClass.poop)
print(a.poop)
print(b.poop)

print('\n')


# Простейший в мире класс Python (классы - также являются объектами)
class rec:
    pass


rec.name = 'Bob'
rec.age = 40

print(rec.name)
print(rec.age)

x = rec()
y = rec()

print(x.name, y.name)
print(x.age, y.age)

# Эти экземпляры не имеют атрибутов, они извлекают эти атрибуты из объекта класса

x.name = 'Sue'
print(rec.name, x.name, y.name)

print()

# В сухом остатке все атрибуты это словари, а деревья - словари из словарей
print(rec.__dict__)
print(x.__dict__)
print(y.__dict__)

print()

# Атрибут может извлекаться либо:
# 1. Посредством индексирования словаря
print(x.__dict__['name'])
# 2. С помощью записи атрибута
print(x.name)

# Но только извлечение атрибута проверяет классы
print(x.age)
# print(x.__dict__['age']) - KeyError: 'age'

print()

# Для упрощения поиска в иерархии наследования при извлечении атрибутов каждый экземпляр имеет связь со своим классом
print(x.__class__)

# Классы также располагают атрибутом__ bases__ , который является кортежем ссылок на их объекты суперклассов
print(rec.__bases__)

print('\n')


# Методы, которые создаются с помощью операторов def, внутри class, могут быть созданы независимо от объекта класса.
def upper_name(obj):
    return obj.name.upper()


print(upper_name(rec))
print(upper_name(x))
print(upper_name(y))
