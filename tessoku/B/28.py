
N = int(input())
dp = [0 for _ in range(10**7+1)]
dp[1] = 1
dp[2] = 1
mod = 10**9+7
for i in range(3,N+1):
    dp[i] += dp[i-1] % mod
    dp[i] += dp[i-2] % mod
    dp[i] %= mod

print(dp[N])