import sys
sys.setrecursionlimit(10**9)
def dfs(node,visit):
    visit.append(node)
    visited[node] = True
    for nv in G[node]:
        if visited[nv] is False:
            visit = dfs(nv, visit)
    return visit

N ,M =map(int, input().split())
G = [[] for _  in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    G[u].append(v)


ans = 0
for i in range(N):
    visited = [False]*N
    unique_visit = dfs(i, [])
    for j in unique_visit:
            if i == j:
                continue
            if j not in G[i]:
                ans += 1
print(ans)