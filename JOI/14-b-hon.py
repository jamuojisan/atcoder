import sys 
sys.setrecursionlimit(10**7)
def saiki_dp(l, r):
    if dp[l][r] != -1:
        return dp[l][r]
    if r-l <1:
        return 0
    
    # lを食べる.


N = int(input())
A = [*map(int, input().split())]
A = A + A

dp = [[-1]*(2*N+1) for _ in range(2*N)]
for i in range(2*N):
    dp[i][i] = 0
print(saiki_dp(0,2*N))
