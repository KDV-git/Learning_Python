class NextClass:
    def printer(self, text):
        self.message = text
        print(self.message)


x = NextClass()
x.printer('poop')
print(x.message)

NextClass.printer(x, 'new_poop')
print(x.message)

print('\n')


class Super:
    def __init__(self, num, text):
        self.num = num
        self.text = text

    def show(self):
        print(f'№{self.num}. {self.text}')


class SubSup(Super):
    def poop(self):
        print('Poop is good!')


# a = Super() - TypeError: Super.__init__() missing 2 required positional arguments: 'num' and 'text'
a = Super(1, 'lul')
a.show()

# b = SubSup() - TypeError: Super.__init__() missing 2 required positional arguments: 'num' and 'text'
b = SubSup(2, 'lel')
b.show()
b.poop()

print()


class Super2:
    def __init__(self, text):
        self.num = 666
        self.text = text

    def show(self):
        print('Secret!')


class SubSup2(Super2, Super):
    def ogo(self):
        print('Ogo!')


# c = SubSup2() -TypeError: Super2.__init__() missing 1 required positional argument: 'text'
# c = SubSup2(3, 'lol') - TypeError: Super2.__init__() takes 2 positional arguments but 3 were given

class SubSup2(Super2, Super):
    def __init__(self, num, text):
        Super.__init__(self, num, text)

    def ogo(self):
        print('Ogo!')


# c = SubSup2() - TypeError: SubSup2.__init__() missing 2 required positional arguments: 'num' and 'text'
c = SubSup2(3, 'lol')
c.show()
c.ogo()
Super.show(c)

print('\n')

# Простые имена: глобальные, если не выполнено их присваивание.
# 1. (X = значение) - По умолчанию делает имя локальным: создает/изменяет имя X в текущей локальной области видимости,
# если только оно не объявлено как global (или nonlocal в Python З.Х).

# 2. Ссылка (X) - Ищет имя X в областях видимости согласно правилу LEGB.

# Имена атрибутов: пространства имен объектов
# 3. Присваивание (object.X = значение) - Создает/модифицирует имя атрибута X в пространстве имен уточняемого объекта
# "object" и больше нигде.
# Подъем по дереву наследования происходит только при ссылке на атрибут, но не в случае присваивания значения атрибуту.

# 4. Ссылка (object.X) - Для объектов, основанных на классах, ищет имя атрибута X в object и затем во всех классах выше.
# Для объектов, не основанных на классах, таких как модули, извлекает X из object напрямую.

# Глобальное имя/атрибут модуля
X = 11


def f():
    print(X)  # Доступ к глобальному имени X


def g():
    X = 22  # Локальная переменная в функции (X, скрывает X в модуле)
    print(X)


class C:
    X = 33  # Атрибут класса (С.Х)

    def m(self):
        X = 44  # Локальная переменная в методе (X)
        self.X = 55  # Атрибут экземпляра (экземпляр.X)


print(X)
f()
g()
print(C.X)
Cl = C()
print(Cl.X)
Cl.m()
print(Cl.X)

print('\n')

# Класс является локальной областью видимости и имеет доступ к объемлющим локальным областям видимости,
# но он не служит объемлющей локальной областью видимости для дальнейшего вложенного кода.

X = 1


def nester():
    print(X)  # Глобальное имя: 1

    class C:
        print(X)  # Глобальное имя: 1

        def method1(self):
            print(X)  # Глобальное имя: 1

        def method2(self):
            X = 3  # Скрывает глобальное имя
            print(X)  # Локальное имя: 3

    I = C()
    I.method1()
    I.method2()


print('-' * 40)
print(X)  # Глобальное имя: 1
nester()  # Остаток: 1, 1, 2, 3
print('-' * 40)

X = 1


def nester():
    X = 2  # Скрывает глобальное имя
    print(X)  # Локальное имя: 2

    class C:
        print(X)  # В объемлющем def (nester) : 2

        def method1(self):
            print(X)  # В объемлющем def (nester) : 2

        def method2(self):
            X = 3  # Скрывает имя из объемлющего def (nester)
            print(X)  # Локальное имя: 3

    I = C()
    I.method1()
    I.method2()


print('-' * 40)
print(X)  # Глобальное имя: 1
nester()  # Остаток: 2, 2, 2, 3
print('-' * 40)

X = 1


def nester():
    X = 2  # Скрывает глобальное имя
    print(X)  # Локальное имя: 2

    class C:
        X = 3  # Локальное имя из класса скрывает имя из nester: C.X или I.X
        print(X)  # Локальное имя: 3

        def method1(self):
            print(X)  # В объемлющем def (не 3 в классе!) : 2
            print(self.X)  # Унаследованное локальное имя класса: 3

        def method2(self):
            X = 4  # Скрывает имя из объемлющей области видимости (nester, не класса)
            print(X)  # Локальное имя: 4
            self.X = 5  # Скрывает имя из класса
            print(self.X)  # Находится в экземпляре: 5

    I = C()
    I.method1()
    I.method2()


print('-' * 40)
print(X)  # Глобальное имя: 1
nester()  # Остаток: 2, 3, 2, 3, 4, 5
print('-' * 40)

# Самое главное: правила поиска для простых имен вроде X никогда не ищут во включающих операторах class
# только в операторах def, модулях и встроенной области видимости (правило называется LEGB, а не CLEGB!).

# Модули:
# • реализуют пакеты данных/логики;
# • создаются с помощью файлов с кодом на Python или расширений на других языках;
# • используются путем импортирования;
# • формируют верхний уровень структуры программы на Python.

# Классы:
# • реализуют новые полнофункциональные объекты;
# • создаются посредством операторов class;
# • используются путем обращения к ним;
# • всегда находятся внутри модуля.
