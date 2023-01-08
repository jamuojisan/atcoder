import math
N = int(input())
edges = []
for _ in range(N):
    x, y = map(int, input().split())
    edges.append((x,y))

ans = set()

for i in range(N):
    for j in range(i+1, N):
        xi, yi = edges[i]
        xj, yj = edges[j]
        x = xi-xj
        y = yi-yj
        gcd = math.gcd(abs(x),abs(y))
        ans.add((x//gcd, y//gcd))
        ans.add((-x//gcd, -y//gcd))
print(len(ans))