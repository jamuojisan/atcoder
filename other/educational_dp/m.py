N, K = map(int, input().split())
A = [*map(int,input().split())]

dp = [[0]*(K+1) for _ in range(N+1)] # i番目の子にj個配る場合の数

dp[0][0] = 1
mod = 10**9 + 7
for i in range(1, N+1):
    for j in range(K+1):
        for k in range(A[i-1]+1):
            if j-k >= 0:
                dp[i][j] += dp[i-1][j-k]
                dp[i][j] %= mod