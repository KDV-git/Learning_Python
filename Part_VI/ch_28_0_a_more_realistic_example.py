class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return f'[Person: {self.name}, {self.pay}]'


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def give_raise(self, percent, bonus=.10):
        # self.pay = int(self.pay * (1 + percent + bonus)) - Не надо
        Person.give_raise(self, percent + bonus)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)

    print(bob.name, bob.pay)
    print(sue.name, sue.pay, end='\n\n')

    # print(bob.name.split()[-1])
    # sue.pay *= 1.10
    # print('{:.2f}'.format(sue.pay))

    print(bob.last_name(), sue.last_name())
    sue.give_raise(.10)
    print(sue.pay, end='\n\n')

    print(bob)
    print(sue, end='\n\n')

    tom = Manager('Tom Jones', 50000)
    tom.give_raise(.10)
    print(tom.last_name())
    print(tom)

    print('\n\n')


# Построение составных объектов (стиль программирования: Делегирование)
# Делегирование — структура на основе составного объекта, управляет внедренным объектом и передает ему вызовы методов.
class NewManager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def give_raise(self, percent, bonus=.10):
        self.person.give_raise(percent + bonus)

    def __getattr__(self, attr):
        return getattr(self.person, attr)

    def __repr__(self):
        return str(self.person)


# Ещё один пример
class Department:
    def __init__(self, *args):
        self.members = list(args)

    def add_member(self, person):
        self.members.append(person)

    def give_raise(self, percent):
        for person in self.members:
            person.give_raise(percent)

    def show_all(self):
        for person in self.members:
            print(person)


if __name__ == '__main__':
    new_tom = NewManager('Tom Jones', 50000)
    new_tom.give_raise(.10)
    print(new_tom.last_name())
    print(new_tom, end='\n\n')

    development = Department(bob, sue)
    development.add_member(tom)
    development.give_raise(.10)
    development.show_all()

    print('\n')

    # Специальные атрибуты класса
    print(bob)
    print(bob.__class__)
    print(bob.__class__.__name__)
    print(list(bob.__dict__.keys()))

    print()

    for key in bob.__dict__.keys():
        print(key, '=>', bob.__dict__[key])

    for key in bob.__dict__.keys():
        print(key, '=>', getattr(bob, key))

    print('\n\n')


# Обобщенный инструмент отображения
class AttrDisplay:
    """
    Предоставляет наследуемый метод перегрузки отображения, который показывает
    экземпляры с их именами классов и пары имя=значение для каждого атрибута,
    сохраненного в самом экземпляре (но не атрибутов, унаследованных от его классов).
    Может соединяться с любым классом и будет работать на любом экземпляре.
    """

    def gather_attrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append(f'{key} = {getattr(self, key)}')
        return '; '.join(attrs)

    def __repr__(self):
        return '[{}: {}]'.format(self.__class__.__name__, self.gather_attrs())


if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0

        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2


    class SubTest(TopTest):
        pass


    X, Y = TopTest(), SubTest()

    print(X)
    print(Y)

    print('\n')

    print(bob.__dict__.keys())  # Атрибуты экземпляра
    print(dir(bob))  # Атрибуты всего что можно
    print(list(attr for attr in dir(bob) if not attr.startswith("__")))  # Атрибуты экземпляра + класса (без перегрузок)

    print('\n')


def class_tree(instance):
    attrs = {}
    attrs[instance.name] = list(key for key in instance.__dict__.keys() if not key.startswith("__"))
    attrs[instance.__class__.__name__] = list(
        key for key in instance.__class__.__dict__.keys() if not key.startswith("__"))

    for supclass in instance.__class__.__bases__:
        if supclass.__name__ == 'object':
            continue
        attrs[supclass.__name__] = list(key for key in supclass.__dict__.keys() if not key.startswith("__"))

    return attrs


if __name__ == '__main__':
    print(class_tree(bob))
    print(class_tree(tom))

    print('\n')
