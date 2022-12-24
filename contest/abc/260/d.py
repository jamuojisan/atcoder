import heapq
n, k = map(int, input().split())
P = list(map(int, input().split()))

ans = {i:0 for i in range(1, n+1)}

field_top = set()
field = {}
for i, p in enumerate(P):
    print(field, field_top)
    tmp = {i for i in range(1,p+1)}
    target = list(field_top - tmp)
    if p==6:
        print(target)
        print(field_top)
    if len(target) == 0:
        field[p]=[p]
        field_top.add(p)
        # if len(field[target]) == k:
        #     print('ans', field[target])
        #     d = field.pop(target)
        #     for j in d:
        #         ans[j] = i+1
    else:

        heapq.heapify(list(target))
        if p == 6:
            print(target)
        target = heapq.heappop(target)
        if p == 6:
            print(target)
        field[target].append(p)
        field_top.remove(target)

        if len(field[target]) == k:
            print('ans', field[target])
            d = field.pop(target)
            for j in d:
                ans[j] = i+1
print(ans)
             



