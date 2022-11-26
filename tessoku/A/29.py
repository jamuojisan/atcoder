def pow_n(x, n):
    ans = 1
    while n:
        if n & 1:
            ans = ans * x % mod
        x = x ** 2 % mod
        n >>= 1
    return ans
mod=10**9 +7
a, b = map(int, input().split())
print(pow_n(a,b))