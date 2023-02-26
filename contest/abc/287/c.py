from networkx.utils import UnionFind
N, M = map(int, input().split())
G = [[] for _ in range(N)]

uf = UnionFind(range(N))
n2c ={i:0 for i in range(N)}
for _ in range(M):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    G[u].append(v)
    G[v].append(u)
    n2c[u]+=1
    n2c[v]+=1
    if uf[u] == uf[v]:
        print('No')
        exit()
    uf.union(u,v)
all_group = [group for group in uf.to_sets()]

if len(all_group) != 1:
    print('No')
    exit()
count = 0

for n in n2c:
    if n2c[n] > 2 or n2c[n] == 0:
        print('No')
        exit()
    elif n2c[n] == 1:
        count += 1

if count == 2:
    print('Yes')
else:
    print('No')





