

from collections import deque

H, W = map(int, input().split())
C = [[*map(int, input().split())] for _ in range(H)]

count  = [[0]*W for _ in range(H)]
# uecount = [[0]*W for _ in range(H)]
# sitacount = [[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        c = C[i][j]
        _c  = 0
        for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ny, nx = i + dy, j + dx
            if 0 <= ny < H and 0<= nx < W:
                if c == C[ny][nx]:
                    _c +=1
        count[i][j] = _c

ans = 0
index_list = []
for i, _c in enumerate(count):
    if min(_c) == 0 and 0<i<H:
       index_list.append(i+1) 

print(len(index_list))