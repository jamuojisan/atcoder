from collections import deque
import heapq
N, Q = map(int ,input().split())
ans = []
que = []
c = 1
done = set()
for _ in range(Q):
    q = input().split()
    if int(q[0]) == 1:
        heapq.heappush(que, c)
        c += 1
    elif int(q[0]) == 2:
        done.add(int(q[1]))
    else:
        call = set()
        while(1):
            v = heapq.heappop(que)
            if v not in done:
                call.add(v)
                ans.append(v)
                break
        for i in call:
            heapq.heappush(que, i)
for i in ans:
    print(i)