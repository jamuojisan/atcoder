Q = int(input())
from collections import defaultdict
import heapq
ans = defaultdict(int)
mx = []
mn = []
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        ans[q[1]] +=1
        heapq.heappush(mx, -q[1])
        heapq.heappush(mn, q[1])
    elif q[0] == 2:
        x, c = q[1:]
        ans[x] = max(0, ans[x]-c)
    else:
        while(ans[-mx[0]]) == 0:
            heapq.heappop(mx)
        while(ans[mn[0]]) ==0:
            heapq.heappop(mn)
        print(-mx[0]- mn[0])