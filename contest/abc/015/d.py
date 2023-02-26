W = int(input())
N, K = map(int, input().split())
AB = []
for _ in range(N):
    a, b = map(int, input().split())
    AB.append([a,b])

dp = [[[0]*(W+1) for _ in range(K+1)] for _ in range(N+1)] # dp[n][w] 最初からn枚の中からk枚選んだ画像の組み合わせで幅の合計値がwのときの重要度の最大値

for i in range(N+1):
    dp[i][0][0] = 0

for i in range(1,N+1):
    for k in range(1, min(i+1, K+1)):
        for j in range(W+1):
            # 選ばないとき
            dp[i][k][j] =  dp[i-1][k][j]
            a, b = AB[i-1]
            # 選ぶとき
            if j-a >= 0:
                dp[i][k][j] = max(dp[i-1][k-1][j-a] + b, dp[i][k][j])

ans = 0
for i in range(W+1):
    for j in range(K+1):
        ans = max(ans, dp[N][j][i])
print(ans)
