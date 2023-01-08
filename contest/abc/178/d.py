S = int(input())
mod = 10**9 + 7
if S <= 2:
    print(0)
    exit()
dp = [0]*(S+1)
dp[0] =1
for i in range(1,S+1):
    for j in range(3,S+1):
        if i-j >= 0:
            dp[i] += dp[i-j]
            dp[i] %= mod
print(dp[S])
# print(dp)
