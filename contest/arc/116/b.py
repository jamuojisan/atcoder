N = int(input())
A = [*map(int,input().split())]

dp1 = [[0]*2 for i in range(N+1)]
dp2 = [[0]*2 for i in range(N+1)]

for i in range(1, N+1):
    dp1[i][0] = max(dp1[i-1][1], dp1[i-1][0])
    dp1[i][1] = max(dp1[i][1], dp1[i-1][0] )
