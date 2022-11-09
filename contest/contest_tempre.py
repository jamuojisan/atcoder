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
            sy, sx = (i,j)
            break


visited = [[-1]*w for _ in range(h)]
def dfs(y, x, ny, nx):
    if  ny < 0 or ny >=h or nx <0 or nx >=w:
        return
    if c[ny][nx] == '#':
        return  
    if c[ny][nx] == 'S':
        if visited[y][x]+ 1 >=4:
            print('Yes')
            exit()
    if visited[ny][nx] != -1:
        return
    visited[ny][nx] = visited[y][x] + 1
    for dy,dx in [(-1,0),(1,0),(0,1),(0,-1)]:
        dfs(ny, nx, ny+dy, nx+dx)
                
   
dfs(sy,sx,sy,sx)
 
print('No')
