
from tokenize import group
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

n,m = map(int, input().split())
ab= []
for i in range(m):
    a,b = map(int, input().split())
    a,b = a-1, b-1
    ab.append([a,b])

uf = UnionFind(n)
ans = [n*(n-1)//2]
ing = set()
for a,b in reversed(ab):
    if uf.same(a,b):
        ans.append(ans[-1])
    else:
        n1 = uf.size(a)
        n2 = uf.size(b)
        ans.append(ans[-1]-(n1*n2))
    uf.union(a,b)

for i,j in enumerate(reversed(ans)):
    if i == 0:
        continue
    print(j)
    