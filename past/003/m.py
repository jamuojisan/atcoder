from collections import deque
def bfs(G,a):
    visited = [-1 for _ in range(N)]
    visited[a] = 0
    q =deque()
    q.append(a)

    while(len(q) > 0):
        v = q.popleft()
        for nv in G[v]:
            if visited[nv] != -1:
                continue
            visited[nv] = visited[v] + 1
            q.append(nv)
    
    return visited

N, M = map(int, input().split())
G =[[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u,v = u-1, v-1
    G[u].append(v)
    G[v].append(u)

s =int(input())
s -= 1
K = int(input())
T = list(map(int, input().split()))
T = [t-1 for t in T]
t2k = {t:k for k, t in enumerate(T)}
if s not in G:
    t2k[s] = len(T)
    G2 = [[] for _ in range(K+1)]
    L =K+1
else:
    G2 = [[] for _ in range(K)]
    L =K

for i in T:
    costs = bfs(G,i)
    i2 = t2k[i]
    for j in range(N):
        if j not in T:
            continue
        if i ==j:
            continue
        j2 = t2k[j]
        G2[i2].append([costs[j], j2])
        G2[j2].append([costs[j], i2])


print(G2)

inf = 10 ** 20
dp = [[inf]*(L) for _ in range(2**L)] # dp[n][i] すでに訪れた都市の集合nがあって、最後にいる都市がiのときの合計コストの最小値
dp[0][s] = 0 # 最初の出発地は都市0

for l in range(2**L):
    # iからjへの遷移をしらべる
    for i in range(L):
        for j in range(L):
            # すでに訪問済みなら調べない
            if  l & (1 << j) or i == j:
                continue
            flg = False
            for c,p in G2[i]:
                if p == j:
                    flg = True
                    break
            if flg:
                dp[l|(1<<j)][j] = min(dp[l|(1<<j)][j], dp[l][i] + c)
ans = inf
for i in range(L):
    ans = min(dp[2**L-1][i],ans)
print(ans)
        


