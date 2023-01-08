H ,W = map(int, input().split())
C = [input() for _ in range(H)]

def dfs(y,x,depth, visited):
    global ans 
    ans = max(ans, depth)
    visited[y][x] = 0
    for dy,dx in [[1,0], [0,1]]:
        ny,nx = y+dy, x+dx
        if  0<= ny<H and 0<=nx<W and C[ny][nx] =='.':
            if visited[ny][nx] == -1:
                dfs(ny,nx, depth+1, visited)

ans = 0
dfs(0,0,0, [[-1]*W for _ in range(H)])


print(ans+1)