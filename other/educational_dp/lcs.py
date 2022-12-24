S = input()
T = input()
N = len(S)
M = len(T)

dp = [[0]*(M+1) for _ in range(N+1)]

ans = ''
for n in range(1, N+1):
    s = S[n-1]
    for m in range(1, M+1):
        dp[n][m] = max(dp[n-1][m], dp[n][m], dp[n][m-1])
        t = T[m-1]
        if s == t:
            dp[n][m] = max(dp[n][m], dp[n-1][m-1] + 1)


# 復元
l = dp[N][M]
i = N - 1
j = M - 1
ans = [0] * l
while(l > 0):
    if S[i] == T[j]:
        ans[l-1] = S[i]
        i -=1
        j -=1
        l -=1
    elif dp[i+1][j+1] == dp[i][j+1]:
        i -= 1
    else:
        j -= 1
        
print(''.join(ans))

