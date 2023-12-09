H ,W = map(int ,input().split())
A = [input() for _ in range(H)]
from collections import defaultdict

count = defaultdict(int)

def get_aij(l, m):
    if 0 <= l < H and 0<= m <W:
        return A[l][m]
    else:
        return '.' 
for n in range(1, min(H,W)+1):
    for h in range(H):
        for w in range(W):
            if A[h][w] != '#':
                continue
            i1 = 0 if get_aij(h+n+1, w+n+1) == '.' else 1
            i2 = 0 if get_aij(h+n+1, w-n-1) == '.' else 1
            i3 = 0 if get_aij(h-n-1, w+n+1) == '.' else 1
            i4 = 0 if get_aij(h-n-1, w-n-1) == '.' else 1
            flg = True if i1*i2*i3*i4 == 0 else False
            if flg is False:
                continue
            for d in range(1,n+1):
                if not(get_aij(h+d,w+d) == get_aij(h+d,w-d) == get_aij(h-d, w+d) == get_aij(h-d, w-d) == '#'):
                    flg = False
                    break
            if flg:
                count[n] += 1
for i in range(1, min(H,W)+1):
    print(count[i], end =' ')