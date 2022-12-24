import math
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

G = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(i+1,N):
        x1, y1 = XY[i]
        x2, y2 = XY[j]
        dis = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        G[i][j] = dis
        G[j][i] = dis
inf = 10**9
dp = [[inf]*(N) for _ in range(2**N)]

dp[0][0] = 0

for S in range(2**N):
    for i in range(N):
        for j in range(N):
            if S & (1<<j) and  i == j:
                continue
            dp[S | (1<<j)][j] =  min(dp[S | (1<<j)][j], dp[S][i] + G[i][j])

print(dp[2**N-1][0])
