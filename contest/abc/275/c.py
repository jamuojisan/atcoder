S = [input() for _ in range(9)]
ans = set()
import math
v = []
for i in range(9):
    for j in range(9):
        if S[i][j] == '#':
            v.append((i, j))
import itertools
permutation = list(itertools.combinations(v, 4))
ans = 0
for p in permutation:
    twopoints = list(itertools.combinations(p, 2))
    lengthlist = list()
    for pair in twopoints:
        distance = (pair[0][0] - pair[1][0]) **2 + (pair[0][1] - pair[1][1]) **2
        lengthlist.append(distance)
    lengthlist.sort()
    
    if lengthlist[0] == lengthlist[1] == lengthlist[2] == lengthlist[3] and (lengthlist[4] == lengthlist[5]) and (lengthlist[0]*2 == lengthlist[5]):
        ans +=1
print(ans)
