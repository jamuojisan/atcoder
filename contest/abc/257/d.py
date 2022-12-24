from collections import deque
import math

def scc(N, G, RG):
    order = []
    used = [0]*N
    group = [None]*N
    def dfs(s):
        used[s] = 1
        for t in G[s]:
            if not used[t]:
                dfs(t)
        order.append(s)
    def rdfs(s, col):
        group[s] = col
        used[s] = 1
        for t in RG[s]:
            if not used[t]:
                rdfs(t, col)
    for i in range(N):
        if not used[i]:
            dfs(i)
    used = [0]*N
    label = 0
    for s in reversed(order):
        if not used[s]:
            rdfs(s, label)
            label += 1
    return label, group

# 縮約後のグラフを構築
def construct(N, G, label, group):
    G0 = [set() for i in range(label)]
    GP = [[] for i in range(label)]
    for v in range(N):
        lbs = group[v]
        for w in G[v]:
            lbt = group[w]
            if lbs == lbt:
                continue
            G0[lbs].add(lbt)
        GP[lbs].append(v)
    return G0, GP

def check(s):
    G = {}
    RG = {}
    for i in range(n):
        for j in range(n):
            # if i == j :
            #     continue
            if(s >= kyori_map[i][j]):
                if(i not in G):
                    G[i] = {j}
                else:
                    G[i].add(j)
                if(j not in RG):
                    RG[j] = {i}
                else:
                    RG[j].add(i)
    
    label, group = scc(n, G, RG)
    G0, GP = construct(n, G, label, group)
    print(G, RG)
    print(label,group,G0,GP)
    exit()
    return False

    






n = int(input())
xyp = []

for _ in range(n):
    x, y, p = map(int, input().split())
    xyp.append((x,y,p))
kyori_map = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(i+1,n):
        x_i, y_i, p_i = xyp[i]
        x_j, y_j, p_j = xyp[j]
        kyori_map[i][j] = math.ceil((abs(x_i -x_j) + abs(y_i - y_j))/p_i)
        kyori_map[j][i] = math.ceil((abs(x_i -x_j) + abs(y_i - y_j))/p_j)

ok = 4*10**9
ng = 0
while(ok - ng > 1):
    mid = (ok + ng) // 2
    for i in range(n):
        f = check(mid)
        if f:
            ok = mid
        else:
            ng = mid
print(ok)

