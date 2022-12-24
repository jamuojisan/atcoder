S = input()
T = input()
N = len(S)
M = len(T)

dp = [[0]*(M+1) for _ in range(N+1)]
for i in range(N+1):
    dp[i][0] = i
for i in range(M+1):
    dp[0][i] = i

for i in range(1, N+1):
    for j in range(1, M+1):
        if S[i-1] == T[j-1]:
            c = 0
        else:
            c = 1
        dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + c)

print(dp[N][M])