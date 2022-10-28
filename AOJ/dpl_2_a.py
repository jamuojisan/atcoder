n,m = map(int, input().split())
INF = 10**9
G =[[INF]*n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    G[a][b]=c

dp =[[INF]*(n) for _ in range(n**2)]  #dp[S][v] = {0,1,2,・・・,n-1}の部分集合Sを巡回する|S|!通りの経路のものの距離。ただし、最後に頂点vに達したときのみを考える

dp[0][0] = 0
for S in range(1,2**n):
    if bin(S).count('1') ==1:
        continue
    for v in range(n-1):
        if not 
        for u in range(n):
            if not(S &(1 << u)):
                continue # uを含まない場合はのぞく
            if ((S & (1 << v)) == 0):
                if v != u:
                    dp[S | (1 << v)][v] = min(dp[S][u]+G[u][v], dp[S | (1 << v)][v])

if dp[(1<<n) -1][0] < INF:
    print(dp[(1<<n) -1][0])
else:
    print(-1)