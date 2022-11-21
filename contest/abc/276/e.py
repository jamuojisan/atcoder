import sys
input = sys.stdin.readline
def n_int():
    return int(input())

def n_str():
    return input()


def map_int():
    return map(int, input().split())

def n_list():
    return list(map(int, input().split()))

def n_lislis(n):
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    return a

import sys
sys.setrecursionlimit(10**7)
h, w= map_int()

c = []
for _ in range(h):
    c.append(input())


for i in range(h):
    for j in range(w):
        if c[i][j] =='S':
            y0, x0 = (i,j)
            break


visited = [[-1]*w for _ in range(h)]
from collections import deque
def bfs(y0, x0):
    visited = [[-1]*w for _ in range(h)]
    visited[y0][x0] = 0
    q =deque()
    q.append([y0,x0])

    while(len(q) > 0):
        y, x = q.popleft()
        for dy, dx in [[-1, 0], [1, 0], [0,-1], [0,1]]:
            ny , nx = y + dy, x+dx
            if ny < 0 or ny >=h or nx<0 or nx >=w:
                continue
            if visited[ny][nx] != -1 or c[ny][nx] == '#' or c[ny][nx] == 'S':
                continue
            visited[ny][nx] = visited[y][x] + 1
            q.append([ny,nx])
    
    return visited

for dy1, dx1 in [[-1, 0], [1, 0], [0,-1], [0,1]]:
    for dy2, dx2 in [[-1, 0], [1, 0], [0,-1], [0,1]]:
        if (dy1 == dy2) and (dx1 == dx2):
            continue
        ny1, nx1 = y0 + dy1, x0 + dx1
        ny2, nx2 = y0 + dy2, x0 + dx2
        if ny1 < 0 or ny1 >=h or nx1 < 0 or nx1 >= w or ny2 < 0 or ny2 >=h or nx2 < 0 or nx2 >= w:
            continue
        if c[ny1][nx1] =='#' or c[ny2][nx2] == '#':
            continue
        visited = bfs(ny1, nx1)
        if visited[ny1][nx1] != -1 and visited[ny2][nx2] != -1:
            print('Yes')
            exit()
print('No')
