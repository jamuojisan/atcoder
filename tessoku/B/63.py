from collections import deque 
r,c = map(int, input().split())


sy,sx = map(int, input().split())
sy, sx = sy-1, sx-1
gy,gx = map(int, input().split())
gy, gx = gy-1, gx-1
mapG = []
for i in range(r):
    _ = input()
    mapG.append(_)

Q = deque()
Q.append([sy,sx])

visited = [[-1 for i in range(c)] for j in range(r)]
visited[sy][sx]= 0

while len(Q) > 0:
    y, x = Q.popleft()
    for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
        if y + dy >= r or  y + dy <0:
            continue
        if x + dx >= c or x + dx <0:
            continue
        if mapG[y+dy][x+dx] == '#':
            continue
        if visited[y+dy][x+dx] == -1:
            visited[y+dy][x+dx] = visited[y][x] + 1
            Q.append((y+dy, x+dx))
print(visited[gy][gx])

