S = input()
out = 'chokudai'
N = len(S)
M = len(out)
dp = [[0]*(M+1) for _ in range(N+1)]
for i in range(N+1):
    dp[i][0] = 1
mod = 10**9 + 7
for i in range(1,N+1):
    moji = S[i-1]
    for j in range(1,M+1):
        dp[i][j] = dp[i-1][j]
        if moji == out[j-1]:
            dp[i][j] += dp[i-1][j-1]
            dp[i][j] %= mod 
print(dp[N][M])