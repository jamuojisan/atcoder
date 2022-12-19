from collections import deque
def bfs(c, y0, x0):
    visited = [[[-1]*4] for _ in range(W) for _ in range(H)]
    visited[y0][x0][0] = 0
    visited[y0][x0][1] = 0
    visited[y0][x0][2] = 0
    visited[y0][x0][3] = 0
    q =deque()
    q.append([y0,x0, -1, -1])

    while(len(q) > 0):
        y, x, ddy, ddx = q.popleft()
        for dy, dx in [[-1, 0], [1, 0], [0,-1], [0,1]]:
            ny , nx = y + dy, x+dx
            if ny < 0 or ny >=H or nx<0 or nx >=W:
                continue
            if visited[ny][nx] != -1 or c[ny][nx] == '#':
                continue
            if ddy * dy == 0 and  ddx * dx == 0:
                visited[ny][nx] = visited[y][x] + 1
            else:
                visited[ny][nx] = visited[y][x]
            q.append([ny,nx, dy, dx])
    
    return visited

H ,W = map(int, input().split())
rs, cs = map(int, input().split())
rt, ct = map(int, input().split())
rs, rt, cs, ct = rs-1, rt-1, cs-1, ct-1
C = [input() for _ in range(H)]
visited = bfs(C, rs, cs)
print(visited[rt][ct])