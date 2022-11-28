# ダイクストラ法
import heapq
def diekstra(G,a):
    q = []
    heapq.heappush(q, (0,a))
    visited = [-1 for _ in range(N)]
    done = [False for _ in range(N)]
    visited[a] = 0
    while(len(q) > 0):
        d, v= heapq.heappop(q)
        
        if done[v] :
            continue
        done[v] = True
        for (c, nv) in G[v]:
            if visited[nv] == -1 or visited[nv] > visited[v] + c:
                visited[nv] = visited[v] + c
                heapq.heappush(q, (visited[nv],nv))
    return visited

N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    a, b, c, d = map(int, input().split())
    a,b = a-1, b-1
    if d == 1:
        G[a].append([c*10000 -1, b])
        G[b].append([c*10000 -1, a])
    else:
        G[a].append([c*10000, b])
        G[b].append([c*10000, a])

dist = diekstra(G,0)
tree = 10000 - dist[N-1] % 10000
ans =  (dist[N-1] + tree ) // 10000
print(ans, tree) 