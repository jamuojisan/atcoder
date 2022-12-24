n = int(input())
a = list(map(int, input().split()))

dp = [[0 for _ in range(21)] for _ in range(n)]
dp[0][a[0]] = 1
for i in range(0,n-1):
    for j in range(21):
        if j - a[i] >= 0:
            dp[i+1][j] += dp[i][j-a[i]]
        if j + a[i] <=20:
            dp[i+1][j] += dp[i][j+a[i]]
print(dp)
print(dp[n-1][a[-1]])

