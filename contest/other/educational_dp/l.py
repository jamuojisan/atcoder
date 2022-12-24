import sys
from collections import deque, defaultdict
sys.setrecursionlimit(10**7)
def f(l, r):
    if flag[l][r]:
        return dp[l][r]
    flag[l][r] = 1
    if l == r:
        dp[l][r] = A[l]
    dp[l][r] = max(A[l]-f(l+1,r), A[r] -f(l,r-1))
    return dp[l][r]

N = int(input())
A = [*map(int, input().split())]
flag = [[False]*(N+1) for _ in range(N+1)]
dp = [[0]*(N+1) for _ in range(N+1)]
ans = f(1,N)