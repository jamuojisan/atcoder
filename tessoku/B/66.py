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
N ,M = map(int, input().split())
edges = []

for _ in range(M):
    a, b = map(int, input().split())
    a ,b = a-1, b-1
    edges.append([a,b])

Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]
query.reverse()

done = [False for _ in range(M)]
for i in range(Q):
    if query[i][0] == 1:
        done[query[i][1]-1] = True

uf = UnionFind(N)

for i, j in enumerate(done):
    if j:
        continue
    else:
        x, y = edges[i]
        uf.union(x,y)
ans = []
for q in range(Q):
    if  query[q][0] == 2:
        x,y = query[q][1:]
        x,y = x-1, y-1
        if uf.same(x,y):
            ans.append('Yes')
        else:
            ans.append('No')
    else:
        x,y = edges[query[q][1] -1]
        uf.union(x,y)
for i in ans[::-1]:
    print(i)


