def painter(x):
    print(x)


def double_painter(x, y):
    print(x, y)


def mega_painter(*args):
    print(*args)


if __name__ == '__main__':
    painter('Hello')
    double_painter('Hello', 'World!')
    mega_painter('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!')
