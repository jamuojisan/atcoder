N = int(input())
PA = []
for _ in range(N):
    p,a = map(int, input().split())
    PA.append([p-1,a])

dp = [[0]*(N) for _ in range(N)] #dp[l][r]= [l,r]のブロックが残っているときの最大値

for length in reversed(range(N-1)):
    for l in range(N-length):
        r = length + l
        if l != 0:
            pl, al = PA[l-1]
            if l-1<= pl <= r:
                dp[l][r] = max(dp[l][r], dp[l-1][r]+ al)
            else:
                dp[l][r] = max(dp[l][r], dp[l-1][r])
        if r != N-1:
            pr, ar = PA[r+1]
            if l<= pr <= r+1:
                dp[l][r] = max(dp[l][r], dp[l][r+1] + ar)
            else:
                dp[l][r] = max(dp[l][r], dp[l][r+1])

ans = 0

for i in range(N):
    ans = max(ans, dp[i][i])
print(ans)