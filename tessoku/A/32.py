N, A, B = map(int, input().split())

dp = [False]*(N+1)

for i in range(N+1):
    if i < min(A,B):
        dp[i] = False
    if ((i-A)>=0 and dp[i-A] is False) or ((i-B)>=0 and dp[i-B] is False):
        dp[i] = True

if dp[N]:
    print('First')
else:
    print('Second')
