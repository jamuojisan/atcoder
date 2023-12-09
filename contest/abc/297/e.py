N, K =map(int ,input().split())
A =list(map(int ,input().split()))

dp = [[10**9]*K for _ in range(N)] # dp[i][k] i番目までの商品をいくつかってもよいが、k番目に安い金額

for i in range(K):
    dp[0][i] = A[0]*(i+1)
for i in range(1,N):
    dp[i][0] = min(dp[i-1][0],A[i])


for i in range(1,N):
    for k in range(1,K):
        dp[i][k] = min(dp[i-1][k], dp[i-1][k-1]+A[i], dp[i][k-1]+A[i])
        
print(dp)