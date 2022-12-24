n,s = map(int, input().split())
ab = []
for _ in range(n):
    a,b = map(int, input().split())
    ab.append([a,b])

dp = [[0 for _ in range(s+1)] for _ in range(n+1)]

dp[0][0] = 1

for i in range(n):
    for j in range(s+1):
        # aに関する条件
        if dp[i][j] == 1:
            if j + ab[i][0] <=s:
                dp[i+1][j+ab[i][0]] = 1
            if j + ab[i][1] <=s:
                dp[i+1][j+ab[i][1]] = 1
if dp[n][s] == 0:
    print('No\n')
else:
    print('Yes')
    ans = ''
    i=n
    val = s
    while(i>0):
        val1 = val - ab[i-1][0]
        val2 = val - ab[i-1][1]
        if dp[i-1][val1]:
            ans += 'H'
            val = val1
        else:
            ans += 'T'
            val = val2
        i = i-1
    ans = ''.join(list(reversed(ans)))
    print(ans)

