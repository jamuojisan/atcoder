import heapq
N , D = map(int, input().split())
XY = []

for _ in range(N):
    x, y =map(int, input().split())
    heapq.heappush(XY,[x,y])

Y = []
ans = 0
for day in range(1, D+1):
    while(XY and XY[0][0] <= day):
        x,y = heapq.heappop(XY)
        heapq.heappush(Y, -y)
    if len(Y):
        y = heapq.heappop(Y)
        ans += -y
print(ans)