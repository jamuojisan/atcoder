N = int(input())
P = [*map(float,input().split())]

# dp[i][j] = i枚目のコインまで投げた時、表がj枚出る確率 
# dp[i][j] = (i-1枚までで表がj枚出る確率) * (i枚目で裏が出る確率) + (i-1枚目までで表がj-1枚出る確率)*(i枚目で表が出る確率)
dp = [[0]*(N+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    p = P[i-1]
    for j in range(N+1):
        if j == 0:
            dp[i][j] = dp[i-1][0]*(1-p)
        dp[i][j] =dp[i-1][j] * (1-p) + dp[i-1][j-1]*p

ans = 0
for i in range(N//2+1,N+1):
    ans += dp[N][i]
print(ans)