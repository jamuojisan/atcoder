S = int(input())
K  = (S//3)+1
dp = [[0]*(S+1) for _ in range(K+1)]

dp[0][0] = 1
for i in range(1, K+1):
    for j in range(1, S+1):
        for k in range(3,10):
            if j-k >=0:
                dp[i][j] += dp[i-1][j-k]
                dp[i][j] %= (10**9 + 7)

ans = 0
for i in range(K+1):
     ans += dp[i][S]
     ans %= (10**9 + 7)
print(ans)
print(dp)
