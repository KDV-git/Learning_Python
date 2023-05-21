import timeit

print(timeit.repeat(stmt='[x ** 2 for x in range(1000)]', number=1000, repeat=5))
print(min(timeit.repeat(stmt='[x ** 2 for x in range(1000)]', number=1000, repeat=5)))

