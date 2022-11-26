N = int(input())
A = list(map(int, input().split())) # A[i]= i kara i+ 1 madeno dis 0 <= i <= N-2
B = list(map(int, input().split())) # B[i]= i kara i+ 2 madeno dis 1 <= i <= N-2
B.append(0)
dp = [10**9]*(N) # dp[i] = ibanmeno minimum dis
dp[0] = 0
dp[1] = A[0]

for i in range(2,N):
    dp[i] = min(dp[i-1] + A[i-1], dp[i-2] + B[i-2])

ans= [N]
loc = N-1
while(loc>0):
    dis1 = dp[loc] - dp[loc-1]
    dis2 = dp[loc] - dp[loc-2]
    if dis1 == A[loc-1]:
        ans.append(ans[-1] - 1)
        loc -=1
    else:
        ans.append(ans[-1] - 2)
        loc -= 2
print(len(ans))
print(*ans[::-1])
    
