N = int(input())
A = list(map(int, input().split()))

dp = [[0]*(N) for i in range(N)]

for i in range(N):
    dp[N-1][i] = A[i]

for i in reversed(range(N-1)):
    for j in range(i+1):
        if i % 2 == 0:
            dp[i][j] = max(dp[i+1][j+1], dp[i+1][j])
        else:
            dp[i][j] = min(dp[i+1][j+1], dp[i+1][j])

print(dp[0][0])

