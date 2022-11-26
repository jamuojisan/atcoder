N, W = map(int, input().split())
VW = []

for _ in range(N):
    w, v = map(int, input().split())
    VW.append([v,w])

dp = [[0]*(W+1) for _ in range(N+1)]  # dp[i][w] = i komemadeno nimotuwo ziyuunierabi omosanogoukeiga wno saidai kati

for i in range(1, N+1):
    for j in range(W+1):
        # tumekomanaitoki
        dp[i][j] = max(dp[i-1][j], dp[i][j])
        # tumekomutoki
        if j-VW[i-1][1]>=0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-VW[i-1][1]] + VW[i-1][0])

ans = 0
for i in range(W+1):
    ans = max(ans, dp[N][i])

print(ans)