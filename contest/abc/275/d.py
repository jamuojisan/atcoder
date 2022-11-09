

from functools import lru_cache

@lru_cache
def f(num):
    if num == 0:
        return 1
    else:
        return f(num//2) + f(num//3)

print(f(int(input())))