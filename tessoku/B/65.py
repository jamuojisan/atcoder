N ,T = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(N-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    G[a].append(b)
    G[b].append(a)

dp = [0]*(N+1)
q = [T - 1]
visited = [False] * N
val = 0
while(len(q)):
    v = q.pop()
    visited[v] = True
    for nv in G[v]:
        if visited[nv] is False:
            dp[nv + 1] = dp[v] + 1
            q.append(nv)

depth = max(dp)

for i in range(1,N+1):
    print(depth + 1 -dp[i], end = ' ')
