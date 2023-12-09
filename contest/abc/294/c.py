import bisect
N, M = map(int ,input().split())
A = list(map(int ,input().split()))
B = list(map(int ,input().split()))
C = sorted(A + B)
ans1 = []
count = 0
for i in range(N):
    index = bisect.bisect_right(B,A[i])
    ans1.append(index+count+1)
    count += 1
ans2 = []
count = 0
for i in range(M):
    index = bisect.bisect_right(A,B[i])
    ans2.append(index+count+1)
    count += 1
print(*ans1)
print(*ans2)
