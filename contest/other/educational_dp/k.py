N ,K = map(int, input().split())
A = [*map(int, input().split())]
dp = [False for _ in range(K+1)]
mn_a = min(A)
for k in range(1,K+1):
    if k < mn_a:
        dp[k] = False
        continue
    for i in A:
        if k - i >= 0 and dp[k-i] is False:
            dp[k] = True

if dp[K]:
    print('First')
else:
    print('Second')

    

