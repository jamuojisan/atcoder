q = int(input())

for _ in range(q):
    s1 = input()
    s2 = input()
    n, m = len(s1), len(s2)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)] # dp[i][j] s1のi文字目、s2のj文字目までの最長部分列の長さ
    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    print(dp[n][m])

