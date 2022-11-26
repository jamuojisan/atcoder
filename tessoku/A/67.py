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
        ans += c
        
        for c, j in G[i]:
            if marked[j]:
                continue
            heapq.heappush(q, [c, j])

    return ans
N, M  = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    a,b =a -1, b-1
    G[a].append([c,b])
    G[b].append([c, a])

print(minimum_spannning_tree(G))