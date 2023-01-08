import sys 
sys.setrecursionlimit(10**7)

def dfs(v, depth):
    if depth > k:
        return 
    visited.add(v)
    for nv in G[v]:
        if nv not in visited:
            dfs(nv, depth+1)
    return 
N , M = map(int, input().split())
G = [[] for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,input().split())
    G[a].append(b)
    G[b].append(a)

Q = int(input())
for _ in range(Q):
    x, k = map(int, input().split())
    visited = set()
    dfs(x, 0)
    print(sum(visited))
