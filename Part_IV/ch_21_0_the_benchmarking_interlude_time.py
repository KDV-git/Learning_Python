import time
import sys


# Модуль измерения времени: любительский
def timer(func, *args):
    start = time.time()
    for _ in range(100000):
        func(*args)
    return time.time() - start


print(timer(pow, 2, 1000))
print(timer(str.upper, 'spam'))

print('\n')

# Улучшенные функции
timer = time.time


# Функция измерения суммарного времени
def total(reps, func, *pargs, **kargs):
    reps_list = list(range(reps))
    start = timer()
    for _ in reps_list:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return elapsed, ret


# Функция измерения лучшего времени
def best_of(reps, func, *pargs, **kargs):
    best = 2 ** 32
    for _ in range(reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best:
            best = elapsed
    return best, ret


# Функция измерения лучшего суммарного времени
def best_of_total(reps1, reps2, func, *pargs, **kargs):
    return best_of(reps1, total, reps2, func, *pargs, **kargs)


print('Функция total')
print(total(100000, pow, 2, 1000)[0])
print(total(100000, str.upper, 'spam'))

print('\nФункция best_of')
print(best_of(100000, pow, 2, 1000)[0])
print(best_of(100000, str.upper, 'spam,spam,spam,spam'))
print(best_of(50, total, 2000, pow, 2, 1000))

print('\nФункция best_of_total')
print(best_of_total(50, 2000, pow, 2, 1000))

print('\n')

# Альтернатива через генераторное выражение
print(min(total(1000, pow, 2, 1000) for i in range(500)))

print('\n')

# Сценарий измерения времени ("Проверка относительной скорости итерационных альтернатив")
reps = 10000
reps_list = list(range(reps))


def for_loop():
    res = []
    for x in reps_list:
        res.append(abs(x))
    return res


def list_comp():
    return [abs(x) for x in reps_list]


def map_call():
    return list(map(abs, reps_list))


def gen_exp():
    return list(abs(x) for x in reps_list)


def gen_func():
    def gen():
        for x in reps_list:
            yield abs(x)

    return list(gen())


def gen_from_func():
    def gen():
        yield from (abs(x) for x in reps_list)

    return list(gen())


# Запуск всех функций
for test in (for_loop, list_comp, map_call, gen_exp, gen_func, gen_from_func):
    best_res, (total_res, result) = best_of_total(5, 1000, test)
    print('Результат для функции', test.__name__, best_res, '=>', '[%s...%s]' % (result[0], result[-1]))

print()


# Влияние вызовов функций: map
def for_loop():
    res = []
    for x in reps_list:
        res.append(x + 10)
    return res


def list_comp():
    return [x + 10 for x in reps_list]


def map_call():
    return list(map(lambda x: x + 10, reps_list))


def gen_exp():
    return list(x + 10 for x in reps_list)


def gen_func():
    def gen():
        for x in reps_list:
            yield x + 10

    return list(gen())


def gen_from_func():
    def gen():
        yield from (x + 10 for x in reps_list)

    return list(gen())


# Запуск всех функций
for test in (for_loop, list_comp, map_call, gen_exp, gen_func, gen_from_func):
    best_res, (total_res, result) = best_of_total(5, 1000, test)
    print('Результат для функции', test.__name__, best_res, '=>', '[%s...%s]' % (result[0], result[-1]))

print()


# Оптимальное написание: использование стандартных значений с передачей только по ключу для конфигурационных параметров!
def total(func, *pargs, _reps=1000, **kargs):
    reps_list = list(range(_reps))
    start = timer()
    for _ in reps_list:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return elapsed, ret