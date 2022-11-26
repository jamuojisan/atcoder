import sys
sys.setrecursionlimit(10**6)
def dfs(v, G, visited):
    visited[v] = True
    for nv in G[v]:
        if visited[nv] is False:
            dfs(nv, G, visited)

N, M  = map(int, input().split())
G = [list() for _ in range(N)]
edges = [ list(map(int, input().split())) for i in range(M) ]
for a,b in edges:
    G[a-1].append(b-1)
    G[b-1].append(a-1)

visited = [False]*(N)
dfs(0, G, visited)


if False in set(visited):
    print('The graph is not connected.')
else:
    print('The graph is connected.')
    

