import math
N , M = map(int, input().split())
X = [0]*(N+M+1)
Y = [0]*(N+M+1)
for i in range(1, N+M+1):
    X[i], Y[i] = map(int, input().split())
dis = [[0]*(N+M+1) for _ in range(N+M+1)]
for i in range(N+M+1):
    for j in range(i+1,N+M+1):
        dist = math.sqrt((X[i]-X[j])**2 + (Y[i]-Y[j])**2)
        dis[i][j] = dist
        dis[j][i] = dist


inf = 10 ** 20
dp = [[inf]*(N+M+1) for _ in range(2**(N+M+1))] # dp[n][i] すでに訪れた都市の集合nがあって、最後にいる都市がiのときの合計コストの最小値
dp[0][0] = 0 # 最初の出発地は都市0

for n in range(1<<(N+M+1)):
    velocity = 1
    for k in range(N+1,N+M+1):
        if (n>>k) & 1:
            velocity *= 2
    # iからjへの遷移をしらべる
    for i in range(N+M+1):
        for j in range(N+M+1):
            # iが未訪問なら調べない
            if n != 0 and not n &(1<<i):
                continue
            # すでに訪問済みなら調べない
            if  n & (1 << j) or i == j:
                continue
            dp[n|(1<<j)][j] = min(dp[n|(1<<j)][j], dp[n][i] + (dis[i][j]/velocity))

ans = inf

for n in range(2**(N+M+1)):
    if n&((1 << (N+1))-1) == (1<<(N+1)) -1:
        ans = min(ans, dp[n][0])
print(ans)
