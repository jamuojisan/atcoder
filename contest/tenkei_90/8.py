# 耳DP-
n = int(input())
s = input()
def add(a, b):
    a += b
    a %= mod
    return a
dp = [[0]*(8) for _ in range(n+1)]
usemoji = 'atcoder'
mod =10**9 +7
dp[0][0] = 1

for i in range(1,n+1):
    moji = s[i-1]
    for j in range(8):
        dp[i][j]  = add(dp[i][j], dp[i-1][j])
        if j>0 and moji == usemoji[j-1]:
            dp[i][j] = add(dp[i][j], dp[i-1][j-1])
print(dp[n][7])     


