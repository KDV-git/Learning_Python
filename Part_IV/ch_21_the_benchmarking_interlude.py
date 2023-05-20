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

