
six = [6**i for i in range(1, 8)]
nine = [9**i for i in range(1,7)]
N = int(input())
dp = [10**9] * (N+1)
dp[0] = 0

for i in range(1, N+1):
    for j in six+nine+[1]:
        if i-j >= 0:
            dp[i] = min(dp[i], dp[i-j] + 1)
print(dp[N])
     

