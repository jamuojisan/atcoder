from collections import deque

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

def dfs(visited, que):
    
    while(len(que) != 0):
        loc = que[0]
        que.popleft()
        # 探索
        next_ = hogehoge
        # 探索先を入れるかどうか
        if next not in set(visited):
            que.appendleft(next)
        


# 0-1 bfs
visited = {}
for i in range(n):
    for j in range(2):
        visited[(i,j)] = -1
visited[(0,0)] = 0
q =deque()
q.append((0,0))
fm = (0,0)
while(len(q) > 0):
    v = q.popleft()
    for nv in G2[v]:
        if visited[nv] != -1:
            continue
        if v[0] == nv[0]:
            visited[nv] = visited[v]
            q.appendleft(nv)
        else:
            visited[nv] = visited[v] + 1
            q.append(nv)
            
# ダイクストラ法
import heapq
def diekstra(G,a):
    q = []
    heapq.heappush(q, (0,a))
    visited = [-1 for _ in range(N)]
    done = [False for _ in range(N)]
    visited[a] = 0
    while(len(q) > 0):
        d, v= heapq.heappop(q)
        
        if done[v] :
            continue
        done[v] = True
        for (nv, c) in G[v]:
            if visited[nv] == -1 or visited[nv] > visited[v] + c:
                visited[nv] = visited[v] + c
                heapq.heappush(q, (visited[nv],nv))
    return visited

# bfs
from collections import deque
def bfs(G,a):
    visited = [-1 for _ in range(n)]
    visited[a] = 0
    q =deque()
    q.append(a)

    while(len(q) > 0):
        v = q.popleft()
        for nv in G[v]:
            if visited[nv] != -1:
                continue
            visited[nv] = visited[v] + 1
            q.append(nv)
    
    return visited

# bfs 2次元グリッドver
def bfs(c, y0, x0):
    visited = [[-1]*w for _ in range(h)]
    visited[y0][x0] = 0
    q =deque()
    q.append([y0,x0])

    while(len(q) > 0):
        y, x = q.popleft()
        for dy, dx in [[-1, 0], [1, 0], [0,-1], [0,1]]:
            ny , nx = y + dy, x+dx
            if ny < 0 or ny >=h or nx<0 or nx >=w:
                continue
            if visited[ny][nx] != -1 or c[ny][nx] == '#':
                continue
            visited[ny][nx] = visited[y][x] + 1
            q.append([ny,nx])
    
    return visited

# ワーシャルフロイド法
def  FloydWarshal()
    INF = 10**20
    dist = [[INF]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for _ in range(m):
        u, v, c = map_int()
        dist[u][v] = c


        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


# 最小全域木
 

n, m  = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    u , v, c = map(int, input().split())
    G[u].append([c, v])
    G[v].append([c, u])
import heapq
def minimum_spannning_tree(G):
    marked = [False]*n

    marked[0] = True
    marked_count = 1

    q = []

    for c, j in G[0]:
        heapq.heappush(q, [c,j])

    # 最小全域木の重みの合計を保存する変数
    ans = 0

    while marked_count < n:
        c, i = heapq.heappop(q)
        if marked[i]:
            continue
        
        marked[i] = True
        marked_count += 1
        ans += c
        
        for c, j in G[i]:
            if marked[j]:
                continue
            heapq.heappush(q, [c, j])

    return ans
        