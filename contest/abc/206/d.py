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
N = int(input())
A = [*map(int, input().split())]
if A == A[::-1]:
    print(0)
    exit()
kumi = set()
for i in range(N//2):
    if A[i] == A[N-1-i]:
        continue
    else:
        if A[i] < A[N-1-i]:
            a = A[i]
            b = A[N-1-i]
        else:
            a = A[N-1-i]
            b = A[i]
        kumi.add((a,b))
val2index = {}
index = 0
for a, b in kumi:
    if a not in val2index:
        val2index[a] = index
        index += 1
    if b not in val2index:
        val2index[b] = index
        index += 1
uf = UnionFind(index)
ans = 0
for a, b in kumi:
    i, j = val2index[a], val2index[b]
    if uf.same(i,j):
        continue
    else:
        uf.union(i,j)
        ans +=1
print(ans)

