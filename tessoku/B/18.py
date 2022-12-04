N, S = map(int, input().split())
A = list(map(int, input().split()))
dp = [[False]*(S+1) for _ in range(N+1)]
dp[0][0] = True

for i in range(1 ,N+1):
    for j in range(S+1):
        dp[i][j] = dp[i][j] | dp[i-1][j]
        if j - A[i-1] >= 0 and dp[i-1][j - A[i-1]]:
            dp[i][j] = True

if dp[N][S]:
    ans = []
    loc_s = S
    for loc in reversed(range(1,N+1)):
        val = A[loc-1]
        if dp[loc-1][loc_s]:
            loc_s = loc_s -0
        else :
            ans.append(loc)
            loc_s -=  val
    ans.reverse()
    print(len(ans))
    print(*ans)
        
else:
    print(-1)
