from collections import deque
def bfs(s):
    q = deque()
    q.append(s)
    dis = [-1] *(2 **N)
    dis[s] = 0    
    while(len(q)):
        v = q.popleft()
        for nv in G[v]:
            if dis[nv] == -1:
                dis[nv] = dis[v] +1
                q.append(nv)
    return dis
        

N, M = map(int, input().split())


A = list(map(int, input().split()))
G = [[] for _ in range(2**N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    a, b, c = (1 << a-1), (1 << b-1), (1 << c-1)
    for i in range(2**N):
        to = ((i^a)^b)^c
        G[i].append(to)

start = 0
for i in range(N):
    if A[i]:
        start += 2**i

dis = bfs(start)
print(dis[2**N-1])