import sys
sys.setrecursionlimit(10**7)
from collections import deque

a, n = map(int, input().split())
M=1
while M <= n:
    M*=10
d = [-1]*M

q = deque()
q.append(1)
d[1] = 0
while len(q):
    
    v = q.popleft()
    
    val1 = v*a
    if val1 <M and d[val1] == -1:
        d[val1] = d[v] +1
        q.append(val1)
    if v > 10 and v%10 !=0:
        sv = str(v)
        val2 = int(sv[-1] +sv[:-1])
        if val2 < M and d[val2] == -1:
            d[val2] = d[v] + 1
            q.append(val2)

print(d[n])
    
        