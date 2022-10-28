n, k = map(int, input().split())
day2p = {}

for _ in range(k):
    day, p = map(int, input().split())
    p = p-1
    day2p[day] = p

mod = 10000

dp = [[[0 for _  in range(3)] for i in range(3)] for _ in range(n+1)]
for i in range(3):
    for j in range(3):
        dp[0][i][j] = 1

for i in range(n):
    if i+i in day2p:
        dp[i+1][day2p[i+1]] = (dp[i][0] + dp[i][1] + dp[2])%mod
    else:
        if i+1 <= 2:
            for j in range(3):
                for k in range(3):
                    dp[i+1][0][0] = dp[i]
        else:
            dp[i+1][0][0]


        dp[i+1][0]