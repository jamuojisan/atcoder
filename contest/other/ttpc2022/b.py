import itertools
N ,X = map(int, input().split())
A = [*map(int, input().split())]

dp = [[0]*(10**4) for _ in range(N+1)]

dp[0][X] = 1

for i in range(1, N+1):
    for j in range(10**4):
        if dp[i-1][j] >=1:
            for k in itertools.permutations(list(str(j))):
                k = list(k)
                if k[0] == 0:
                    continue
                money = int(''.join(k))
                if money < j:
                    continue
                if money - A[i-1] >= 0:
                    dp[i][money - A[i-1]] = max(dp[i-1][j]+1, dp[i][money - A[i-1]])
                dp[i][money] = max(dp[i-1][j], dp[i][money])

ans = 0
for i in range(10**4):
    ans = max(ans, dp[N][i])
print(max(ans-1,0))
