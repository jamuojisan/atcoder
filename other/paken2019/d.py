from collections import defaultdict
N = int(input())

field = [input() for _ in range(5)]

dp = [[10**9]*3 for _ in range(N+1)]
ind2c = {0:'R', 1:'B', 2:'W'}
for i in range(3):
    dp[0][i] = 0
for i in range(1,N+1):
    count = defaultdict(int)
    for j in range(5):
        count[field[j][i-1]] += 1
    for j in range(3):
        c = ind2c[j]
        num = count[c]
        for k in range(3):
            if j == k:
                continue
            dp[i][j] = min(dp[i-1][k] + 5-num, dp[i][j])

ans = 10 ** 10
for i in range(3):
    ans = min(ans, dp[N][i])
print(ans)
