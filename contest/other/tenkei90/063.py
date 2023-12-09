H , W= map(int,  input().split())
P = [[*map(int, input().split())]  for i in range(H)]

mx = 0
from collections import defaultdict
for i in range(1, 2**H):
    same = []
    for j in range(H):
        if (i >> j) & 1 == 1:
            same.append(j)
    cnt = defaultdict(int)
    for w in range(W):
        n = P[same[0]][w]
        flg = True
        for j in same:
            if n != P[j][w]:
                flg = False
                break
        if flg:
            cnt[n] += 1
    mx_c = 0
    for c in cnt:
        mx_c = max(mx_c, cnt[c])
    mx = max(mx, mx_c*len(same))
print(mx)
        