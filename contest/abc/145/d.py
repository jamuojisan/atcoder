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

x, y = map(int, input().split())

flg = True
for a in range(x+1):
    b = y - 2*a
    if a + 2*b == x:
        flg = False
        break

if flg:
    print(0)
    exit()
print(ncr(a+b, a, 10**9+7))