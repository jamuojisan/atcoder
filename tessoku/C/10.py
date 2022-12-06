def POW(x, n):
    ans = 1
    while n:
        if n % 2:
            ans *= x
            ans %= mod
        x *= x
        x%= mod
        n >>= 1
    return ans%mod
W = int(input())
mod = 10**9 + 7
ans = 12
beki = POW(7, W-1)
ans = (ans*beki) %mod
print(ans)