n ,m = map(int, input().split())
import math
from collections import deque
selection = []

for i in range(int(math.sqrt(m)) +1):
    for j in range(int(math.sqrt(m))+1):
        if i**2 + j**2 == m:
            selection.append([i,j])
            selection.append([-i,j])
            selection.append([i,-j])
            selection.append([-i,-j])
visited = [[-1]*n for _ in range(n)]
visited[0][0] = 0
q = deque()
q .append([0,0])

while(len(q) > 0):
    y ,x = q.popleft()
    for dy, dx in selection:
        ny, nx  = y +dy, x + dx
        if ny < 0 or ny >=n or nx < 0 or nx >=n:
            continue
        if visited[ny][nx] == -1:
            visited[ny][nx] = visited[y][x] + 1
            q.append((ny, nx))
            
    
for i in range(n):
    print(*visited[i])
