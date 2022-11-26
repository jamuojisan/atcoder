N, Q = map(int, input().split())
A = list(map(int, input().split()))
XY = [map(int, input().split()) for _ in range(Q)]

dp = [[None]*(N) for _ in range(30)] # DP[n][i]＝ i番目の場所にいたときのｎ+1日後にいる場所

for i in range(N):
    dp[0][i] = A[i]-1

for i in range(1,30):
  for j in range(N):
    dp[i][j] = dp[i-1][dp[i-1][j]]

for q in range(Q):
    x, y = XY[q]
    x =  x-1
    for d in reversed(range(30)):
        if y // (1<<d) % 2 != 0:
            x = dp[d][x]
    print(x+1)
