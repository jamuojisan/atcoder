def  FloydWarshal(p, s):
    INF = 10**20
    dist = [[INF]*N for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0

    for i in range(N):
        for j in range(i+1,N):
            if A[i][j] == -1:
                dist[i][j] = p
                dist[j][i] = p
            else:
                dist[i][j] = A[i][j]
                dist[j][i] = A[j][i]
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            if dist[i][j] <= P:
                count += 1
    if count >= s:
        return True
    else:
        return False

N, P, K = map(int ,input().split())
A = [[*map(int, input().split())] for _ in range(N)]

# Infty check
if FloydWarshal(10**20, K):
    if FloydWarshal(10**20, K+1):
        print(0)
    else:
        print('Infinity')
    exit()

ok = 0
ng = 10 ** 20

while(ng - ok > 1):
    mid = (ok+ng)//2
    if FloydWarshal(mid, K+1):
        ok = mid
    else:
        ng = mid
ans = ok

ok = 0
ng = 10 ** 20
while(ng - ok > 1):
    mid = (ok+ng)//2
    if FloydWarshal(mid, K):
        ok = mid
    else:
        ng = mid
print(ok-ans)