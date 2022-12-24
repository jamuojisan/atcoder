N ,M = map(int, input().split())
D = [int(input()) for _ in range(N)]
C = [int(input()) for _ in range(M)]
dp = [[10**10]*(M+1) for _ in range(N+1)]
for i in range(M+1):
    dp[0][i] = 0
for n in range(1, N+1):
    dis = D[n-1]
    for m in range(1, M+1):
        h = C[m-1]
        dp[n][m] = min(dp[n][m], dp[n-1][m-1] + h*dis, dp[n][m-1])
ans = 10**10
for i in range(1,M+1):
    ans = min(dp[N][i], ans)
print(ans)

