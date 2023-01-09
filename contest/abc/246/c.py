import heapq
N, K, X = map(int ,input().split())
A = [*map(int, input().split())]
B = [-i for i in A]
heapq.heapify(B)
while(K>0 and len(B) > 0):
    v = heapq.heappop(B)
    v = -v
    n = v//X
    k = max(min(n, K),1)
    v = max(v-X*k, 0)
    K -= k
    if v != 0:
        heapq.heappush(B, -v)
print(-sum(B))


    


