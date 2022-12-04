N ,K = map(int, input().split())
S = 31
dp = [[0]*(S+1) for i in range(N+1)]

def digit_sum(val):
    return sum([int(i) for i in list(str(val))])
for i in range(N+1):
    dp[i][0] = i - digit_sum(i)

for i in range(1, N+1):
    for j in range(1,S+1):
        dp[i][j] = dp[dp[i][j-1]][j-1]

bk = [int(i) for i in bin(K)[2:][::-1]]

for i in range(1, N+1):
    ans = i
    for index, j in enumerate(bk):
        if j:
            ans = dp[ans][index]
    print(ans)

