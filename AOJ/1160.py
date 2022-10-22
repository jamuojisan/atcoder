import sys
sys.setrecursionlimit(10**9)
def dfs(y,x):
    if y <0 or y >=h or x <0 or x >=w:
        return
    if c[y][x] == 0:
        return
    if visited[y][x] != -1:
        return
    visited[y][x] = 1
    dfs(y,x-1)
    dfs(y,x+1)
    dfs(y-1,x)
    dfs(y+1,x)
    dfs(y-1,x-1)
    dfs(y-1,x+1)
    dfs(y+1,x-1)
    dfs(y+1,x+1)


while(True):
    w,h = map(int, input().split())
    if w == 0:
        break
    c = []
    for _ in range(h):
        c.append(list(map(int, input().split()) ))
    
    visited = [[-1 for _ in range(w)] for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if visited[i][j] != -1:
                continue
            elif c[i][j] == 0:
                continue
            else:
                dfs(i, j)
                ans +=1
    print(ans)
