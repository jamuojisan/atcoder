N , M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

dp = [[10**9]*(2**N) for _ in range(M+1)]
dp[0][0]=0

for i in range(1, M+1):
    T  = 0
    for k, j in enumerate(A[i-1]):
        T += j*2**(k)
    for S in range(2**N):
        dp[i][S] = min(dp[i-1][S], dp[i][S])
        dp[i][S|T] = min(dp[i][S|T], dp[i-1][S] +1)
if dp[M][2**N-1]==10**9:
    print(-1)
else:
    print(dp[M][2**N-1])

