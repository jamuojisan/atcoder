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

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
def cordinate2index(i,j):
    return w*(i) + j -1 

h,w = map(int, input().split())
q = int(input())
field = set()
uf = UnionFind(h*w)

cnt = 0

for _ in range(q):
    t = list(map(int, input().split()))
    if len(t) == 3:
        y, x = t[1]-1, t[2] -1
        index = cordinate2index(y,x)
        field.add(index)
        for dy, dx in [[1,0], [-1, 0], [0,1], [0,-1]]:
            ny, nx = y+dy, x +dx
            nindex = cordinate2index(ny,nx)
            if ny < 0 or ny >= h or nx <0 or nx >=w:
                continue
            elif nindex  not in field:
                continue
            else:
                uf.union(index,nindex)
    else:
        y1, x1, y2, x2 = t[1]-1, t[2]-1, t[3]-1, t[4]-1
        index1 = cordinate2index(y1,x1)
        index2 = cordinate2index(y2,x2)
        if index1 in field and index2 in field:
            if uf.same(index1,index2):
                print('Yes')
            else:
                print('No')
        else:
            print('No')
