D, N = map(int, input().split())
T = [int(input()) for _ in range(D)]
ABC = []
for _ in range(N):
    a,b,c = map(int, input().split())
    ABC.append([a,b,c])
    
dp = [[0]*(N) for _ in range(D+1)]

for d in range(2,D+1):
    t1 = T[d-1]
    t2 = T[d-2]
    for n1 in range(N): #当日
        a1,b1,c1 = ABC[n1]
        if t1 < a1 or b1 < t1:
            continue
        for n2 in range(N): #前日
            a2, b2, c2 = ABC[n2]
            if t2 < a2 or b2 < t2:
                continue
            dp[d][n1] = max(dp[d][n1], dp[d-1][n2] + abs(c1-c2))

ans = 0
for i in range(N):
    ans = max(dp[D][i], ans)
print(ans)
