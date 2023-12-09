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
import itertools
def mult(l):
    ret = 1
    for _l in l:
        ret *= _l
    return ret
N, M = map(int, input().split())
if N*N < M:
    print(-1)
elif N>= M:
    print(M)
else:
    for m in range(M, M+100000):
        lis = prime_factorize(m)
        if len(lis) <= 1:
            continue
        for i in range(2, len(lis)):
            for v in itertools.combinations(lis, i):
                val1 = mult(v)
                val2 = m //val1
                if val1 <= N and val2 <= N:
                    print(m)
                    exit()
            