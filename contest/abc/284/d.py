import sys
from collections import defaultdict
from collections import deque
import heapq
sys.setrecursionlimit(10**7)
from collections import defaultdict
import math
def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False
    prime = [i for i, j in enumerate(prime) if j is True]

    return prime
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
T = int(input())
p_list = sieve_of_eratosthenes(3*(10**6) + 1)

for _ in range(T):
    N = int(input())
    ans = []
    for p in p_list:
        if N%p == 0:
            if N%(p**2) == 0:
                _p = p
                _q = N//(p**2)
            else:
                _q = p
                N //= p
                _p = int(math.sqrt(N))
            break
    print(_p, _q)
            


# A = [*map(int, input().split())]
# C = [[*map(int, input().split())] for _ in range(N)]
# P = [[] for _ in range(N)]
