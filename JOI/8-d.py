import sys
import numpy as np
sys.setrecursionlimit(10**9)

def dfs(y, x, num):
    global depth
    c[y][x] = 0 #　氷を悪

    if num > depth:
        depth +=1

    for y_move, x_move in move:
        nx = x + x_move
        ny=  y + y_move

        if 0 <= ny <h and 0 <= nx < w and c[ny][nx] == 1:
            dfs(ny, nx, num+1)
    c[y][x] = 1 # もどす

w = int(input())
h = int(input())
    
c = []
for _ in range(h):
    c.append(list(map(int, input().split()) ))
move = [[-1, 0], [1,0], [0,-1], [0,1]]
max_depth = 0


for i in range(h):
    for j in range(w):
        if c[i][j] == 0:
            continue
        depth=0
        dfs(i,j, 1)
        max_depth = max(max_depth, depth)
print(max_depth)


