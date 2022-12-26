import sys
sys.setrecursionlimit(10**7)
def kukan_dp(l, r):
    if dp[l][r] != -1:
        return dp[l][r]
    if r-l <= 1:
        dp[l][r] =0
        return 0
    
    # lをたたく
    lp, la = PA[l]
    dp[l][r] = max(kukan_dp(l+1, r), dp[l][r]) # 加算されない時
    if l <= lp < r:
        dp[l][r] = max(dp[l+1][r] + la, dp[l][r])
    
    # r-1をたたく
    rp, ra = PA[r-1]
    dp[l][r] = max(kukan_dp(l,r-1), dp[l][r])
    if l <= rp < r:
        dp[l][r] = max(dp[l][r-1] + ra, dp[l][r])
    
    return dp[l][r]


N = int(input())
PA = []
for _ in range(N):
    p, a = map(int, input().split())
    PA.append([p-1, a])

dp = [[-1]*(N+1) for _ in range(N)] # dp[i][j] 区間[i,j)での答え

# 初期条件はdp[i][i] = 0
for i in range(N):
    dp[i][i] = 0

print(kukan_dp(0,N))