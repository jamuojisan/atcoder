N = int(input())
T = [*map(int, input().split())]

dp = [[False]*(10**5+1) for _ in range(N+1)]# dp[i][j]: T1 ... Ti まで選んでｊにできるか
dp[0][0] = True
for i in range(1,N+1):
    for j in range(1,10**5+1):
        dp[i][j] = dp[i][j] | dp[i-1][j]
        if j- T[i-1] >= 0 and dp[i-1][j-T[i-1]]:
            dp[i][j] = True
S = (sum(T)+1)//2
for i in range(S,10**5+1):
    if dp[N][i]:
        print(i)
        exit()