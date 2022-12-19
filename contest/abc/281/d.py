N ,K , D = map(int, input().split())
A = [*map(int, input().split())]

# dp[i][j][k] a_1,,,a_i までからj個選んだ時の和の余りがkの時の最大値
dp = [[[-1]*(D) for _ in range(K+1)] for _ in range(N+1)]

dp[0][0][0] = 0
for i in range(1, N+1):
    for j in range(K+1):
        for k in range(D):
            # 選ばないとき
            dp[i][j][k] = max(dp[i-1][j][k], dp[i][j][k])
            # 選ぶとき
            if j == 0:
                continue
            
            val = (k - A[i-1])%D
            if dp[i-1][j-1][val] != -1:
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][val] + A[i-1])

print(dp[N][K][0])
