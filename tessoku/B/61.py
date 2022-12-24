N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    G[x].append(y)
    G[y].append(x)

ans = -1
val = 0
for i in range(N):
    if val < len(G[i]):
        val = len(G[i])
        ans = i+1
    
print(ans)