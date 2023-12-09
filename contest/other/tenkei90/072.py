from collections import deque

# bfs 2次元グリッドver
def dfs(c, y0, x0, visited, depth):
    if y0==sy and sx == x0:
        global mx
        mx = max(mx,depth)
    visited[y0][x0] = depth
    flg = False
    for dy, dx in [[-1, 0], [1, 0], [0,-1], [0,1]]:
        ny, nx = y0 + dy, x0+dx
        if ny < 0 or ny >=H or nx<0 or nx >=W:
                continue
        if visited[ny][nx] == -1 or visited[ny][nx] == 0:
            flg = True
            dfs(c, ny, nx, visited, depth + 1)
        if flg is False:
            return

H, W = map(int, input().split())
S = [input() for _ in range(H)]

mx = -1
for i in range(H):
    for j in range(W):
        sy, sx = i, j
        dfs(S,i, j, [[-1]*W for _ in range(H)], 0)

print(mx)
                    