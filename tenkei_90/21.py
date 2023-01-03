import sys
sys.setrecursionlimit(10**7)

def scc(G,RG):
    """強連結成分分解を行う関数

    Args:
        G (_type_): 順方向のGraph
        RG (_type_): 逆方向のGraph
    Returns:
        label:最後のグループID
        groups:グループリスト
    """
    
    order = []
    used = [-1]*N
    groups = [None]*N
    def dfs(v):
        used[v] = 1
        for nv in G[v]:
            if used[nv] != -1:
                continue
            dfs(nv)
        order.append(v)
    
    def rdfs(v, col):
        groups[v] = col
        used[v] = 1
        for nv in RG[v]:
            if used[nv] != -1:
                continue
            rdfs(nv, col)
    for i in range(N):
        if used[i] != -1:
            continue
        dfs(i)
    used = [-1]*N
    label = 0
    for v in reversed(order):
        if used[v] != -1:
            continue
        rdfs(v, label)
        label +=1
    return label, groups

N, M = map(int, input().split())
G = [[] for _ in range(N)]
RG = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    G[a].append(b)
    RG[b].append(a)
groupnum, groups = scc(G, RG)
from collections import defaultdict
count = defaultdict(int)
for i in groups:
    count[i] +=1
ans = 0
for i in count:
    ans += count[i]*(count[i]-1)//2
print(ans)
