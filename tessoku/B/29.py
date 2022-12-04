def POW(x, n):
    ans = 1
    while n:
        if n % 2:
            ans *= x
            ans %= mod
        x *= x
        x %= mod
        n >>= 1
    return ans % mod
a, b = map(int, input().split())
mod = 10**9 + 7
print(POW(a,b))