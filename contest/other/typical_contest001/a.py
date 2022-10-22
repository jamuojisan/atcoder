import sys
sys.setrecursionlimit(10**9)
h,w = map(int, input().split())
c = []
for _ in range(h):
    c.append(input())

for i in range(h):
    for j in range(w):
        if c[i][j] == 's':
            sy, sx = i, j
        elif c[i][j] == 'g':
            gy, gx = i, j

visited = [[-1 for _ in range(w)] for _ in range(h)]
def dfs(y, x):
    visited[y][x] = 0
    for dy,dx in [(-1,0),(1,0),(0,1),(0,-1)]:
        if y + dy <h and y+ dy >=0 and x+dx>=0 and x+dx <w:
            if visited[y+dy][x+dx] == -1:
                if c[y+dy][x+dx]=='.' or c[y+dy][x+dx] =='g':
                    dfs(y+dy, x+dx)
   
dfs(sy,sx)

if visited[gy][gx] != -1:
    print('Yes')
else:
    print('No')