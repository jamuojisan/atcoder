n = int(input())
from collections import defaultdict
from sys import stdin
import sys
sys.setrecursionlimit(10**5 + 100)
G = defaultdict(list)
for _ in range(n-1):
    a, b = map(int , stdin.readline().split())
    a,b = a-1, b-1
    G[a].append(b)
    G[b].append(a)

color = [-1 for _ in range(n)]

def dfs(node, col):
    color[node] = col
    for to in list(G[node]):
        if color[to] != -1:
            continue
        dfs(to, 1 - col)
dfs(0,0)
ans1 = []
ans0 = []
for i in range(n):
    if color[i] == 1:
        ans1.append(i+1)
    else:
        ans0.append(i+1)
if len(ans1) >= len(ans0):
    print(*ans1[:n//2])
else:
    print(*ans0[:n//2]) 