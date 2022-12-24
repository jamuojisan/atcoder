N = int(input())
A = list(map(int, input().split()))
G = [[] for _ in range(N)]
for i in range(N-1):
    n = A[i]
    G[n-1].append(i+1)
dp = [0] * N
for i in reversed(range(N)):
    ans = 0
    for j in G[i]:
        ans += (dp[j]+1)
    dp[i] = ans

print(*dp)    


