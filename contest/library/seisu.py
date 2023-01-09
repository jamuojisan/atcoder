# 約数列挙　 O(√n)
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

# n以下の素数かどかのフラグリストを列挙 O(nloglogn)
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

    return prime

# 素因数分解
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

import sys
sys.setrecursionlimit(10**7)

# ! 逆元
def modinv(a, m):
    b = m
    u = 1
    v = 0
    while(b):
        t = a//b
        a -=t*b
        a,b = b,a
        u -= t*v
        u ,v = v,u
    u %= m
    if(u < 0):
        u +=m
    return u


# from functools import lru_cache # 時々メモリエラーになる
# @lru_cache(maxsize=None)
# ! 階乗
def factorial(k,m):
    x = 1
    for i in range(k):
        x = x*(k-i)%m
    return x
# ! mod 組み合わせ
def ncr(n,r, m):
    bunsi = factorial(n,m)
    bunbo1 = factorial(n-r,m)
    bunbo2 = factorial(r, m)
    
    bunbo = bunbo1*bunbo2 % m
    inv = modinv(bunbo,m)
    return bunsi * inv % m