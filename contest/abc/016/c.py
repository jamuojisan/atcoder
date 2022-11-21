n , m= map(int, input().split())
G = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    G[a].append(b)
    G[b].append(a)
from collections import deque
def bfs(G,a):
    visited = [-1 for _ in range(n)]
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

for i in range(n):
    visited = bfs(G, i)
    cnt = 0
    for j in range(n):
        if visited[j] == 2:
            cnt +=1
    print(cnt)