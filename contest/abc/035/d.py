import heapq
N, M , T= map(int, input().split())
A  = list(map(int, input().split()))
G1= [[]*N for _ in range(N)]
G2= [[]*N for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    a,b = a-1, b-1
    G1[a].append([b,c])
    G2[b].append([a,c])

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
        for (nv, c) in G[v]:
            if visited[nv] == -1 or visited[nv] > visited[v] + c:
                visited[nv] = visited[v] + c
                heapq.heappush(q, (visited[nv],nv))
    return visited

# def dijkstra_heap(s,edge):
#     #始点sから各頂点への最短距離
#     d = [float("inf")] * N
#     used = [True] * N #True:未確定
#     d[s] = 0
#     used[s] = False
#     edgelist = []
#     for e in edge[s]:
#         heapq.heappush(edgelist,e)
#     while len(edgelist):
#         minedge = heapq.heappop(edgelist)
#         #まだ使われてない頂点の中から最小の距離のものを探す
#         if not used[minedge[1]]:
#             continue
#         v = minedge[1]
#         d[v] = minedge[0]
#         used[v] = False
#         for e in edge[v]:
#             if used[e[1]]:
#                 heapq.heappush(edgelist,[e[0]+d[v],e[1]])
#     return d
visited1 = diekstra(G1)
visited2 = diekstra(G2)
print(visited1)
print(visited2)
ans = 0
for i in range(N):
    ans = max(ans, (T - visited1[i] -visited2[i])*(A[i]))
    

print(ans)


    
    