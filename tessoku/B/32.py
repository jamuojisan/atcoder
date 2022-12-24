N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [False for _ in range(N+1)]
minA = min(A)
for i in range(1,N+1):
    if i < minA:
        dp[i] = False
    for j in range(K):
        val = A[j]
        if i - val >= 0 and dp[i-val] is False:
            dp[i] = True
            break

if dp[N]:
    print('First')
else:
    print('Second')



