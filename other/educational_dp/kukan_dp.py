import sys
sys.setrecursionlimit(10**9)
def kukan(l, r):
    if l == r:
        return 0
    if done[l][r]:
        return dp[l][r]
    done[l][r] = True
    if (N - (r-l)) %2 == 0: # 先手
        dp[l][r] = max(A[l] + kukan(l+1, r), kukan(l, r-1) + A[r-1])
    else: # 後手
        dp[l][r] = min(-A[l] + kukan(l+1,r), kukan(l,r-1) - A[r-1])
    return dp[l][r]

N = int(input())
A = [*map(int,input().split())]

dp = [[None]*(N+2) for _ in range(N+2)] # 区間[i,j)の数列から初めて最善種をとったときの最終的なX-Yの値
done = [[False]*(N+2) for _ in range(N+2)]
# 初期化
for i in range(N+1):
    dp[i][i] = 0

print(kukan(0, N))