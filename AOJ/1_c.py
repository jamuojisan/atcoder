N,W = map(int, input().split())
vw = []
for _ in range(N):
    v,w = map(int, input().split())
    vw.append([v,w])

dp = [[0 for _ in range(W+1)] for _ in range(N+1)] # dp[i][j] i個目までの荷物で重さの合計がj以下の価値を最大化

for i in range(N):
    for _w in range(W+1):
        if _w+vw[i][1] <= W:
            dp[i+1][_w+vw[i][1]] = max(max(dp[i][_w] + vw[i][0], dp[i+1][_w+vw[i][1]]), dp[i+1][_w] + vw[i][0])
        dp[i+1][_w] = max(dp[i][_w], dp[i+1][_w])
print(max(dp[N]))
