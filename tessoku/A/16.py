N = int(input())
A = list(map(int, input().split())) # A[i]= i kara i+ 1 madeno dis 0 <= i <= N-2
B = list(map(int, input().split())) # B[i]= i kara i+ 2 madeno dis 1 <= i <= N-2
B.append(0)
dp = [10**9]*(N+1) # dp[i] = ibanmeno minimum dis
dp[0] = 0
dp[1] = A[0]

for i in range(2,N):
    dp[i] = min(dp[i-1] + A[i-1], dp[i-2] + B[i-2])

print(dp[N-1])  