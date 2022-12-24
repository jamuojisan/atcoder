def get_otherpas(val):
    if val == 0:
        return 1, 2
    elif val == 1:
        return 0, 2
    else:
        return 0, 1
N, K = map(int, input().split())
day2p = {}
for i in range(K):
    a,b = map(int, input().aplit())
    day2p[a] = b

dp = [[0]*3 for _ in range(N+1)]

if 1 in day2p:
    p = day2p[1]
    dp[1][p] = 1
else:
    dp[1][0] = 1
    dp[1][1] = 1
    dp[1][2] = 1

for i in range(2,N+1):
    if i in day2p:
        p = day2p
        a, b = get_otherpas(p)
        dp[i][p] = (dp[i-1][a] + dp[i-1][b])%10000
    else:
        for j in range(3):
            a, b = get_otherpas(j)
            dp[i][j] = (dp[i-1][a] + dp[i-1][b])%10000

ans = 0
for i in range(3):
    ans += dp[N][i]
    ans %= 10000
print(ans)