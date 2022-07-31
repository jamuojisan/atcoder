import numpy as np

INF = 10**9

n, m = map(int, input().split())
x = list(map(int, input().split()))
b = np.zeros(n+1, np.int64)
for _ in range(m):
    c, y = map(int, input().split())
    b[c] = y

dp = np.zeros(n+1, np.int64)


for i in range(1,n+1):
    d0 = dp.max()
    dp[1:i+1] = dp[:i] + x[i-1] +b[1:i+1]
    dp[0] = d0
print(dp.max())

