import sys
sys.setrecursionlimit(10**7)
def dfs(v):
    global ans
    if ans == limit:
        return
    visited[v] =True
    path.append(v)
    ans += 1
    for nv in G[v]:
        if visited[nv] is False:
            dfs(nv)
    print(f'now node:{v}, pathlist:{path}, ans:{ans}')
    visited[v] = False
    path.pop()

N ,M = map(int ,input().split())
G =[[] for _ in range(N)]
for _ in range(M):
    u, v = map(int ,input().split())
    u, v = u-1, v-1
    G[u].append(v)
    G[v].append(u)
ans = 0
limit = 10**6
path = []
visited = [False]*N

dfs(0)
print(ans)

