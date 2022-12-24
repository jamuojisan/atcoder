import heapq
def diekstra(G,a):
    q = []
    heapq.heappush(q, (0,a, -1))
    visited = [-1 for _ in range(N)]
    done = [False for _ in range(N)]
    visited[a] = 0
    while(len(q) > 0):
        d,v, fr= heapq.heappop(q)
        
        if done[v] :
            continue
        Fr[v] = fr
        done[v] = True
        for (c, nv) in G[v]:
            if visited[nv] == -1 or visited[nv] > visited[v] + c:
                visited[nv] = visited[v] + c
                heapq.heappush(q, (visited[nv],nv,v))
    return visited
N ,M = map(int,input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    a, b, c = map(int ,input().split())
    a, b = a-1 ,b-1
    G[a].append([c,b])
    G[b].append([c,a])

Fr = [-1] * N
visited = diekstra(G, 0)

ans = []
now = N-1
while now != -1:
    ans.append(now+1)
    now = Fr[now]

ans.reverse()
print(*ans)





