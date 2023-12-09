# bfs
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
N, K = map(int,input().split())
A=[[*map(int ,input().split())] for _ in range(N)]
G = [[] for _ in range(N)]
ziko = [0]*N
for i in range(N):
    for j in range(N):
        if i == j and A[i][j] == 1:
            ziko[i] = 1
        elif A[i][j] == 1:
            G[i].append(j)
q = int(input())
ans = []
for _ in range(q):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    a, b = a%N, b%N
    visited = bfs(G, a)
    if a == b:
        if ziko[a] == 1:
            ans.append(1)
        else:
            mn = 10 **9
            for j in G[a]:
                visited = bfs(G,j)
                mn = min(mn, visited[b] + 1)
            ans.append(mn)
    else:
        
        ans.append(visited[b])
for i in ans:
    print(i)