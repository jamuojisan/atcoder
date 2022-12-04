N , W = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(N)]

inf = 10** 9 + 100
dp = [[inf]*100001 for _ in range(N+1)]
dp[0][0] = 0
for i in range(1, N+1):
    for j in range(100001):
        dp[i][j] = min(dp[i-1][j], dp[i][j])
        w, v = WV[i-1]
        if j - v>= 0:
            dp[i][j] = min(dp[i][j], dp[i-1][j-v] + w)

ans = 0
for i in range(100001):
    if 0 < dp[N][i] <= W:
        ans = i
print(ans)
