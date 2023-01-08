H1, W1 = map(int, input().split())
A =[[*map(int, input().split())] for _ in range(H1)]
H2, W2= map(int, input().split())
B =[[*map(int, input().split())] for _ in range(H2)]

# 各列各行を削除するかのbit探索
for h in range(2**H1):
    row = []
    for i in range(H1):
        if (h >> i) & 1:
            row.append(i)
    if len(row) != H2:
        continue
    for w in range(2**W1):
        column = []
        for i in range(W1):
            if (w >> i) & 1:
                column.append(i)
        if len(column) != W2:
            continue

        # 行列があっているか判定
        flg = True
        for i1,i2 in enumerate(row):
            for j1,j2 in enumerate(column):
                if A[i2][j2] != B[i1][j1]:
                    flg = False
                    break
        if flg:
            print('Yes')
            exit()
print('No')
