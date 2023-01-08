N ,M , K ,S, T, X = map(int, input().split())
G = [[] for i in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    G[u].append(v)
    G[v].append(u)

dp = [[0]*N for _ in range(K+1)] # dp[k][j]　kstep目にｊにいる場合の数
dp[0][S-1] = 1

for i in range(1,K+1):
    for j in range(N):
        