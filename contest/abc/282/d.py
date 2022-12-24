from collections import deque
def bfs(G,a):
    visited[a] = 0
    q =deque()
    q.append(a)
    bi = True
    zero = [a]
    one = []

    while(len(q) > 0):
        v = q.popleft()
        for nv in G[v]:
            if visited[nv] != -1:
                if visited[v] == visited[nv]:
                    bi = False
                continue
            visited[nv] = 1 - visited[v]
            if visited[v] == 0:
                one.append(nv)
            else:
                zero.append(nv)
            q.append(nv)
    
    return bi, one, zero

N , M = map(int, input().split())
G = [[] for _ in range(N)]


for i in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    G[a].append(b)
    G[b].append(a)



ans =  N*(N-1)//2

continuous = []
visited = [-1] * N
for i in range(N):
    if visited[i] != -1:
        continue
    _ans = 0
    bi, zero, one = bfs(G, i)
    if bi is False:
        print(0)
        exit()

    ans -= len(zero)*(len(zero)-1)//2
    ans -= len(one)*(len(one)-1)//2
print(ans-M)
