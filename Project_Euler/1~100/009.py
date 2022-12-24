for i in range(1,999):
    for j in range(i+1,999):
        k = 1000 - i - j
        if k <= j:
            continue
        if i*i + j*j == k*k:
            print(i*j*k)
        