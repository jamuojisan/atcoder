import sys
sys.setrecursionlimit(10**9)
n, q = map(int, input().split())
G ={}
for _ in range(n-1):
    a,b = map(int, input().split())
    if a not in G:
        G[a] = [b]
    else:
        G[a].append(b)
    if b not in G:
        G[b] = [a]
    else:
        G[b].append(a)
point = [0 for i in range(n)]
visited = [-1 for _ in range(n)]
def dfs(now):
    visited[now-1] = 0
    for next in G[now]:
        if visited[next-1] == -1:
            point[next-1] += point[now-1]
            dfs(next)




for _ in range(q):
    p, x = map(int, input().split())
    point[p-1] +=x

dfs(1)

print(*point)

