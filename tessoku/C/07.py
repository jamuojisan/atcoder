import bisect
N = int(input())
C = [*map(int, input().split())]
C.sort()
S = [0]
for i in range(N):
    S.append(S[-1] + C[i])
Q = int(input())

for i in range(Q):
    x = int(input())
    print(bisect.bisect(S,x)-1)