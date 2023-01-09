from collections import deque
def bfs(G,a):
    visited = [0 for _ in range(N)]
    visited[a] = 1
    q =deque()
    q.append(a)
    mod = 10**9 + 7
    while(len(q) > 0):
        v = q.popleft()
        for nv in G[v]:
            if visited[nv] != 0:
                continue
            visited[nv] += visited[v]
            visited[nv] %= mod
            q.append(nv)
    
    return visited
N, M = map(int,input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    G[a].append(b)
    G[b].append(a)

visited = bfs(G, 0)
print(visited[N-1])