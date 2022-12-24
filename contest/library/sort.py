def bubble_sort(data, n):
    count  = 0
    for i in range(n):                                      # i=0からnまでのループ
        for j in range(n-1, i, -1):                         # n-1からiまでの逆ループ
            if data[j-1] > data[j]:                         # 隣り合う値を比較
                count  += 1
                data[j], data[j-1] = data[j-1], data[j]     # 交換
    return count