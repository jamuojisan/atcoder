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

ans = [N]
loc = N-1
while(loc > 0):
    if loc == 1:
        ans.append(1)
        break
    dis1 = dp[loc] - dp[loc-1]
    dis2 = dp[loc] - dp[loc-2]
    if dis2 == abs(h[loc]- h[loc-2]) :
        ans.append(loc -1)
        loc -= 2
    else:
        ans.append(loc)
        loc -=1
ans.reverse()
print(len(ans))
print(*ans)
