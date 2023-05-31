# Упражнения для части V
# 1. Основы операций импортирования.
def count_lines(name):
    f = open(name)
    return len(f.readlines())


def count_chars(name):
    f = open(name)
    return len(f.read())


def test(name):
    return count_lines(name), count_chars(name)


# 2. from / from *

# 3. __main__
if __name__ == '__main__':
    file_name = 'test_module2a.py'

    print(count_lines(file_name))
    print(count_chars(file_name))
    print(test(file_name))
    print(test('ch_XX_exercises_part_V.py'))

print('\n')

# 4-7. Да.
