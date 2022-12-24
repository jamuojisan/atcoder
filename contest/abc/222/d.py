N = int(input())
# for all i に対して、a_i <= c_i <= b_i　が成り立つような
# 広義短調増加列Cの個数を求めよ。
A = [*map(int,input().split())]
B = [*map(int,input().split())]
M = 10
dp = [[0]*(M+1) for _ in range(N+1)]
mod =  998244353 
for i in range(M+1):
    dp[0][i] = 1
for i in range(1, N+1):
    a = A[i-1]
    b = B[i-1]
    for j in range(a, b+1):
        for k in range(a,j):
            dp[i][j] += dp[i-1][k]
            dp[i][j] %= mod
ans = 0
for i in range(M+1):
    ans += dp[N][i]
    ans %= mod
print(ans)

for i in dp:
    print(i)
