H ,W, K = map(int ,input().split())
C = [input() for _ in range(H)]
ans = 0
for h in range(2**H):
    r = []
    for i in range(H):
        if h & (1<<i):
            r.append(i)
    for w in range(2**W):
        c = []
        for i in range(W):
            if w & (1<<i):
                c.append(i)
        count = 0
        for i in range(H):
            for j in range(W):
                if i in r or j in c:
                    continue
                else:
                    if C[i][j] == '#':
                        count += 1
        if count == K:
            ans +=1
print(ans)