def bubble_sort(data, n):
    count  = 0
    for i in range(n):                                      # i=0からnまでのループ
        for j in range(n-1, i, -1):                         # n-1からiまでの逆ループ
            if data[j-1] > data[j]:                         # 隣り合う値を比較
                count  += 1
                data[j], data[j-1] = data[j-1], data[j]     # 交換
    return count

N = int(input())
P = [list(map(int, input().split())) for i in range(N)]
tate = []
for i in range(N):
    for j in range(N):
        if P[i][j] != 0:
            tate.append(P[i][j])
            
yoko = []
for j in range(N):
    for i in range(N):
        if P[i][j] != 0:
            yoko.append(P[i][j])
tatecount = bubble_sort(tate, N)
yoko_count = bubble_sort(yoko, N)

print(tatecount + yoko_count)
