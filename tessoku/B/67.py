
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

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u , v, c = map(int, input().split())
    u ,v= u-1 ,v-1
    G[u].append([-c, v])
    G[v].append([-c, u])

ans = minimum_spannning_tree(G)

print(-ans)