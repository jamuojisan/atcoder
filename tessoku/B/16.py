N = int(input())
h = list(map(int, input().split()))

inf = 10** 9
dp = [inf for _ in range(N)]
dp[0] = 0
dp[1] = abs(h[1] - h[0])
for i in range(2, N): 
    dp[i] = min(dp[i], dp[i-1] + abs(h[i]-h[i-1]))
    if i -2 >= 0:
        dp[i] = min(dp[i], dp[i-2] + abs(h[i] - h[i-2]))
print(dp[N-1]) 