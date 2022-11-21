def apend_(index, val, lis):
    if index == N and 3<=len(val)<=16:
        lis.append(val)
        return lis
    if 0 < 16 - len(val) - len(kumi[index]):
        for i in range(16 - len(val) - len(kumi[index])):
            val += '_'
            lis =  apend_(index+1, val+kumi[index], lis)
    return lis
import itertools
import sys
sys.setrecursionlimit(10**9)
N, M = map(int, input().split())
S = [input() for _ in range(N)]
if M == 0:
     T = []
else:
    T = sorted([input() for _ in range(M)])

def apend_(index, val, lis):
    if index == N and 3<=len(val)<=16:
        lis.append(val)
        return lis
    elif index == N:
        return lis
    if N >1:
        if 0 < 16 - len(val) - len(kumi[index]):
            for i in range(16 - len(val) - len(kumi[index])):
                val += '_'
                lis =  apend_(index+1, val+kumi[index], lis)
    return lis
for kumi in itertools.permutations(S, N):
    kumi = list(kumi)
    kumiawase = apend_(1,kumi[0], [])
    if len(T) > 0:
        for target in kumiawase:
            ok = 0
            ng = M
            while(ng- ok  >1):
                mid = (ok + ng)//2
                if T[mid] <= target:
                    ok = mid
                else:
                    ng = mid
            if T[ok] != target:
                print(target)
                exit()
    else:
        if len(kumiawase) > 0:
            print(kumiawase[0])
            exit()



print(-1)
    
