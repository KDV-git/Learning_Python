import test
from test import minus


def formula(sum_result):
    return sum_result / 2


if __name__ == '__main__':
    print(dir(test))
    print(formula(test.plus(10, 5)))
    print(formula(minus(10, 5)))

    exec(open("test.py").read())
