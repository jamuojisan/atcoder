import bisect
N = int(input())
A = list(map(int, input().split()))

ans = 0
dp = [0]*(N)
L = []

for i in range(N):
    pos = bisect.bisect_left(L, A[i])
    dp[i] = pos
    if dp[i] >= ans:
        L.append(A[i])
        ans +=1
    else:
        L[dp[i]] = A[i]

print(ans)