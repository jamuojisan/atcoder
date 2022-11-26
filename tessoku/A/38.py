D, N = map(int, input().split())
LRH = []
limit = [24]*(D)
for _ in range(N):
    l,r,h = map(int, input().split())
    l, r = l-1, r-1
    for i in range(l,r+1):
        limit[i] = min(limit[i], h)

ans = 0
for i in limit:
    ans += i
print(ans)
