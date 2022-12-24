n, m = map(int, input().split())
S = [0]
C = [0]

for _ in range(m):
    s, c = map(str, input().split())
    s_val = 0
    for j in range(n):
        if s[j] == 'Y':
            s_val |= 1 << j
    S.append(s_val)
    C.append(int(c))

inf = 10 **20
dp = [[inf]*(2**n) for _ in range(m+1)] # dp[i][n] セット1 ~ iまでを買うかどうか決めた時の、そろった部品集合がnであるときのコスト最小値
dp[0][0] = 0
for i in range(1,m+1):
    for N in range(2**n):
        # セットiを買わない
        dp[i][N] = min(dp[i][N], dp[i-1][N])
        # セットiを買う
        dp[i][N|S[i]] = min(dp[i][N|S[i]], dp[i-1][N] + C[i])

ans = dp[m][2**n - 1]

if ans == inf:
    print(-1)
else:
    print(ans)
