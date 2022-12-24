from collections import deque

def bfs(a):
    visited = [-1]*(N)
    q = deque()
    q.append(a)
    visited[a] = 0
    while(len(q)):
        v = q.popleft()
        for nv in G[v]:
            if visited[nv] == -1:
                visited[nv]= visited[v] +1
                q.append(nv)
    return visited

N, M  = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a,b =a -1, b-1
    G[a].append(b)
    G[b].append(a)


visited = bfs(0)

for i in range(N):
    print(visited[i])