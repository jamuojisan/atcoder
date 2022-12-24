
import heapq
def minimum_spannning_tree(G, n):
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
while(1):
    N = int(input())
    if N == 0:
        exit()
    G = [[] for _ in range(N)]
    import math
    IXYZR = []
    for i in range(N):
        x, y, z, r = map(float, input().split())
        IXYZR.append([i, x,y,z,r])

    for i, x1,y1, z1, r1 in IXYZR:
        for j, x2, y2, z2, r2 in IXYZR:
            if i == j:
                continue
            dis = max(math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2) -r1 - r2, 0)
            G[i].append([dis, j])
            G[j].append([dis, i])
    ans = round(sum(minimum_spannning_tree(G, N)),3)
    ans_digit = len(str(ans).split('.')[-1])
    
    if ans == 0:
        print('0.000')
    elif ans_digit < 3:
        print(str(ans) + '0' *(3-ans_digit))
    else:
        print(ans)