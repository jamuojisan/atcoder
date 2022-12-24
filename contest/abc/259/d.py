n = int(input())
import math
def in_circle(x,y):
    for i in range(n):
        x0, y0, r = xyr[i]
        if (x-x0)**2 + (y-y0)**2 == r**2:
            return True, i
    return False, -1

from collections import deque
def bfs(G,a):
    visited = [-1 for _ in range(n)]
    visited[a] = 0
    q =deque()
    q.append(a)

    while(len(q) > 0):
        v = q.popleft()
        for nv in G[v]:
            if visited[nv] != -1:
                continue
            visited[nv] = visited[v] + 1
            q.append(nv)
    
    return visited


sx, sy, tx, ty = map(int, input().split())

G = [[] for _ in range(n)]
xyr =[]
for _ in range(n):
    x, y, r = map(int,input().split())
    xyr.append([x,y,r])

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        x1, y1, r1 = xyr[i]
        x2, y2, r2 = xyr[j]
        dis = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        if((x1 -x2)**2 + (y1-y2)**2 < (r1 - r2)**2):
            continue
        if((x1 -x2)**2 + (y1-y2)**2 > (r1 + r2)**2):
            continue

        G[i].append(j)
        G[j].append(i)

flg1, ind0 = in_circle(sx,sy)
flg2, ind2 = in_circle(tx,ty)

if ind0 < 0 or ind2 < 0:
    print('No')
else:
    visited = bfs(G,ind0)
    if visited[ind2] != -1:
        print('Yes')
    else:
        print('No')