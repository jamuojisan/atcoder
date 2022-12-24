import numpy as np
n , m = map(int, input().split())

a = list(map(int, input().split()))

dp = [[-10**18]*(m+1) for _ in range(n+1)] # dp[i][m] = 数列のi番目までの数の中でm個の数字を選んでいたときの和の最大値
dp[0][0] = 0
for i in range(n):
    for j in range(m):
        if j > i:
            continue
        if j == 0:
            dp[i+1][j] = 0
        dp[i+1][j+1] = max(dp[i][j+1], dp[i][j] + (j+1)*a[i])
print(np.max(np.array(dp)[:,m]))