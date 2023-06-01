class C2:
    def __init__(self):
        self.name = 'C2'

    def x(self):
        print(f'Hello, i am X in C2')

    def z(self):
        print(f'Hello, i am Z in C2')


class C3:
    def __init__(self):
        self.name = 'C3'

    def w(self):
        print(f'Hello, i am W in C3')

    def z(self):
        print(f'Hello, i am Z in C3')


class C1(C2, C3):
    def __init__(self):
        self.name = 'C1'

    def x(self):
        print(f'Hello, i am X in C1')

    def y(self):
        print(f'Hello, i am Y in C1')


I1 = C1()
I2 = C1()

I1.w()
I1.x()
I1.y()
I1.z()
