import heapq
def minimum_spannning_tree(G):
    marked = [False]*N

    marked[0] = True
    marked_count = 1

    q = []

    for c, j in G[0]:
        heapq.heappush(q, [c,j])

    # 最小全域木の重みの合計を保存する変数
    ans = 0

    while marked_count < N:
        c, i = heapq.heappop(q)
        if marked[i]:
            continue
        
        marked[i] = True
        marked_count += 1
        ans -= c
        
        for c, j in G[i]:
            if marked[j]:
                continue
            heapq.heappush(q, [c, j])

    return ans


N , M = map(int, input().split())
A = [*map(int, input().split())]

G = [[] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        val = (pow(A[i], A[j],M) + pow(A[j], A[i], M)) % M
        G[i].append([-val, j])
        G[j].append([-val, i])
print((minimum_spannning_tree(G)))
