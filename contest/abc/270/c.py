n, x, y = map(int, input().split())

G = {}
for _ in range(n-1):
    u,v = map(int,input().split())
    if u in G:
        G[u].append(v)
    else:
        G[u] = [v]
    
    if v in G:
        G[v].append(u)
    else:
        G[v] = [u]


from collections import deque 
import sys
sys.setrecursionlimit(10**9)
ans = []

def dfs(v,p):
    if v == y:
        return True
    for k in G[v]:
        if k == p:
            continue
        if dfs(k,v):
            ans.append(k)
            return True

dfs(x,-1)
ans.append(x)
print(*reversed(ans))

