from collections import deque 
n, h , w, p ,q = map(int, input().split())
field = [[0]*w for _ in range(h)]
for _ in range(n):
    _p, _q = map(int,input().split())
    field[_p][_q] = 1
visited = [[-1]*w for _ in range(h)]
ans = [[] for _ in range(201)]
Q = deque()
Q.append([p,q])
visited[p][q] = 0
if field[p][q] == 0:
    print(p,q)
    exit()
while len(Q) > 0:
    y, x = Q.popleft()
    for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
        if y + dy >= h or  y + dy <0:
            continue
        if x + dx >= w or x + dx <0:
            continue
        if visited[y+dy][x+dx] == -1:
            visited[y+dy][x+dx] = visited[y][x] + 1
            if field[y+dy][x+dx] == 0:
                ans[visited[y][x] + 1].append([y+dy,x+dx])
            Q.append((y+dy, x+dx))


for index in range(201):
    if len(ans[index]) != 0:
        for _ans in sorted(ans[index]):
            print(*_ans)
        exit()

