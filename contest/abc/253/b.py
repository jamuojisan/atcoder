H ,W = map(int, input().split())
S = [input() for _ in range(H)]

flg = False
for i in range(H):
    for j in range(W):
        if S[i][j] == 'o':
            if flg is False:
                koma1 = [i,j]
                flg = True
            else:
                koma2 = [i,j]
print(abs(koma1[0]-koma2[0]) + abs(koma1[1]-koma2[1]))