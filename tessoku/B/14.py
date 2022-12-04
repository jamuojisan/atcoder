import bisect
def bitsearch(lis):
    n = len(lis)
    ret = []
    for S in range(2**n):
        s = 0
        for j in range(n):
            if (S >> j) & 1 :
                s += lis[j]
        ret.append(s)
    return ret
N, K = map(int, input().split())
A = list(map(int, input().split()))

B = A[:N//2]
C = A[N//2:]

sumB = bitsearch(B)
sumC = sorted(bitsearch(C))

for i in sumB:
    j = bisect.bisect_left(sumC, K-i)
    if 0<=  j< len(sumC) and i + sumC[j] == K:
        print('Yes')
        exit()
print('No')
