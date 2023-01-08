N, M = map(int,input().split())
X = [[*map(int, input().split())] for _ in range(M)]
X = [set(l[1:]) for l in X]
for i in range(1, N+1):
    for j in range(1, N+1):
        flg = False
        if i==j:
            continue
        for k in range(M):
            if i in X[k] and j in X[k]:
                flg = True
                break
        if flg is False:
            print('No')
            exit()
print('Yes')
