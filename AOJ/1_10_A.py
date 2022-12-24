n = int(input())

dp = [0 for i in range(n+1)]

dp[0] = 1
dp[1] = 1

for i in range(n-1):
    dp[i+2] = dp[i+1] + dp[i]

print(dp[n])
