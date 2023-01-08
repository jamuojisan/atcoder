def bubble_sort(data, n):
    count  = 0
    for i in range(n):                                      # i=0からnまでのループ
        for j in range(n-1, i, -1):                         # n-1からiまでの逆ループ
            if data[j-1] > data[j]:                         # 隣り合う値を比較
                count  += 1
                data[j], data[j-1] = data[j-1], data[j]     # 交換
    return count
S = input().split()
T = input().split()
RGB2index = {'R':0, 'G':1, 'B':2}
SS = [RGB2index[i] for i in S]
TT = [RGB2index[i] for i in T]
n1, n2 = bubble_sort(SS,3), bubble_sort(TT,3)
if (10**18 - n1+n2) % 2 == 0:
    print('Yes')
else:
    print('No')