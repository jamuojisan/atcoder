N =int(input())
A = sorted([*map(int, input().split())], reverse= True)
import heapq
ans = 0
p = []
for i in range(N):
    if i >0:
        ans += p[0]
    heapq.heappush(p, A[i])
print(ans)