w, h = map(int, input().split())
import sys
sys.setrecursionlimit(10**7)
mod = 10**9 +7
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
def factorial(k,m):
    k %= m
    if k == 1:
        return k
    else:
        return k*factorial(k-1, m)%m

def ncr(n,r, m):
    bunsi = factorial(n,m)
    bunbo1 = factorial(n-r,m)
    bunbo2 = factorial(r, m)
    
    bunbo = bunbo1*bunbo2 % m
    inv = modinv(bunbo,m)
    return bunsi * inv % mod

ans = ncr(h+w-2, h-1, mod)
print(ans)