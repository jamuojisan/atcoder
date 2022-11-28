N = int(input())
DT = []
for _ in range(N):
    t, d = map(int, input().split())
    DT.append([d, t])

DT.sort()

dp = [[0]*(1441) for _ in range(N+1)] # dp[i][j] = i番目の問題までを解くかどうか決めたときの、時間jまでの解けた最大数

for n in range(1, N+1):
    for t in range(1441):
        dp[n][t] = dp[n-1][t] # n-1番目の問題を解かないとき
        if  DT[n-1][1]<= t <= DT[n-1][0]: # n-1番目の問題を解くとき
            dp[n][t] = max(dp[n][t], dp[n-1][t-DT[n-1][1]] + 1)

ans = 0
for i in range(1441):
    ans = max(ans, dp[N][i])
print(ans)