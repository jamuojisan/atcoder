import sys
sys.setrecursionlimit(10**9)

from collections import defaultdict
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

def dfs(f, node, _flag):
    if len(G[node]) != 2:
        _flag = False
    if  node == f and visited[f] is True:
        _flag = True
        return True
    visited[node] = True
    for nv in G[node]:
        if visited[nv] is False or (visited[nv] and nv == f):
            if visited[nv] and nv ==f:
                _flag = True
            else:
                _flag = dfs(f, nv, _flag)
        else:
            _flag  = False
    return _flag
N, M = map(int, input().split())
ABCD = [[*map(str, input().split())] for _ in range(M)]
G = [[] for _ in range(2*N)]
uf = UnionFind(2*N)
for i in range(N):
    G[2*i].append(2*i+1)
    G[2*i+1].append(2*i)
    uf.union(2*i, 2*i+1)

for a, b, c, d in ABCD:
    a, c = int(a), int(c)
    a, c = a-1, c-1
    if b == 'R':
        l = 2*a + 1
    else:
        l = 2*a
    if d == 'R':
        r = 2*c + 1
    else:
        r = 2*c
    G[l].append(r)
    G[r].append(l)
    uf.union(l, r)
node2num ={node:len(G[node]) for node in range(2*N)}
all_member = uf.all_group_members()
ans1= 0
ans2 = 0
for n in all_member:
    member = all_member[n]
    flg = True
    for m in member:
        if node2num[m] != 2:
            flg = False
    if flg:
        ans1 += 1
    else:
        ans2 += 1
print(ans1, ans2)
# visited = [False]*(2*N)


# for i in range(2*N):
#     if visited[i] is False:
#         fv = sum(visited)
#         flg = dfs(i, i, True)
#         tv = sum(visited)
#         print(i, (tv-fv), flg)
#         if flg and tv - fv != 2:
#             ans1 += 1
#         else:
#             ans2 += 1
# print( ans1, ans2)
        
    