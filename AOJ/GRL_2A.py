n , e = map(int, input().split())

G = [[] for _  in range(n)]

for _ in range(e):
    s, t, w = map(int, input().split())
    G[s].append([w, t])
    G[t].append([w, s])

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
print(minimum_spannning_tree(G))
        