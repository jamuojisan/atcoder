N  = int(input())



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

G =[[] for _ in range(N)]

cityx = []
cityy = []
for i in range(N):
    x, y = map(int, input().split())
    cityx.append([x,i])
    cityy.append([y,i])
cityx = sorted(cityx)
cityy = sorted(cityy) 
for index in range(N-1):
    x1, i = cityx[index]
    x2, j = cityx[index+1]
    G[i].append([abs(x1-x2), j])
    G[j].append([abs(x1-x2), i])

for index in range(N-1):
    y1, i = cityy[index]
    y2, j = cityy[index+1]
    G[i].append([abs(y1-y2), j])
    G[j].append([abs(y1-y2), i])

costs= minimum_spannning_tree(G, N)



print(sum(costs))
