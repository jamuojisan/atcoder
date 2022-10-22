n,m = map(int, input().split())
c = list(map(int,input().split()))

# dp = [[10**9 for _ in range(n+1)] for _ in range(m+1)] # dp[i][j] i枚目までのコインを使ってj円払うコインの最小枚数
# # for i in range(n+1):
# #     dp[0][i] = 0
# dp[0][0] = 0
# for i in range(m):
#     for j in range(n+1):
#         if j + c[i] <= n:
#             dp[i+1][j + c[i]] = min(dp[i][j] + 1, dp[i+1][j + c[i]])
#             dp[i+1][j + c[i]] = min(dp[i+1][j] + 1, dp[i+1][j+c[i]])
#         dp[i+1][j] = dp[i][j]

# ans = 10**9

# for i in range(m+1):
#     ans = min(ans, dp[i][n])
# print(ans)
# print(dp)

dp = [10**9 for _ in range(n+1)] # dp[i] i円払うのに必要な最小枚数
dp[0] =0
for i in range(n+1):
    for j in range(m):
        if i +c[j] <=n:
            dp[i + c[j]] = min(dp[i] + 1, dp[i + c[j]])
print(dp[n])

