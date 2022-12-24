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
    a,b = map(int, input().split())
    b = b
    day2p[a] = b

dp = [[[0]*4 for _ in range(4)] for _ in range(N+1)] # dp[i][j][k] = 前日にjを食べて、前々日にjを食べているようなi日目までの場合の数
dp[0][0][0] = 1

for n in range(N):
    for i in range(4): # 前々日
        for j in range(4): # 前日
            for k in range(1, 4): # 当日
                if n + 1 in day2p and day2p[n+1] != k:
                    continue
                if i == j == k:
                    continue
                dp[n + 1][k][j] += dp[n][j][i]
                dp[n+1][k][j] %= 10000 
                    

ans = 0
for i in range(1, 4):
    for j in range(1, 4):
        ans += dp[N][i][j]
        ans %= 10000
print(ans)
