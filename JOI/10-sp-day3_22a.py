n , m , k = map(int, input().split())

G = [[] for _  in range(n)]

for _ in range(m):
    s, t, w = map(int, input().split())
    s, t = s-1, t-1
    G[s].append([w, t])
    G[t].append([w, s])

import heapq
def minimum_spannning_tree(G):
    marked = [False]*n
    costs = []
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
        costs.append(c)
        ans += c
        
        for c, j in G[i]:
            if marked[j]:
                continue
            heapq.heappush(q, [c, j])

    return costs
costs = minimum_spannning_tree(G)
print(sum(sorted(costs)[:len(costs)-(k-1)]))
