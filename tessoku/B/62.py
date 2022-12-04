import sys
sys.setrecursionlimit(10**7)
def dfs(v, pre):
    visited[v] = visited[pre] + 1
    ans.append(v+1)
    if v == N-1:
        print(*ans)
        exit()
    for nv in G[v]:
        if visited[nv] == -1:
            dfs(nv, v)
    ans.pop()
    return
N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    G[x].append(y)
    G[y].append(x)

visited = [-1 for i in range(N)]
prev = [-1] * N
ans = []
dfs(0,0)

# start = N-1

# while(start != 0):
#     ans.append(start+1)
#     start = prev[start]
# ans.append(1)
# ans.sort()
# print(*ans)
