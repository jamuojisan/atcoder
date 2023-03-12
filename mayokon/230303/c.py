H, W = map(int ,input().split())
A = [input() for _ in range(H)]
h_flg = [0]*W
w_flg = [0]*H

for i in range(H):
    if A[i] == '.'*W:
        w_flg[i] = 1

for i in range(W):
    flg = True
    for j in range(H):
        if A[j][i] == '#':
            flg = False
            break
    if flg:
        h_flg[i] = 1

for i in range(H):
    flg = False
    for j in range(W):
        if not(h_flg[j] or w_flg[i]):
            flg = True
            print(A[i][j], end='')
    if flg:
        print()